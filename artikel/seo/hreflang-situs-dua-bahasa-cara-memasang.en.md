---
title: "Hreflang: How to Set Up SEO for a Two-Language Website"
meta_description: "Hreflang tells Google which language version suits each visitor. Learn the rules, code examples, common mistakes, and how to test it on a two-language site."
slug: "hreflang-situs-dua-bahasa-cara-memasang"
focus_keyword: "hreflang"
category: "SEO"
image_alt: "Illustration of two pages in different languages linked by arrows, with language code labels above them"
date: "2026-10-23"
lang: "en"
---

# Hreflang: How to Set Up SEO for a Two-Language Website

You've translated your article into English. It's tidy, readable, ready to show off. Then someone overseas searches that topic on Google and the Indonesian version comes up. They frown, hit the back button, and your translation never gets read. That is the problem **hreflang** exists to solve.

Offering two languages isn't enough. Search engines need to know the two pages are a pair, so each visitor is steered to the right one. That's the job of **hreflang**.

## What Hreflang Does

Hreflang is an annotation telling search engines that a page has another version in a different language or region. With it, Google can show the version that best fits the user's language and location: readers from Indonesia see the Indonesian page, English readers see the English one.

It's a signal, not a command. Google still makes the call, so don't expect hreflang to guarantee that a particular version always appears.

Without it, annoying things can happen: the wrong version shows up for the wrong reader, Google can't decide between two similar pages, and signals like inbound links get scattered across two addresses with no clear link between them. Translations generally aren't treated as duplicates, but the annotation still makes the relationship clear.

## How to Write It

You can put the annotation in three places: link elements in the page head, HTTP headers, or an XML sitemap. For a small site, link elements in the head are easiest. According to Google's guidance, each page carries a set of link elements, one for every version including itself, and the set is identical across all versions.

An example for one article with Indonesian and English versions:

```
<link rel="alternate" hreflang="id" href="https://example.id/artikel/cara-membuat-cv" />
<link rel="alternate" hreflang="en" href="https://example.id/en/artikel/how-to-write-a-cv" />
<link rel="alternate" hreflang="x-default" href="https://example.id/artikel/cara-membuat-cv" />
```

What it means:

- `hreflang="id"` marks the Indonesian version, using a two-letter language code.
- `hreflang="en"` marks the English version. For a specific region, use the language-region format such as en-gb.
- `x-default` is the fallback page for visitors whose language isn't on the list, or a language-picker page.
- `href` must be a full address, including https.

## The Rules That Get Broken Most

**It must be reciprocal.** If page A points to B as another version, B has to point back to A. Sources outside Google say one-way links get ignored, and it's the most common mistake of all.

**Include itself.** Every page lists itself in the set.

**Real equivalents only.** Link pages that truly say the same thing. Two pages that merely share a topic aren't a pair.

**Valid language codes.** "in" or "eng" aren't recognized. An annotation with a wrong code is as good as none.

**Addresses must be reachable.** Don't point to pages that redirect, are blocked, or error out.

**One method only.** Choose link elements, headers, or the sitemap, and don't mix them for the same set of addresses so they don't contradict each other.

## Hreflang and Canonical Have to Get Along

Each language version should have a canonical pointing to itself. The classic blunder: setting the English version's canonical to the Indonesian page. That's like telling Google, "this English page is just a copy," and the whole point of hreflang disappears.

## Address Structure

There are three common patterns. Subfolders (example.id/ and example.id/en/) are easy to manage and typical for small to mid-sized sites. Subdomains (en.example.id) are more separate but need more setup. A different domain per country suits big businesses, though it's much heavier to maintain. Keep in mind that Google doesn't guess the target audience from subdomain names, so the mapping has to be stated through hreflang.

## An Annotation Won't Rescue a Bad Translation

Hreflang handles the pointing, not the quality. If your English version is stiff, raw machine output, readers will feel it within two paragraphs and leave. Write it naturally. Adapt the titles, meta descriptions, image alt text, and internal links too, so they lead to the same language version.

One detail people often miss: the language switcher should point to the counterpart of the page currently open, not always the home page. Someone changing language usually wants the same article.

## How to Check

1. Open the page source and make sure the link elements are there, complete, and identical across versions.
2. Test reciprocity: from Indonesian to English, then from English back to Indonesian.
3. Use a testing tool in Google Search Console, or a third-party hreflang checker if you have one.
4. Look at the Indexing report in Search Console for signs of trouble on alternate pages.
5. Try searching from different locations and browser languages.

After changing anything, be patient. Google needs time to recrawl.

If you only have time for one thing today, check a single article: does its counterpart point back? If not, start there.
