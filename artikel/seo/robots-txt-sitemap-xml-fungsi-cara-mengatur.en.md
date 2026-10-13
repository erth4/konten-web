---
title: "Robots.txt and XML Sitemaps: What They Do and How to Set Them Up"
meta_description: "Robots.txt controls what may be crawled; an XML sitemap points to key pages. Learn their roles, differences, sample rules, and mistakes that can hurt your SEO."
slug: "robots-txt-sitemap-xml-fungsi-cara-mengatur"
focus_keyword: "robots.txt"
category: "SEO"
image_alt: "Illustration of a crawler robot at a site gate with a page map and lists of allowed and disallowed paths"
date: "2026-10-16"
lang: "en"
---

# Robots.txt and XML Sitemaps: What They Do and How to Set Them Up

Two small files at the root of your site play a big part in how search engines treat your website: **robots.txt** and the XML sitemap. They are often mentioned together and often have their roles confused. Robots.txt tells crawlers which parts they may or may not visit, while the XML sitemap hands over a list of the pages you want to show. Getting this wrong can have serious effects, from important pages never being crawled to pages appearing in results when you wanted them hidden.

## What Robots.txt Does

Robots.txt is a plain text file that must sit at the root of the domain, for example yourdomain.com/robots.txt. Well-behaved crawlers, Googlebot included, read it before exploring the site. It contains rules for particular user agents.

The most common directives:

- **User-agent**: names which crawler the rules apply to. An asterisk means all crawlers.
- **Disallow**: blocks crawling of a given path.
- **Allow**: permits a given path, useful as an exception inside a blocked path.
- **Sitemap**: points to the full address of your XML sitemap.

A simple example that blocks an admin folder for all crawlers and points to the sitemap reads: User-agent: *, then Disallow: /admin/ on the next line, then Sitemap: https://yourdomain.com/sitemap.xml. Note that paths are case sensitive.

## What Robots.txt Does Not Do

This is the most misunderstood part. Robots.txt controls **crawling**, not **indexing**. A page blocked in robots.txt can still appear in search results without a description if other sites link to it. To keep a page out of the index, use a meta robots noindex tag or an X-Robots-Tag header, and make sure the page can still be crawled, because the crawler has to be able to read the noindex instruction.

Robots.txt is also not a security tool. The file is public, so listing a secret path there shows it to anyone. Protect sensitive data with authentication, not with Disallow.

Finally, do not block the CSS and JavaScript files needed to render pages. Google needs to load them to understand how a page looks and what it contains.

## What an XML Sitemap Does

An XML sitemap is a list of URLs you want to present to search engines, in a machine-readable format. It helps page discovery, especially for large sites, new sites with few inbound links, or pages rarely linked from other pages. A sitemap does not guarantee that a page will be crawled or indexed, but it makes discovery easier.

Each entry needs at minimum the full address in a loc element. A lastmod element holds the date of the last change and is useful when accurate. Google has said it ignores the priority and changefreq elements, so there is no need to fill them in.

A single sitemap file is limited to 50,000 URLs or 50 MB uncompressed. Larger sites use a sitemap index, a file that lists several sitemaps.

## The Differences at a Glance

- Robots.txt blocks or allows crawling. A sitemap suggests pages to discover.
- Robots.txt is one file per host. Sitemaps can be many files.
- Robots.txt does not guarantee a page stays out of the index. A sitemap does not guarantee a page gets indexed.

## Building a Healthy Sitemap

1. **Include only pages you want indexed.** Avoid URLs that redirect, return 404, carry noindex, or are not the canonical version.
2. **Use consistent main addresses**, including https and your chosen www or non-www version.
3. **Fill in lastmod only when it is true.** Changing it daily without real changes makes the signal useless.
4. **Generate it automatically.** WordPress SEO plugins and many frameworks can build it. On a custom PHP site, write a script that reads the page list from the database.
5. **Register it.** Submit the sitemap in Google Search Console and also reference it with the Sitemap line in robots.txt.

## Costly Mistakes That Happen Often

- A Disallow: / left over from development, blocking the entire site.
- Blocking folders that hold images, CSS, or JavaScript that matter.
- Relying on robots.txt to hide pages from search results.
- A sitemap full of thousands of error or redirected URLs.
- Forgetting to update the sitemap after the site structure changes.

## How to Check

Open yourdomain.com/robots.txt in a browser and confirm the content is what you expect. The robots.txt report in Google Search Console shows which file Google read and any parsing problems. In the Sitemaps report, check the submission status, the number of URLs discovered, and any reported errors. After changing rules, test a few important URLs with the URL Inspection tool to be sure they are not blocked.

## Wrapping Up

Robots.txt and XML sitemaps are simple, but one small mistake can have wide impact. Keep the principle: robots.txt to manage crawling, noindex to keep pages out of the index, and the sitemap as your list of best pages. Review both files whenever the site changes in a big way.
