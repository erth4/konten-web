#!/usr/bin/env python3
"""Ubah tanggal terbit artikel yang sudah ada lewat form edit panel admin (API tidak punya endpoint ubah).

Contoh: python3 -I tools/ubah-tanggal-artikel.py 2026-10-14T09:00 48 49 50
Waktu dalam Asia/Jakarta. Semua field lain dikirim ulang apa adanya; skrip mencetak field yang berubah.
Kredensial: MASERTA_USER dan MASERTA_PASS.
"""
import os,sys,json,re,html,http.cookiejar,urllib.request,urllib.parse
from html.parser import HTMLParser
B='https://maserta.my.id'; NEW=sys.argv[1]; IDS=sys.argv[2:]
op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
def req(path,data=None,json_body=None,tok=None):
    h={}
    if json_body is not None: data=json.dumps(json_body).encode(); h['Content-Type']='application/json'
    elif data is not None: data=urllib.parse.urlencode([(k,'' if v is None else v) for k,v in data]).encode(); h['Content-Type']='application/x-www-form-urlencoded'
    if tok: h['X-CSRF-Token']=tok
    rq=urllib.request.Request(B+path,data=data,headers=h)
    try:
        with op.open(rq,timeout=60) as r: return r.status,r.read().decode(),r.geturl()
    except urllib.error.HTTPError as e: return e.code,e.read().decode(),path
class P(HTMLParser):
    def __init__(s): super().__init__(convert_charrefs=True); s.forms=[]; s.cur=None; s.ta=None; s.sel=None; s.fields=[]
    def handle_starttag(s,tag,a):
        a=dict(a)
        if tag=='form': s.cur={'action':a.get('action'),'fields':[]}; s.forms.append(s.cur)
        if s.cur is None: return
        if tag=='input':
            t=a.get('type','text'); n=a.get('name')
            if not n or t in('file','button','submit'): return
            if t in('checkbox','radio') and 'checked' not in a: return
            s.cur['fields'].append([n,a.get('value','')])
        elif tag=='textarea': s.ta=[a.get('name'),'']
        elif tag=='select': s.sel=[a.get('name'),None,None]
        elif tag=='option' and s.sel is not None:
            if 'selected' in a: s.sel[1]=a.get('value')
            elif s.sel[2] is None: s.sel[2]=a.get('value')
    def handle_data(s,d):
        if s.ta is not None: s.ta[1]+=d
    def handle_endtag(s,tag):
        if tag=='textarea' and s.ta: s.cur['fields'].append(s.ta); s.ta=None
        if tag=='select' and s.sel: s.cur['fields'].append([s.sel[0],s.sel[1] if s.sel[1] is not None else s.sel[2]]); s.sel=None
        if tag=='form': s.cur=None
def form(id):
    st,h,_=req(f'/admin/artikel/{id}/ubah'); p=P(); p.feed(h)
    f=[x for x in p.forms if x['action'] and 'logout' not in x['action']][0]; return f
st,b,_=req('/admin/api/csrf'); tok=json.loads(b)['data']['csrf_token']
st,b,_=req('/admin/api/login',json_body={'username':os.environ['MASERTA_USER'],'password':os.environ['MASERTA_PASS']},tok=tok); assert st==200; tok=json.loads(b)['data']['csrf_token']
for id in IDS:
    f=form(id); d={k:v for k,v in f['fields']}
    before={k:v for k,v in f['fields'] if k!='_csrf'}
    print(id,f['action'],'old',d['published_at'],'status',d['status'],'fields',len(f['fields']))
    f['fields']=[[k,(NEW if k=='published_at' else v)] for k,v in f['fields']]
    st,b,url=req(f['action'],data=f['fields']); print(' POST',st,url)
    a={k:v for k,v in form(id)['fields'] if k!='_csrf'}
    diff=[k for k in a if a[k]!=before.get(k)]; print(' changed fields:',diff,'->',a['published_at'])
req('/admin/api/logout',json_body={},tok=tok)
