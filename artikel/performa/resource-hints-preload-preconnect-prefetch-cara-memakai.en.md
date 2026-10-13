---
title: "Resource Hints: How to Use Preload, Preconnect, and Prefetch"
meta_description: "Resource hints tell the browser what it needs early. Learn preload, preconnect, dns-prefetch, prefetch, and fetchpriority, plus the pitfalls to avoid."
slug: "resource-hints-preload-preconnect-prefetch-cara-memakai"
focus_keyword: "resource hints"
category: "Performance"
image_alt: "Illustration of a web page preparing connections to several external domains before the resources are requested"
date: "2026-10-13"
lang: "en"
---

# Resource Hints: How to Use Preload, Preconnect, and Prefetch

A browser discovers a page's resources in stages. It reads the HTML, learns that a stylesheet exists, and only after downloading that stylesheet finds out about the font and background image inside it. Every late discovery means a download that starts late. **Resource hints** are cues you add to the page so the browser knows earlier what it will need, and can start connections and downloads without waiting. Used well, they cut delays that were never necessary. Used carelessly, they waste bandwidth.

## Why Late Discovery Is a Problem

Before downloading anything from another domain, the browser must resolve DNS, open a TCP connection, and negotiate TLS for HTTPS. This takes time before a single byte of content arrives. If your fonts or scripts live on a third-party domain, that sequence only begins once the browser spots the reference. Resource hints move some of that work to the very start.

## Five Hints Worth Knowing

**dns-prefetch** only asks the browser to resolve a domain's DNS ahead of time. It is lightweight and widely supported, a good fallback for domains you might use.

**preconnect** goes further: DNS, connection, and TLS are all prepared together. Use it for third-party domains you are sure to need early in the load, such as a font service or an image CDN. For fonts, add the crossorigin attribute because fonts are fetched in CORS mode. A prepared connection that goes unused for a while gets closed, so do not scatter it across many domains.

**preload** tells the browser to download one specific resource right away with high priority, because you know this page needs it. The as attribute is required so the browser knows the type, for example as="font", as="style", or as="image". Preloaded fonts also need the crossorigin attribute, even when they come from your own domain.

**prefetch** is different in nature: it downloads a resource that may be needed on the next page, at low priority while the browser is idle. An example is fetching the checkout page's script while the visitor is still in the cart.

**fetchpriority** is not a connection hint but a priority marker. fetchpriority="high" on the main image helps the browser fetch it first, while fetchpriority="low" lowers the priority of less urgent images.

## Sensible Use Cases

- **The main image on a home page.** A hero image is often the LCP element. If it is called from CSS, the browser only learns about it after parsing the CSS. Preloading it, or moving it into an img tag with fetchpriority="high", gets it downloading earlier.
- **A custom font.** Preload one or two font files used by above-the-fold text, together with font-display: swap so text is not held back.
- **External services.** If your site uses a separate domain for key images or scripts, preconnecting to it saves time at the start.
- **Sequential flows.** In an online shop, prefetching the payment page from the cart page speeds up the next step.

## Pitfalls to Avoid

First, do not preload too much. Each preload competes with other important resources for the same bandwidth. If everything is a priority, nothing is.

Second, an unused preload is waste. Browsers usually print a console warning when a preloaded resource is not used. Make sure the URL and attributes match exactly what the page uses, including crossorigin on fonts, or the file may be downloaded twice.

Third, do not put loading="lazy" on the LCP image. Lazy loading suits below-the-fold images, but on the main image it delays rendering.

Fourth, remember that support and behavior of each hint can differ between browsers. Always test rather than rely on assumptions.

## How to Apply and Measure

These hints are written as link tags inside the head, or sent from the server in an HTTP Link header. On WordPress and other CMSs, a theme or performance plugin sometimes offers settings for them, but still check the final output in the page source.

To measure, open the Network tab in DevTools and study the waterfall: do the important resources now start earlier? Compare the LCP value before and after in Lighthouse, and check real-user data such as the Chrome UX report if your site has any. Change one thing at a time so it is clear what made the difference.

## Wrapping Up

Resource hints are a precision tool, not an automatic speed button. The principle is simple: tell the browser about the things you are certain to need sooner, and let everything else flow as usual. Start with a single candidate, such as the LCP image or the font domain, test the impact, and add more only when the data supports it.
