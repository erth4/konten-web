#!/usr/bin/env python3
"""Unggah artikel (ID + EN) beserta gambar OG ke API Maserta.

Contoh:
  python3 tools/upload-artikel.py --dir keuangan --category keuangan \
      --published-at 2026-10-12T09:00 slug-satu slug-dua slug-tiga
  python3 tools/upload-artikel.py --dir keuangan --category keuangan --dry-run slug-satu

Kredensial dibaca dari env MASERTA_USER dan MASERTA_PASS (cadangan: username dan password).
Dokumentasi API: https://maserta.my.id/api/docs
"""
import argparse, base64, html, http.cookiejar, json, os, re, sys, urllib.error, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAX_IMG = 5 * 1024 * 1024


def inline(s):
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html.escape(s, quote=False))


def md2html(md):
    out, lst, para = [], None, []

    def flush():
        nonlocal para
        if para:
            out.append('<p>' + inline(' '.join(para)) + '</p>')
            para = []

    def close():
        nonlocal lst
        if lst:
            out.append(f'</{lst}>')
            lst = None

    for ln in md.splitlines():
        s = ln.strip()
        if not s:
            flush(); close(); continue
        m = re.match(r'^(#{2,3})\s+(.*)', s)
        if m:
            flush(); close(); n = len(m.group(1)); out.append(f'<h{n}>{inline(m.group(2))}</h{n}>'); continue
        ul, ol = re.match(r'^[-*]\s+(.*)', s), re.match(r'^\d+\.\s+(.*)', s)
        if ul or ol:
            flush(); tag = 'ul' if ul else 'ol'
            if lst != tag:
                close(); out.append(f'<{tag}>'); lst = tag
            out.append('<li>' + inline((ul or ol).group(1)) + '</li>'); continue
        if s.startswith('>'):
            flush(); close(); out.append('<blockquote><p>' + inline(s.lstrip('> ')) + '</p></blockquote>'); continue
        close(); para.append(s)
    flush(); close()
    return '\n'.join(out)


def parse(path):
    text = path.read_text(encoding='utf-8')
    _, fm, body = text.split('---\n', 2)
    meta = {k: v.strip().strip('"') for k, v in re.findall(r'^(title|meta_description|image_alt):\s*(.*)$', fm, re.M)}
    body = re.sub(r'^\s*# .*\n', '', body, count=1)
    return meta, md2html(body)


def build(slug, a):
    d = ROOT / 'artikel' / a.dir
    idm, idb = parse(d / f'{slug}.md')
    enm, enb = parse(d / f'{slug}.en.md')
    img = ROOT / 'og' / f'{slug}.jpg'
    if img.stat().st_size > MAX_IMG:
        raise SystemExit(f'{img} lebih dari 5 MB')
    p = dict(
        title=idm['title'], excerpt=idm['meta_description'], body=idb, slug=slug, status='published',
        published_at=a.published_at,
        image_base64='data:image/jpeg;base64,' + base64.b64encode(img.read_bytes()).decode(),
        image_alt=idm.get('image_alt') or f"Ilustrasi: {idm['title']}"[:200],
        title_en=enm['title'], excerpt_en=enm['meta_description'], body_en=enb,
        image_alt_en=enm.get('image_alt') or f"Illustration: {enm['title']}"[:200],
        category_slug=a.category,
    )
    errs = []
    if not 5 <= len(p['title']) <= 160: errs.append('title 5-160 karakter')
    if not 30 <= len(p['excerpt']) <= 300: errs.append('excerpt 30-300 karakter')
    if len(p['title_en']) > 160: errs.append('title_en maks 160 karakter')
    if not 30 <= len(p['excerpt_en']) <= 300: errs.append('excerpt_en 30-300 karakter')
    if errs:
        raise SystemExit(f'{slug}: ' + '; '.join(errs))
    return p


class Api:
    def __init__(self, base):
        self.base = base
        self.op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))

    def call(self, path, data=None, token=None):
        h = {}
        if data is not None: h['Content-Type'] = 'application/json'
        if token: h['X-CSRF-Token'] = token
        rq = urllib.request.Request(self.base + path, data=None if data is None else json.dumps(data).encode(), headers=h)
        try:
            with self.op.open(rq, timeout=60) as r:
                return r.status, json.load(r)
        except urllib.error.HTTPError as e:
            return e.code, json.load(e)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('slugs', nargs='+')
    ap.add_argument('--dir', required=True, help='subfolder di artikel/, mis. keuangan')
    ap.add_argument('--category', required=True, help='slug kategori di Maserta, mis. keuangan, toko')
    ap.add_argument('--published-at', required=True, help='YYYY-MM-DDTHH:mm, zona Asia/Jakarta (disarankan jam 09:00)')
    ap.add_argument('--base-url', default=os.environ.get('MASERTA_BASE_URL', 'https://maserta.my.id'))
    ap.add_argument('--dry-run', action='store_true', help='validasi dan tampilkan ukuran, tanpa login')
    a = ap.parse_args()

    arts = [build(s, a) for s in a.slugs]
    for p in arts:
        print(f"OK {p['slug']}: judul {len(p['title'])}, ringkasan {len(p['excerpt'])}/{len(p['excerpt_en'])}, "
              f"body {len(p['body'])}/{len(p['body_en'])} byte, gambar {len(p['image_base64'])} char")
    if a.dry_run:
        return

    user = os.environ.get('MASERTA_USER') or os.environ.get('username')
    pw = os.environ.get('MASERTA_PASS') or os.environ.get('password')
    if not user or not pw:
        sys.exit('Set MASERTA_USER dan MASERTA_PASS di environment.')

    api = Api(a.base_url)
    st, r = api.call('/admin/api/csrf')
    st, r = api.call('/admin/api/login', {'username': user, 'password': pw}, r['data']['csrf_token'])
    if st != 200:
        sys.exit(f'Login gagal ({st}): {r.get("message")}')
    token = r['data']['csrf_token']

    st, r = api.call('/admin/api/kategori-artikel')
    slugs = [c['slug'] for c in r['data']]
    if a.category not in slugs:
        api.call('/admin/api/logout', {}, token)
        sys.exit(f'Kategori "{a.category}" tidak ada. Pilihan: {", ".join(slugs)}')

    failed = False
    for p in arts:  # tanpa retry otomatis: API tidak punya kunci idempotensi
        st, r = api.call('/admin/api/artikel', p, token)
        d = r.get('data') or {}
        print(f"{p['slug']} -> {st} {r.get('message')} id={d.get('id')} terbit={d.get('published_at')}")
        if st != 201:
            print(json.dumps(d, ensure_ascii=False)); failed = True; break
    api.call('/admin/api/logout', {}, token)
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
