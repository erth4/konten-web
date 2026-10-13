---
title: "Canonical URLs: How to Fix Duplicate Content on Your Site"
meta_description: "A canonical URL marks the main version of similar pages. Learn what causes duplicate content, how to set rel canonical, when to redirect, and how to check it."
slug: "canonical-url-konten-duplikat-cara-mengatasi"
focus_keyword: "canonical URL"
category: "SEO"
image_alt: "Illustration of several similar page addresses with one address marked as the main version"
date: "2026-10-16"
lang: "en"
---

# Canonical URLs: How to Fix Duplicate Content on Your Site

A page can have more than one address without you noticing. Addresses with and without www, http and https versions, URLs with tracking parameters, or the same listing with filters in a different order can all show identical content. For a search engine that is confusing: which one should collect the signals and appear in search results? This is where the **canonical URL** comes in, a marker that names the main version among a set of similar pages.

## What a Canonical URL Is

A canonical URL is the address you declare as the preferred version of a page. It is usually added with a link tag in the head, using rel="canonical" and an href holding the full address of the main version. For files such as PDFs, the marker can be sent in an HTTP header instead.

Understand that canonical is a hint, not a command. Google weighs it together with other signals such as redirects, internal links, and sitemap contents, then picks the version it considers best. That is why your signals should agree with each other.

On the common worry: ordinary duplicate content does not automatically get a site penalized. The real problem is waste and ambiguity: signals get spread across several addresses, and Google may choose a version you did not want.

## What Causes Duplicate Content

- Protocol and domain variations: http and https, www and non-www.
- A trailing slash, or differences in upper and lower case in the path.
- URL parameters for tracking such as utm, sessions, or product sorting and filters.
- Print pages, old AMP versions, or separate mobile versions.
- Category archives, tags, and pagination on a CMS that show the same snippets of content.
- Product variants with nearly identical descriptions in an online shop.
- Content that is copied or syndicated to other sites.

## How to Set Canonicals Properly

1. **Choose one main version** for each page and use it consistently across the site.
2. **Use full absolute addresses**, including https and the domain name, not relative ones.
3. **Add a canonical to every page, including self-referencing ones.** A self-referencing canonical protects against unexpected parameter variations.
4. **Place it in the head of the document.** A canonical tag that appears in the body is usually ignored.
5. **Point to an equivalent page.** Do not point a canonical from a page with different content just to gather signals, because the hint may be ignored.

On WordPress, SEO plugins usually add canonicals automatically. Still check the output, especially for archive pages and pages with parameters. On a custom-built site, write a function that builds a clean address from the page path and strips parameters that do not change the content.

## Canonical or 301 Redirect

The two often get mixed up. Use a **301 redirect** when the old address no longer needs to be reachable, for instance forcing http to https or www to non-www. Visitors and crawlers are moved straight away. Use a **canonical** when both addresses must stay reachable for users but you want only one as the main version, such as pages with filter parameters.

## Mistakes to Avoid

- A canonical pointing to a 404 page or to a redirected page.
- Several different canonical tags on one page, for example one from the theme and one from a plugin.
- Combining canonical with noindex on the same page, sending contradictory messages.
- Putting non-canonical addresses in the sitemap. The sitemap should contain only main versions.
- Pointing all pagination pages to the first page when their contents differ.

## How to Check Canonicals

View the page source and look for the rel="canonical" tag in the head, then confirm the address matches your plan. In Google Search Console, the URL Inspection tool shows two important pieces of information: the user-declared canonical and the Google-selected canonical. If they differ, find out why, for instance internal links pointing to another version or content that turns out not to be similar enough. The Page indexing report also lists statuses such as duplicate without user-selected canonical, a useful starting point for an audit.

## Wrapping Up

Canonical URLs do not change your site's content, but they tidy up how search engines understand it. Begin by unifying the domain version with redirects, add self-referencing canonicals to all pages, then deal with the parameters and archives that create duplicates. Make sure every signal, from internal links to the sitemap, points to the same main address.
