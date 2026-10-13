---
title: "Browser Caching: How to Set Cache-Control for a Faster Site"
meta_description: "Browser caching speeds up repeat visits. Learn Cache-Control, ETag, and versioned filenames, then set cache headers safely without serving stale pages."
slug: "cache-control-browser-caching-cara-mengatur-header"
focus_keyword: "browser caching"
category: "Performance"
image_alt: "Illustration of a browser keeping site files in a local cache so it does not download them again from the server"
date: "2026-10-13"
lang: "en"
---

# Browser Caching: How to Set Cache-Control for a Faster Site

The first visit to a website is always the heaviest, because the browser has to download HTML, CSS, JavaScript, fonts, and images. The second visit should be far lighter, since most of those files have not changed. That is what **browser caching** is for: the browser keeps copies of files on the visitor's device and reuses them without asking the server again. The catch is that a browser only knows how long it may keep a file if the server says so through HTTP headers. Without clear rules you get either pointless repeat downloads or, the opposite problem, an old version of the page that never updates.

## How the Browser Cache Works

When a browser requests a file, the server answers with the file and a set of headers. Those headers decide what happens on the next request, and there are two outcomes.

In the first, the copy is still considered fresh. The browser uses it straight from local storage and does not contact the server at all. This is the fastest path.

In the second, the copy has expired or must be revalidated. The browser asks the server whether the file changed, sending along the version marker it received earlier. If nothing changed, the server replies with 304 Not Modified and no file body. If it did change, the server sends the new version.

## The Headers Worth Knowing

- **Cache-Control**: the main header for cache behavior. Common values are max-age (how many seconds the copy counts as fresh), public and private (whether shared caches such as a CDN may store it), no-cache (store it, but validate before each use), no-store (never store it), and immutable (the file will not change during its fresh lifetime).
- **ETag**: a version marker for the file. The browser sends it back in an If-None-Match header to validate.
- **Last-Modified**: when the file last changed, paired with If-Modified-Since.
- **Expires**: the older way to set an expiry date. Modern browsers prefer Cache-Control: max-age when both are present.

A common misunderstanding: no-cache does not mean "do not store". It means "store it, but check with the server before using it". To forbid storage, use no-store.

## Treat Static Assets and HTML Differently

One rule for every file type is almost always wrong, because the files behave differently.

Static assets such as CSS, JavaScript, fonts, and images rarely change. They suit a long lifetime, for example Cache-Control: public, max-age=31536000, immutable, which equals one year.

HTML pages change often and carry current content. Give them a short lifetime, or use no-cache so they are always validated with an ETag. Pages that contain personal data, like a shopping cart or an account dashboard, should use private or no-store so they do not end up in a shared cache.

## Put the Version in the Filename

A one-year lifetime sounds risky: what if you update the CSS tomorrow? The answer is to put a version in the filename, such as app.3f9a1c.css, using a code generated from the file's contents. When the contents change, the name changes, and the HTML points to the new name. The browser treats it as a file it has never seen, while the old file stays safely cached for any page still using it.

Build tools like Vite and webpack generate these names for you. On a simple PHP site, a version parameter such as style.css?v=20261013 can also work, although some intermediate caches treat query strings inconsistently. A changed filename is the more reliable option.

## Applying It on the Server

On Nginx, the expires directive sets a lifetime per file type inside a location block, and add_header can add a specific Cache-Control value. On Apache, the mod_expires and mod_headers modules do the same through the main configuration or an .htaccess file. A PHP application that serves files itself, such as downloads, can set headers with the header() function before any output is sent. Hosting platforms and CDNs usually offer cache lifetime settings in their dashboards too.

## Mistakes That Come Up Often

- Giving a long lifetime to files whose names carry no version, so visitors keep seeing old CSS after an update.
- Caching dynamic HTML for too long, including pages that contain user data.
- Assuming no-cache is the same as no-store for sensitive data.
- Sending conflicting headers from several layers, for instance the application, the web server, and a CDN each adding their own rules.
- Forgetting that cookies and the Vary header can affect whether a response may be reused.

## How to Check the Result

Open DevTools in your browser, go to the Network tab, and reload the page twice. On the second load, files that were cached usually show up as served from memory cache or disk cache. Click a file and look at the Response Headers to confirm that Cache-Control matches your plan. Make sure the Disable cache option is unchecked, because it stops the test from reflecting real visitors. You can also inspect headers from a terminal with curl -I followed by the file URL. A PageSpeed Insights report also flags static files that lack an efficient cache lifetime.

## Wrapping Up

Browser caching is among the cheapest performance fixes there is: a few lines of configuration, with a benefit every time a visitor returns. Start by separating static assets from HTML, add versions to filenames, then give static assets a long lifetime. Test in DevTools before and after the change, and make sure pages with personal data stay out of shared caches.
