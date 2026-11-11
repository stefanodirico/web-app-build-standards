# Compliance audit prompts

Copy-paste prompts for an AI coding tool that can read the whole project (Claude Code, Codex, Cursor, Gemini CLI). Adapted from the "How to protect your vibe coded app from getting sued" guide [Saved], widened to cover UK and EU rules. The rules behind each prompt, with sources and caveats, are in [legal-and-compliance.md](legal-and-compliance.md). This is a working checklist, not legal advice.

You'll need: the code open in the tool, access to the email provider, Stripe and analytics dashboards, and about two hours. Most fixes take 5 to 15 minutes. If users can upload files, budget $6 (about €5 ⚠️ approximate conversion) for the DMCA agent registration.

## 1. Full audit (run first, changes nothing)

```text
Audit this codebase for common legal compliance risks. Do not change any code. Read the whole project and, for each item below, report FOUND, NOT FOUND or UNSURE, the exact files and line numbers, and a one-sentence fix.

1. Fonts: anything loaded from fonts.googleapis.com, fonts.gstatic.com or another third-party font or asset CDN, including CSS @import, <link> tags, packages and themes.
2. Third-party tracking: every analytics, session replay, heatmap or chat widget script (for example Hotjar, FullStory, LogRocket, Microsoft Clarity, PostHog, Mixpanel, Google Analytics, Intercom). For each, say whether it can record keystrokes or form inputs, and whether it loads before consent.
3. Consent: is there a consent banner, are Accept and Reject equally easy, and do non-essential scripts, cookies, pixels and local storage actually wait for consent?
4. Age: does sign-up ask for age or date of birth? Is any part of the app or its marketing aimed at children?
5. Email: every place the app sends marketing or newsletter email. Does each template include a postal address, a working unsubscribe link and List-Unsubscribe headers? Does the send code skip unsubscribed people?
6. Subscriptions: every checkout or pricing page with a recurring charge or a trial that converts to paid. Are the price, frequency, renewal terms, first charge date and how to cancel shown next to the pay button? Can users cancel online? Is consent recorded?
7. User uploads: every place users can post files, images or text others can see. Is there a terms of service, a copyright takedown page and a Report button?
8. Legal pages and business details: is there a privacy policy, terms, cookies policy and, where relevant, refund policy and company details, linked from the footer and the sign-up form?
9. Access control: can one user open another user's record by changing an ID in a URL or request, and does logout invalidate the session on the server?

Finish with a table ranked from highest to lowest risk. Mark anything you can't judge from code as MANUAL, with how to check it.
```

Save the report and work through the fixes below one at a time.

## 2. Self-host fonts

```text
Find every font this project loads from Google Fonts or any other external font service. For each one:
1. Download the exact woff2 files for the weights and styles actually used.
2. Save them under /fonts in the public or static folder.
3. Replace the external <link> or @import with local @font-face rules using font-display: swap.
4. Remove every remaining reference to fonts.googleapis.com and fonts.gstatic.com.
If this is a Next.js project, use next/font/local instead.
Then search the whole project, including node_modules, CSS and config files, and confirm no external font domains remain. If a package or theme still loads them, tell me which one.
```

Check: open the live site, Network tab, reload, filter for "google". Nothing from either font domain should load.

## 3. Mask session replay and gate tracking on consent

```text
For every analytics, session replay or heatmap tool in this project:
1. Turn on input masking so no keystrokes or form values are ever recorded. Use the tool's own setting (for example maskAllInputs, data-hj-suppress, fs-mask) and mask every input, textarea and contenteditable element by default.
2. Exclude passwords, payment fields, email addresses and other personal data from recordings entirely.
3. Load the tool only after the user accepts in a consent banner. If there is no banner, add one with Accept and Reject buttons that are equally easy to use, and remember the choice.
4. Switch session replay off completely on sign-up, login, checkout and account settings pages.
Show me every change.
```

Check: in the tool's dashboard, confirm the project-level privacy setting matches, then record a test session and type a fake email to confirm it is masked.

## 4. Neutral age screen

```text
Add a neutral age screen to the sign-up flow:
1. Ask for date of birth with an empty date picker. Do not pre-fill it or say what age is required.
2. Use this minimum age: [13 for UK-only or US-only; 14 for Spain-only; 16 if the app serves several EU countries, or the UK and EU together, without per-country rules]. If the user is under it, do not create the account and do not store the date of birth, email or anything else they entered. Show a polite message that the app isn't available for their age.
3. Set a cookie or local storage flag so they can't immediately go back and enter a different date.
4. If they are old enough, continue sign-up and store only an "age verified" flag unless the app needs the full date.
Also list anything in the landing page, app store listing or marketing copy that could look aimed at children.
```

