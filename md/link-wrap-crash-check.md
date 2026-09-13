# Link wrap crash check

Regression check for [suzuri#56](https://github.com/harrywang/suzuri/issues/56): opening a note with a long, soft-wrapping line holding several links, followed by a heading, killed the app on a fold-map assertion before a window was usable. The fix stops the wrap map from breaking a line inside a link placeholder before that placeholder has been measured.

**How to run this check.** Close Suzuri, then open this vault and this note from a terminal so a panic is visible:

```sh
ZED_RELEASE_CHANNEL=nightly RUST_BACKTRACE=1 target/release-fast/zed ~/sandbox/suzuri-testbed ~/sandbox/suzuri-testbed/md/link-wrap-crash-check.md
```

Every section below must simply render. On a broken build the app exits with code 1 the moment this note opens, and the terminal shows `assertion failed: transform.placeholder.is_none()`.

- [ ] The note opened and this checklist is visible.
- [ ] Section 1 shows one wrapped bullet with six link labels, then a rendered heading.
- [ ] Narrowing the window until every line rewraps does not crash.
- [ ] Section 2 shows a link whose label is one unbreakable bare URL; it sits on its own wrap row rather than being split mid-URL.
- [ ] Section 3 shows a link whose label is longer than 128 bytes.
- [ ] Sections 4 and 5, the two shapes that never crashed, still render.
- [ ] Moving the cursor onto each link reveals its source, and moving away conceals it again.

## 1. The reporter's file

This is the reporter's three-line reproduction, verbatim: one long bullet with six links whose labels contain spaces, a blank line, and a `###` heading. Both properties were needed to crash: a line long enough to soft-wrap, and links on it.

- One-year house outlooks that are often mistaken for CMAs: [Allianz Global Investors](https://www.allianzgi.com/en/insights/outlook-and-commentary/outlook-2026), [Pictet](https://am.pictet.com/us/en/investment-views/multi-asset/2025/annual-outlook-for-2026), [Nordea](https://www.nordea.com/en/news/setting-the-plan-for-your-financial-year-2026-get-insights-from-our-local-experts), [Columbia Threadneedle](https://www.columbiathreadneedle.com/en/gb/intermediary/global-outlooks-2026/), [Goldman Sachs AM](https://am.gs.com/en-us/advisors/insights/article/investment-outlook/public-markets-2026), [Wellington](https://www.wellington.com/en/insights/2026-macro-outlook). These carry views, not full return-volatility-correlation grids.

### Access mode per publisher

## 2. A label with no space to break at

A bare URL used as its own label gives the wrapper no word boundary. It must move to the next row whole, never be cut mid-URL.

Please review [https://www.example.com/students/support/policies/academic-integrity/and/conduct/overview](https://www.example.com/students/support/policies/academic-integrity/and/conduct/overview) before class.

### Heading after the bare-URL label

## 3. A label over 128 bytes

The tab map tracks each chunk's characters in a 128-bit bitmap, so a placeholder longer than that is cut down before it becomes display text. The rendered link still shows the full label.

Please review [https://www.example.com/students/support/policies/academic-integrity/students/support/policies/academic-integrity/students/support/policies/academic-integrity/students/support/policies/academic-integrity/](https://www.example.com/students/support/policies/academic-integrity/students/support/policies/academic-integrity/students/support/policies/academic-integrity/students/support/policies/academic-integrity/) before class.

### Heading after the long label

## 4. Same length, no links

The reporter's control case: this never crashed, because there is no placeholder to wrap into.

- lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet

### Heading after the plain line

## 5. Six links, short line

The reporter's other control case: links, but no wrapping.

- a [b](https://x.com/1) c [d](https://x.com/2) e [f](https://x.com/3) g [h](https://x.com/4) i [j](https://x.com/5) k [l](https://x.com/6)

### Heading after the short line
