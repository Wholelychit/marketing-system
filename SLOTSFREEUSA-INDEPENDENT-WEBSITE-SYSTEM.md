# SlotsFreeUSA Independent Website System

Last updated: 2026-05-28

## Purpose

This file defines the operating standard for `slotsfreeusa.com` so the website can stand on its own without ChatGPT being open.

The live website must be usable, crawlable, reviewable, and fast as a normal public website.

## Non-Negotiable Website Rule

`slotsfreeusa.com` must run independently.

That means:

1. The GitHub website repo owns the code.
2. GitHub Pages or Cloudflare Pages hosts the public site.
3. Visitors can open and use the site without ChatGPT.
4. Google can crawl the site.
5. Affiliate managers can review the site without needing explanations in chat.
6. The site stays fast, simple, mobile-first, and beginner-friendly.

## Correct Repository Roles

| Repository | Role |
|---|---|
| `Wholelychit/slotsfreeusa.com` | Website code, pages, images, CSS, JavaScript, robots.txt, sitemap.xml, legal/disclosure pages |
| `Wholelychit/marketing-system` | Marketing plans, content queue, affiliate outreach, campaign scripts, SEO strategy, review system |

Do not put production website code inside this marketing repo.

## Independent Site Minimum Requirements

The website repo should contain these public files/pages before serious affiliate outreach:

1. `index.html` — homepage with clear adult-focused positioning.
2. `robots.txt` — allows crawling of public pages.
3. `sitemap.xml` — lists key public pages.
4. `affiliate-disclosure.html` — clear affiliate disclosure.
5. `responsible-play.html` or similar — safer-play and risk reminder page.
6. `privacy-policy.html` — privacy basics before analytics, email, ads, or tracking.
7. `terms.html` — plain site terms.
8. `contact.html` — affiliate and visitor contact path.
9. `reviews.html` — review hub.
10. `how-we-review.html` — explains review standards.
11. Beginner guide pages for free slots, social casinos, bonuses, and review terms.

## Public Review Standard

Affiliate managers should be able to visit `https://slotsfreeusa.com` and quickly see:

1. The site is active and public.
2. The domain is secure.
3. The audience is adults 21+.
4. The site does not operate gambling.
5. The site does not accept bets or deposits.
6. The site uses FTC-style affiliate disclosure language.
7. The site avoids fake winnings claims.
8. The site has a review process.
9. The site has contact information.
10. The site has enough useful content to show real intent.

## Google Crawl Standard

The site should be built so Google can understand it.

Required basics:

1. One clear `<title>` per page.
2. One clear meta description per page.
3. Canonical URL on every important page.
4. Simple HTML links between major pages.
5. No important content hidden behind scripts.
6. Mobile-first layout.
7. Clean headings: one H1, useful H2 sections.
8. Descriptive internal links.
9. Updated sitemap after new public pages are added.
10. No accidental `noindex` on public pages.

## Speed Standard

Keep SlotsFreeUSA simple.

Allowed:

- static HTML
- CSS
- small JavaScript
- compressed images
- plain internal links
- lightweight demo-game embeds only if they do not slow the homepage

Avoid:

- heavy frameworks unless already used
- autoplay video
- large uncompressed images
- excessive third-party scripts
- popups before trust is built
- live tracking scripts before privacy setup
- live ad scripts before approval

## Affiliate Readiness Standard

Before applying to or re-contacting affiliate programs, the site should show:

1. Homepage with clear value proposition.
2. Review hub.
3. How We Review page.
4. Affiliate disclosure.
5. Responsible play page.
6. Contact page.
7. At least 5 helpful public content pages.
8. No broken navigation.
9. No placeholder text on public pages.
10. No unsupported claims about legal availability.

## Safe Monetization Order

Use this order:

1. Build trust pages.
2. Build beginner content.
3. Build review templates.
4. Apply to affiliate programs.
5. Add approved affiliate links only after approval.
6. Add disclosures near affiliate calls-to-action.
7. Add analytics only after privacy setup.
8. Add ads only after ad network approval.
9. Add email capture only after consent and email-provider setup.

## Content Language Standard

Use simple language for visitors.

Good:

- "Play free first."
- "Read the bonus terms."
- "This site is for adults 21+."
- "We may earn a commission if you use approved partner links."
- "We do not operate casino games or accept deposits."

Avoid:

- "guaranteed wins"
- "risk-free gambling"
- "available in every state"
- "best payout"
- "easy money"
- "beat the casino"

## Codex Handoff For Website Repo

When working in `Wholelychit/slotsfreeusa.com`, Codex should:

1. Keep the current stack.
2. Keep the website static and fast.
3. Update files directly instead of asking Gerry to paste code.
4. Add or update `robots.txt` and `sitemap.xml`.
5. Add missing trust pages.
6. Add internal links between guide pages and review pages.
7. Avoid live ads, live tracking, payment setup, private keys, or unsupported legal claims.
8. Commit each safe improvement with a clear message.

## Current Priority

Build the site so a stranger, Google crawler, or affiliate manager can understand it without asking Gerry or ChatGPT for context.