The defaults come from GDPR Article 8 and COPPA; see the minimum age section in [legal-and-compliance.md](legal-and-compliance.md). Below the minimum, the alternative to blocking is verified parental consent. If the app is meant for under-18s (including 14 to 18-year-olds), don't use this gate: design for the UK Children's Code and get legal review. A self-declared age may not be enough there.

## 5. Marketing email

```text
Audit every marketing, newsletter and announcement email this app sends. List transactional emails (password resets, receipts) separately but don't change them.
For each marketing template:
1. Add a footer with the business name and postal address: [ADDRESS].
2. Add a clear unsubscribe link that works without logging in.
3. Add List-Unsubscribe and List-Unsubscribe-Post: List-Unsubscribe=One-Click headers if the provider supports them.
4. Make sure the subject line isn't misleading and the from name is the real business name.
Then check that unsubscribing removes the person from every marketing list and that the send code skips them. Show me where that check happens.
Finally, check how addresses get onto marketing lists. Every sign-up, waitlist or checkout form that adds someone to marketing must have an unticked opt-in box (or, for existing customers only, a clear opt-out at the point of collection), and the database must store when and how each person agreed. List any form that adds people to marketing without this.
```

UK and EU rules need consent before the first marketing email, not just an unsubscribe link afterwards; Spain accepts no tacit consent at all. See the marketing email sections in [legal-and-compliance.md](legal-and-compliance.md).

Check: send the launch email to yourself first and click unsubscribe.

## 6. Subscription checkout

```text
Audit every checkout and pricing page that sells a recurring subscription or a free trial that converts to paid.
1. Next to the purchase button, show in plain text: the price, how often it is charged, that it renews automatically until cancelled, when the first charge happens (including when a trial ends), and exactly how to cancel.
2. If we use Stripe Checkout, add this with custom_text near the submit button, and set consent_collection for terms of service so the user must tick a box before paying.
3. Add online cancellation as easy as signing up. With Stripe, turn on the customer portal with cancellation enabled and link to it from the account page.
4. Send a confirmation email after purchase repeating the terms and how to cancel.
5. Store a consent record for each user (timestamp, terms shown, plan) in the database.
Show me the checkout page before and after.
```

Check: could a stranger tell in five seconds what they pay, how often, and how to stop? If Stripe won't show the custom text in your Checkout mode, put the terms on your own pricing page directly above the button that sends people to Stripe.

## 7. User uploads

```text
Set up user content protection:
1. Create a /copyright page explaining how to send a copyright takedown notice, with our designated agent's name, address and email: [AGENT DETAILS FROM THE COPYRIGHT OFFICE REGISTRATION]. List what a valid DMCA notice must include.
2. Add a Report button on every piece of user-uploaded content that sends the report to an admin queue.
3. Add an admin action to remove reported content and track strikes per user. After 3 valid copyright strikes, suspend the account. Write this repeat infringer policy into the terms of service.
4. Under every upload form, add: "Only upload content you own or have permission to share. See our Terms and Copyright Policy."
5. Link the Terms of Service and Copyright Policy in the footer.
```

Register the agent at copyright.gov first ($6, renew every three years). For image uploads, also plan for CSAM detection and reporting, and in the UK check the Online Safety Act.

## 8. Privacy policy and terms from the real code

```text
Read this whole codebase and list every piece of personal data the app collects (including what third-party tools such as analytics, Stripe and the email provider collect), where it is stored, and who it is shared with. Then draft a plain-English privacy policy and terms of service based on what the app actually does, not a generic template. Cover UK GDPR and, where relevant, EU GDPR and California rules. Mark every point a lawyer should review with [LAWYER REVIEW]. Add both pages and link them in the footer and next to the sign-up button.
```

An AI draft based on the real code beats a copied template, but it is still a draft: have a lawyer check it before you scale.

## 9. Access control and logout

```text
Check access control and logout. Do not change code yet.
1. List every route or endpoint that takes a record ID (in the URL, query or body). For each, show where the server checks that the signed-in user is allowed to see or change that record. Flag any that only rely on the ID being hard to guess.
2. Show what logout does. Confirm it clears the session token, auth cookies, localStorage and sessionStorage, and invalidates the token on the server.
Report as a table with file:line and a one-sentence fix, then stop.
```

Check by hand: open user A's record URL as user B, and paste a private URL after logging out. Neither should load.

## When things go wrong

- **The AI says the fonts are fixed but Google still loads.** A package or theme is pulling them in. Ask it to search node_modules and every CSS and config file for googleapis and gstatic and name the package.
- **Replay still shows typed text.** The dashboard setting overrides the code. Change it there and test again with a fake email.
- **You get a legal letter or demand.** Don't ignore it and don't reply yourself. Send it to a lawyer and fix the issue it describes straight away.
