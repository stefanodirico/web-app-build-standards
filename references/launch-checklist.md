# Launch checklist

Run before any site or app goes live, and again after big changes. Mark each item passed, failed, N/A or UNSURE, with evidence. Labels: [Saved] from saved reels; ⚠️ verify before relying on it.

## Pre-launch checklist [Saved]

From the @yatesvids and @buildwithfrancis reels.

### Legal pages and business details
- [ ] Privacy policy page
- [ ] Terms and conditions page
- [ ] Cookies policy
- [ ] Refund policy, where something is sold
- [ ] Real business details
- [ ] Local laws checked (see [legal-and-compliance.md](legal-and-compliance.md))

### Consent and data
- [ ] Cookie consent checked
- [ ] Form consent checked
- [ ] Only necessary data collected
- [ ] Tracking checked
- [ ] Third-party embeds checked

### Content and claims
- [ ] Image copyright checked
- [ ] Fake reviews removed
- [ ] Unsupported claims removed
- [ ] Button labels are clear

### Accessibility
- [ ] Colour contrast checked
- [ ] Alt text on images
- [ ] Forms work by keyboard
- [ ] Accessibility issues fixed
- [ ] H1 and heading structure correct ⚠️ label partly obscured in the source reel

Standard to pick, from a saved screenshot: WCAG AA (the default), WCAG AA plus colour-blind-safe charts, or WCAG AAA contrast for body text (7:1 instead of 4.5:1). Build to WCAG 2.2 AA unless the project says otherwise.

### Search and sharing
- [ ] No vercel.app or preview domain
- [ ] Specific page titles
- [ ] Meta descriptions
- [ ] Custom favicon
- [ ] Open Graph image
- [ ] Canonical URLs
- [ ] Social previews work
- [ ] sitemap.xml

### Design and user experience
- [ ] Custom 404 page
- [ ] Designed loading states ⚠️ label partly obscured in the source reel
- [ ] Useful error messages ⚠️ label partly obscured in the source reel
- [ ] Mobile layouts work
- [ ] Consistent UI spacing
- [ ] No dead buttons or links

### Code and performance
- [ ] No console errors
- [ ] No leftover console.logs
- [ ] No exposed source maps
- [ ] No massive JS bundles

## The six legal holes [Saved]

From the "How to protect your vibe coded app from getting sued" guide and the @dr.erinjacques and @securedbycasco reels. Run the full audit prompt in [compliance-audit-prompts.md](compliance-audit-prompts.md) before every launch, not just the first.

- [ ] Fonts load from your own app, not Google or another font CDN
- [ ] Session replay masks every input and loads only after consent
- [ ] Consent banner has Accept and Reject buttons that are equally easy to click
- [ ] Sign-up has a neutral age screen if children could use it, with the minimum age set to 13 (UK or US only), 14 (Spain only) or 16 (several EU countries); anyone younger is blocked without storing their data; Children's Code applied for under-18s (UK)
- [ ] Marketing email has recorded opt-in consent (unticked box), or the soft opt-in for existing customers
- [ ] Every marketing email has a postal address and a working unsubscribe link; unsubscribes honoured within 10 business days
- [ ] Checkout shows price, frequency, auto-renewal and how to cancel next to the pay button
- [ ] Users can cancel online as easily as they signed up; consent records saved for every subscriber
- [ ] If users upload content: DMCA agent registered ($6, renew every three years), copyright page live, Report button on every piece of user content
- [ ] Privacy policy and terms linked in the footer and at sign-up
- [ ] User B can't open user A's record by URL, and a logged-out URL no longer loads (see [security.md](security.md))

## Vibe-coded giveaways to avoid and fix [Saved]

From a screenshot of a reel, "20 (hidden) vibecoded website giveaways" (creator not visible). Avoid these while building, and fix any you find on an existing site. The giveaway names are as shown on screen, and the fixes are [Practice]. ⚠️ Items 4, 13, 16 and 20 were cut off or unclear in the screenshot, so the wording in brackets or the fix is a best reading.

