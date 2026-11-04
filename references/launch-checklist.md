# Launch checklist

Run before any site or app goes live, and again after big changes. Mark each item passed, failed, N/A or UNSURE, with evidence. Labels: [Saved] from Stefano's saved reels; ⚠️ verify before relying on it.

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

Standard to pick, from a screenshot Stefano saved: WCAG AA (the default), WCAG AA plus colour-blind-safe charts, or WCAG AAA contrast for body text (7:1 instead of 4.5:1). Build to WCAG 2.2 AA unless the project says otherwise.

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
- [ ] All ⚠️ items relevant to this project have been verified.
- [ ] Any remaining gaps have been reported plainly.
