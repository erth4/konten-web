---
title: "Render-Blocking Resources: How to Fix CSS and JavaScript Delays"
meta_description: "Render-blocking resources keep your page from showing. Learn defer vs async, critical CSS, and how to cut CSS and JavaScript that hold back rendering."
slug: "render-blocking-resources-cara-mengatasi-css-javascript"
focus_keyword: "render-blocking resources"
category: "Performance"
image_alt: "Illustration of a page load timeline: a blocking script holds back rendering while a deferred script runs after the page appears"
date: "2026-10-13"
lang: "en"
---

# Render-Blocking Resources: How to Fix CSS and JavaScript Delays

Have you ever opened a website and stared at a blank screen for a moment before anything appeared, even though your connection was fine? Very often the cause is **render-blocking resources**: CSS or JavaScript files that make the browser postpone drawing the page until they have been downloaded and processed. The "Eliminate render-blocking resources" audit in Lighthouse and PageSpeed Insights points at exactly this. This article explains what is actually being blocked and how to deal with it without breaking your layout.

## What Gets Blocked and Why

The browser reads HTML from top to bottom to build the page structure. Two kinds of resources can halt that process or the painting that follows.

**CSS blocks rendering.** The browser will not show a page before it knows the styles, so visitors do not see plain text that suddenly changes. Every stylesheet in the head must therefore finish loading before the page is drawn.

**Synchronous JavaScript blocks the parser.** A plain script tag without attributes makes the browser stop reading HTML, download the script, run it, and only then continue. Scripts can also wait on CSS listed above them, so the delays stack up.

You feel the effect in metrics such as First Contentful Paint and Largest Contentful Paint, because the first content only appears once every blocker is done.

## defer, async, and Modules

The most direct fix for scripts that get in the way is an attribute on the script tag.

- **defer**: the script downloads while HTML keeps being parsed, then runs after the document is parsed, in the order written. It is the safe choice for most application scripts.
- **async**: the script downloads while HTML is parsed and runs as soon as it arrives, with no guaranteed order. It suits standalone scripts such as an analytics counter.
- **type="module"**: module scripts behave like defer by default.

Watch out for one trap: scripts that depend on each other should not use async, because the order is not guaranteed. Inline scripts that rely on a library such as jQuery can also fail if that library is loaded later with defer. Change them one at a time and test each change.

## Handling Blocking CSS

CSS cannot simply be postponed, but there are several ways to lighten the load.

1. **Remove unused CSS.** The Coverage panel in Chrome DevTools shows which parts of a stylesheet the page never uses. Frameworks loaded in full often contribute many unused rules.
2. **Split by condition.** A print stylesheet can carry media="print" so it does not block on-screen rendering.
3. **Critical CSS.** Rules needed for the initial view, meaning the area above the fold, go directly into a style tag in the head. The rest loads separately without blocking. It works well but adds maintenance effort, so reserve it for pages that really matter, such as the home page or a landing page.
4. **Minify and compress.** Smaller files finish downloading sooner. Combine this with Brotli or Gzip compression and browser caching.

## Fonts and Third-Party Scripts

Fonts can also hold text back. Set font-display: swap in your font declarations so text is readable in a fallback font until the main font is ready, and load only the weights and styles you actually use.

Third-party scripts such as chat widgets, ad trackers, and tag managers are often the biggest blockers because they are outside your control. Load them with async or defer, hold them back until a user interaction when possible, and review regularly whether you still need each one. Every script you no longer use is a free load you can remove.

## A Suggested Workflow

1. Run Lighthouse or PageSpeed Insights and note the files flagged as blocking.
2. Open the Performance tab in DevTools to see when the first paint happens and what delays it.
3. Start with scripts: add defer to application scripts and async to standalone ones.
4. Clean out unused CSS, then consider critical CSS for priority pages.
5. Test every interactive feature: menus, forms, sliders, and the shopping cart.
6. Measure again and compare. If the result does not improve, revert the last change and try another approach.

## WordPress and Other CMS Users

On WordPress the main cause is usually a theme and plugins that load many files on every page. Optimization plugins can add defer and generate critical CSS automatically, but results differ from site to site and sometimes break the layout. Enable one feature at a time, test on a mobile device, and keep an easy way to undo it. Deactivating rarely used plugins often gives a bigger gain than any technical trick.

## Wrapping Up

Render-blocking resources are not an enemy to eliminate completely. Some CSS genuinely has to be present before the page is drawn. The goal is to make sure only what the first view truly needs gets in the way, while everything else waits its turn. Start with defer on scripts, trim excess CSS, and measure the result after every step.