| # | Giveaway | Fix |
|---|---|---|
| 1 | vercel.app url | Move to a real domain (see domain setup below) |
| 2 | viewsource empty | Pre-render or server-render the main content so it is in the page's HTML |
| 3 | no 404 page | Add a custom 404 page with a route home, and return a real 404 status |
| 4 | vite + react browser [tab title] | Replace the template's default tab title and favicon ⚠️ |
| 5 | same page titles | Give each page its own specific title |
| 6 | no meta desc | Write a meta description for each page |
| 7 | no og:image | Add an Open Graph image and check the social preview |
| 8 | no structured data | Add JSON-LD where it fits, and make it match what the page shows |
| 9 | multiple H1's | Use one H1 per page |
| 10 | no H1's | Add one H1 that says what the page is |
| 11 | no canonical tag | Add a canonical URL to each page, using the real domain |
| 12 | no llms.txt | Optional: add one if you want a summary for AI tools. ⚠️ It is a proposed convention, not an agreed standard, and its benefit is unproven as far as I know |
| 13 | AI blocked robots.t[xt] | Check `robots.txt` and any host or CDN bot settings, then allow or block AI crawlers on purpose ⚠️ |
| 14 | no favicon | Add a custom favicon |
| 15 | no sitemap.xml | Publish one and submit it in Google Search Console |
| 16 | no lang attribut[e] | Set the page language, such as `<html lang="en-GB">` ⚠️ |
| 17 | missing alt text | Add alt text to meaningful images, and empty alt text to decorative ones |
| 18 | source maps | Don't expose production source maps publicly |
| 19 | console errors | Fix them, and check the console on every main page |
| 20 | massive JS bundl[e] | Split code by route and remove unused dependencies. The screenshot shows no target size ⚠️ |

## Staging and preview environments [Saved]

From the @paigethepm reel. If a vibe-coded app keeps breaking, ask whether you are "testing in prod": pushing code live to everyone and testing it there.

- **Staging:** a production-like environment, separate from production, for testing new features and bug fixes.
- **Setting it up:** this depends on your tools. You usually want a staging branch in GitHub and a staging environment at your hosting provider, such as Vercel, Bolt, Lovable or Cloudflare Workers. ⚠️ The reel gives no steps, so check each tool's current documentation.
- **Quicker option when you're small:** preview branches. The reel names Vercel as doing this well: they show what a deployment will look like before it goes to production.

Add when setting it up [Practice]:
- [ ] Test new features and bug fixes on staging or a preview before production.
- [ ] Give staging its own database and keys. A preview connected to the production database is not a safe test.
- [ ] Never use real personal data for testing (see [security.md](security.md)).
- [ ] Restrict access to staging and preview URLs and keep them out of search engines. ⚠️ Settings vary by host.
- [ ] Treat preview URLs as test addresses only. The live site still needs a real domain.

## Domain setup [Saved]

From the @danielwelsh_routiq reel ("You bought the domain. Now what?"). About 10 minutes in total.

1. **Split the site and the app with subdomains.** `www.` for the marketing site and `app.` for the product, each one CNAME record (about a minute to add). Do it now: moving the app later breaks every link anyone has shared.
2. **Send email from two subdomains, never the root domain.** `mail.` for operations mail (sign-up verification, receipts, booking confirmations, password resets, "no-reply") and `news.` for marketing mail (campaigns, newsletters). If marketing mail gets flagged as spam, only `news.` suffers: resets from `mail.` still arrive and the main address on the root domain is untouched.
3. **Publish sitemap.xml and submit it in Google Search Console.** This is how search engines find every page.

Add for each sending subdomain [Practice]: SPF, DKIM and DMARC records from the email provider, and a working unsubscribe link on marketing mail.

## Final sign-off

- [ ] Every applicable item has been checked, with evidence where possible.
- [ ] Legal pages match what the site or app actually does.
- [ ] A real browser check confirms no non-essential tracker fires before consent.
- [ ] Automated accessibility scan and manual keyboard and screen reader test completed. Automated tools alone are not enough.
- [ ] The latest changes were tested on staging or a preview before going live.
- [ ] Every vibe-coded giveaway has been fixed, marked N/A or kept on purpose, with the reason noted.
- [ ] All ⚠️ items relevant to this project have been verified.
- [ ] Any remaining gaps have been reported plainly.
