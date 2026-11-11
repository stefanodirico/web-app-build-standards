# Legal and compliance (UK, EU, Spain, US)

Labels: **[Saved]** from Stefano's saved reels and files; **[Researched]** checked against sources on 3 November 2026 (US section: 10 November 2026; marketing email and minimum age: 11 November 2026); **[Practice]** good practice, not a legal rule; **⚠️** weaker source, background knowledge or likely to change, so verify before relying on it.

This is a working checklist, not legal advice. Have a solicitor check anything high-risk, particularly payments, health data, children's data or user-generated content. Ask before making legal claims about a specific project.

## Start here: which rules apply?

Answer these before building:

- Who is the legal operator, and where is it established?
- Does the site or app target people in the UK, the EU, the US, or a mix?
- Does it collect personal data, including through forms, analytics or embeds?
- Does it sell anything to consumers? Is it a one-off purchase or a subscription?
- Could under-18s use it?
- Can users post content or talk to each other?
- Does it use an AI chatbot or publish AI-generated content?
- Does it handle health or other special category data?
- Does it send marketing email, sell a subscription, or let users upload content others can see?

For a quick scan of an existing codebase, run the full audit prompt in [compliance-audit-prompts.md](compliance-audit-prompts.md).

## UK rules [Researched]

### Company details
- [ ] A UK limited company shows on its website its registered name, registered number, part of the UK where it is registered, and registered office address. The rules sit in the Company, Limited Liability Partnership and Business (Names and Trading Disclosures) Regulations 2015.
- [ ] If VAT registered, show the VAT number. ⚠️ Based on a law firm note, so confirm with the accountant.
- [ ] Copy the details exactly from the Companies House register.

### Cookies and tracking (PECR)
- [ ] Audit more than cookies. The ICO's April 2026 guidance also covers tracking pixels, link decoration, local storage, fingerprinting, scripts and tags.
- [ ] Get consent before setting anything non-essential, unless a specific exception applies.
- [ ] Newer exceptions, in force since 5 February 2026, can cover limited statistical analytics and remembering appearance preferences such as language or dark mode.
- [ ] To rely on the statistical exception, tell users clearly and give them a simple, free way to object. Any provider must act only on your behalf and not use the data for its own purposes.
- [ ] Assume default Google Analytics needs consent. ⚠️ Based on vendor commentary, so check the current ICO text and configuration.
- [ ] Advertising trackers need consent. The ICO has looked at relaxing enforcement for low-risk advertising, but do not assume that applies. ⚠️ This area may change.
- [ ] Session replay and heatmap tools (Hotjar, FullStory, LogRocket, Microsoft Clarity and similar) are non-essential: load them only after consent, mask every input by default, and switch replay off on sign-up, login, checkout and account pages. [Saved] [Practice]
- [ ] Fines under PECR now align with UK GDPR levels, up from the old £500,000 cap (about €575,000 ⚠️ approximate conversion).

### Data protection (UK GDPR and Data Protection Act 2018)
- [ ] Give a clear privacy notice covering who you are, what you collect, why, your lawful basis, who receives it, retention, transfers and user rights. ⚠️ Background knowledge.
- [ ] Add a data processing agreement with each supplier that handles personal data for you. ⚠️ Background knowledge.
- [ ] Check whether the ICO data protection fee is due. ⚠️ Not verified in this research.

### Accessibility (Equality Act 2010)
- [ ] Treat accessibility as a legal duty. Service providers must make reasonable adjustments and anticipate disabled people's needs.
- [ ] Do not describe WCAG as a law for private companies. The Act names no technical standard, but WCAG AA is the usual benchmark in practice.
- [ ] Build to WCAG 2.2 AA. This also covers the WCAG 2.1 AA level used in the EU.

### Consumer law (DMCC Act 2024)
- [ ] Do not write, commission or publish fake reviews or concealed incentivised reviews. This applies to businesses of all sizes.
- [ ] Do not publish genuine reviews in a misleading way, such as hiding negative ones without saying so.
- [ ] Remove misleading claims, pressure tactics and hidden compulsory fees. The CMA can fine directly, up to 10% of global turnover.
- [ ] If selling at a distance, check pre-contract information and the 14-day cancellation rules. ⚠️ Confirm how they apply to the specific product.
- [ ] If selling subscriptions, check the new DMCC regime. ⚠️ One law firm says it is expected in January 2027, so verify the date and final rules.

### Children and user-generated content
- [ ] If under-18s are likely to use the service, apply the ICO Children's Code and its 15 standards, and carry out a data protection impact assessment.
- [ ] A tick-box asking users to state their age may not be enough. The ICO has criticised this on services with user interaction and user-generated content.
- [ ] If users can post or interact, check the Online Safety Act 2023 and Ofcom's guidance.

### Marketing email and texts (PECR regulation 22) [Researched]
- [ ] To individuals (including sole traders and partnerships), marketing email or texts need prior consent, unless the soft opt-in applies.
- [ ] Soft opt-in: you got the details directly from the person in the course of a sale or negotiations for a sale, you only market your own similar products or services, and you gave a simple way to refuse when you collected the details and in every message since.
- [ ] Put a prominent opt-out or an unticked opt-in box on the form itself. The ICO says an opt-out hidden in the privacy policy isn't enough.
- [ ] For waitlists and newsletter sign-ups, get explicit consent with an unticked box and keep a record of it. ⚠️ Whether a waitlist sign-up counts as "negotiations for a sale" for the soft opt-in is untested; don't rely on it. [Practice]
- [ ] Every message must say who it is from and give a valid address or link to opt out, free of charge. Act on opt-outs promptly.
- [ ] Emails to company addresses (limited companies, LLPs) don't need PECR consent, but you must still identify yourself and offer an opt-out, and UK GDPR still applies to named people's addresses.
- [ ] Since 5 February 2026 there is also a charitable purposes soft opt-in, for registered charities only.
- [ ] PECR fines are now up to £17.5 million (about €20 million ⚠️ approximate conversion) or 4% of global turnover.

## EU rules [Researched]

### Cookies and data protection
- [ ] Apply the GDPR and the national ePrivacy rules. A UK company targeting EU users may still be caught. ⚠️ Confirm for the specific project.
- [ ] Do not build to the proposed Digital Omnibus cookie or GDPR changes. As of October 2026 the proposal was still at first reading. ⚠️ Recheck before launch.
- [ ] Consider whether an EU representative is needed under GDPR Article 27 if there is no EU establishment. ⚠️ Background knowledge.

### Marketing email (ePrivacy Directive Article 13)
- [ ] Same shape as the UK: prior consent for marketing email to individuals, with a soft opt-in for existing customers about similar products, and an opt-out at collection and in every message. ⚠️ Background knowledge; rules for business addresses vary by country, so check each market.
- [ ] Spain is stricter: see the Spain section below.

### Minimum age and parental consent (GDPR Article 8) [Researched]
- [ ] If you rely on consent to process a child's data for an online service offered directly to children, a child below the national "digital age of consent" needs a parent's consent, and you must make reasonable efforts to verify it.
- [ ] The default is 16. Countries can lower it to 13. Thresholds found in November 2026: UK 13; Spain, Italy, Austria 14; France, Greece, Czech Republic 15; Germany, Ireland, Netherlands 16; Belgium, Denmark, Sweden, Finland, Portugal 13. ⚠️ Sources disagree on a few countries, and Spain has a draft law to raise its age to 16, so recheck before launch.
- [ ] Default for the sign-up age screen in Stefano's projects:
  - UK only: 13.
  - Spain only: 14.
  - Several EU countries, or UK and EU together, with no per-country logic: 16. It is the highest threshold, so it is valid everywhere.
  - Below the threshold, either block sign-up or collect verified parental consent. Don't just tick a box.
- [ ] Article 8 is a consent rule, not a ban: if the lawful basis is something else (such as contract), the threshold works differently. ⚠️ Get advice before relying on that.
- [ ] Separately, the UK Children's Code and the Online Safety Act protect everyone under 18. Passing the age screen doesn't switch them off. If the app is built for under-18s, skip the age gate and design for the Children's Code, with legal review.

### Third-party fonts [Saved]
- [ ] Self-host every font. Loading from fonts.googleapis.com or fonts.gstatic.com sends each visitor's IP address to Google before they have agreed to anything. Vibe-coded apps do this by default.
- [ ] The case: in January 2022 the Munich Regional Court (LG München I) found this breached the GDPR and awarded the visitor €100 in damages. It set off a wave of demand letters in Germany.
- [ ] ⚠️ One saved reel quotes "fines up to €250,000 per violation". That figure was the penalty the court threatened if the site kept doing it after the ruling, not a fine per visitor. Don't repeat it as a GDPR fine.
- [ ] The same reasoning applies under UK GDPR, since an IP address is personal data. ⚠️ No UK ruling on this found; treat it as a risk, not settled law.
- [ ] Check other third-party CDNs too (icon fonts, Adobe Fonts, script CDNs), and packages or themes that pull fonts in without an obvious link tag.
- [ ] Verify in the browser: Network tab, reload, filter for "google". Nothing from either font domain should appear. Prompt in [compliance-audit-prompts.md](compliance-audit-prompts.md).

### Accessibility (European Accessibility Act)
- [ ] Check whether the service is covered. The Act has applied since 28 June 2025 and covers e-commerce services sold to EU consumers, including from outside the EU.
- [ ] Use WCAG 2.1 AA, through EN 301 549, as the working standard. ⚠️ EAA-specific harmonised standards were reported as still being finalised, and native apps have extra requirements.
- [ ] Check the microenterprise exemption for services. ⚠️ From background knowledge, it covers fewer than 10 staff and no more than €2m in annual turnover or balance sheet total. It does not cover products. Build accessibly anyway, because UK duties still apply.
- [ ] If in scope, publish the required accessibility information. ⚠️ Confirm the format under national law.

### Consumer sales
- [ ] If consumers can buy online and have a withdrawal right, provide an online withdrawal function. This has applied since 19 June 2026 with no small business exemption.
- [ ] Make it clearly labelled and easy to find, send an automatic confirmation, and record the date and time.
- [ ] Update the privacy notice for data collected through that function.
- [ ] Do not offer email or phone as the only route. Check national implementation. ⚠️ Timing and details vary by country.

### AI (EU AI Act, Article 50)
- [ ] Article 50 transparency duties have applied since 2 August 2026. Tell users when they are talking to an AI system, unless it is obvious. ⚠️ Check the exact scope and exceptions.
- [ ] Check whether AI-generated content needs labelling or machine-readable marking. Providers of systems already on the market before 2 August 2026 have until 2 December 2026 for marking. ⚠️ Check whether you count as a provider or deployer.

### Online platforms
- [ ] If the service hosts user content or is a marketplace, check the Digital Services Act. ⚠️ Not fully verified here, including reliefs for small businesses.

## Spain (if targeting Spanish users)

- [ ] Follow Article 22.2 of the LSSI (Ley 34/2002) on cookies and the AEPD's cookie guide. Provide clear information and get valid consent before non-exempt cookies are used.
- [ ] Block non-exempt cookies until consent. ⚠️ Based on a practitioner source, so check the current AEPD guide.
- [ ] Check the aviso legal details required by Article 10 of the LSSI. ⚠️ Not fully verified here.
- [ ] Marketing email (LSSI Article 21) [Researched]: prohibited unless the person asked for it or expressly agreed beforehand. Tacit consent isn't accepted. The AEPD applies this to companies' addresses as well as individuals'.
- [ ] The only exception: an existing contract with the person, marketing your own products or services similar to what they bought.
- [ ] Offer a simple, free opt-out when collecting the address and in every email. The email must include an email address or other valid electronic address for opting out.
- [ ] The AEPD fines this regularly, from a few thousand euros for continuing after an unsubscribe to €20,000 for sending without consent.
- [ ] Minimum age for consent: 14 (Organic Law 3/2018, Article 7). See the EU minimum age section above.
- [ ] Check Spanish consumer law for any sales, including the withdrawal function. ⚠️ Not fully verified here.
- [ ] Add other countries only after checking their local rules.

## US (if targeting US users) [Saved]

From the "How to protect your vibe coded app from getting sued" guide (the six legal holes). Figures and dates checked on 10 November 2026; see [sources.md](sources.md). US rules can reach a UK or EU operator whose app is used by people in the US. Copy-paste fix prompts are in [compliance-audit-prompts.md](compliance-audit-prompts.md).

### Session replay and wiretapping (California, CIPA)
- [ ] Plaintiffs sue under the California Invasion of Privacy Act, arguing a third-party tool recording what visitors type is like tapping a phone call. Statutory damages are $5,000 (about €4,300 ⚠️ approximate conversion) per violation.
- [ ] SB 690, signed on 30 September 2026, ends private lawsuits over pen-register and trap-and-trace claims (the tracking pixel theory) for websites and apps. It does not touch the wiretapping (§631) and eavesdropping (§632) sections that session replay claims rely on. [Researched] ⚠️ One source says it takes effect on 1 January 2027.
- [ ] Fix: mask every input in replay tools, exclude passwords, payment fields and personal data, and load trackers only after consent. Check the tool's dashboard too: a project-level setting can override the code.

### Children under 13 (COPPA)
- [ ] COPPA applies if the app is aimed at children, or you actually know a user is under 13. Then you need verified parental consent before collecting their data.
- [ ] Civil penalties reach $53,088 (about €46,000 ⚠️ approximate conversion) per violation. [Researched] ⚠️ The FTC made no inflation adjustment for 2026, according to a secondary source; check 16 CFR 1.98.
- [ ] The amended COPPA Rule had a compliance date of 22 April 2026.
- [ ] For a general-audience app, use a neutral age screen: an empty date of birth field that doesn't hint at the required age (not an "I am over 13" tick-box). If under 13, don't create the account, store nothing they entered, and set a flag so they can't immediately retry with a different date. If 13 or over, store an "age verified" flag rather than the full date unless the app needs it.
- [ ] Check landing pages, app store listings and marketing for anything aimed at children.
- [ ] If the app is meant for children, stop and get a lawyer. Note the UK Children's Code covers under-18s, a much wider group than COPPA.

### Marketing email (CAN-SPAM, plus Gmail and Yahoo rules)
- [ ] Covers launch emails, newsletters and promotions, even to people who joined your waitlist. Each non-compliant email can be a separate violation, up to $53,088.
- [ ] Every marketing email needs a real postal address (a registered PO box or mailbox service counts), a clear unsubscribe link that works without logging in, a truthful subject line and a real from name.
- [ ] Honour unsubscribes within 10 business days, across every marketing list, and make the send code skip them.
- [ ] Since 2024, bulk senders (more than 5,000 a day to Gmail) need one-click unsubscribe headers: `List-Unsubscribe` and `List-Unsubscribe-Post: List-Unsubscribe=One-Click`. Most providers (Resend, Loops, ConvertKit, Mailchimp) handle this once turned on.
- [ ] Send the launch email to yourself first and test the unsubscribe link.
- [ ] Transactional email (receipts, password resets) is treated differently; list it, but don't add marketing footers to it.

### Subscriptions and auto-renewal (ROSCA, California ARL)
- [ ] Federal ROSCA: show all material terms before taking card details, get clear consent, and give a simple way to cancel. The FTC is actively enforcing it.
- [ ] California's amended Automatic Renewal Law, in force since 1 July 2025: express affirmative consent to the auto-renewal terms; keep proof for three years or one year after the contract ends, whichever is longer; send an annual reminder; give 7 to 30 days' notice of a price increase. [Researched]
- [ ] Next to the pay button, show the price, how often it is charged, that it renews until cancelled, when the first charge happens (including when a trial ends), and how to cancel.
- [ ] Offer online cancellation as easy as signing up (for Stripe, the customer portal with cancellation on), send a confirmation email repeating the terms, and store a consent record (timestamp, terms shown, plan).
- [ ] The five-second test: could a stranger tell what they pay, how often, and how to stop?
- [ ] ⚠️ The FTC's 2024 "click to cancel" rule was struck down by a federal appeals court in July 2025 (background knowledge, not rechecked); ROSCA and state laws still apply.

### User uploads (DMCA safe harbour, CSAM reporting)
- [ ] If users can upload content others can see, the DMCA safe harbour only protects you if it is set up properly. A disclaimer alone isn't enough.
- [ ] Register a designated agent with the US Copyright Office: $6 (about €5 ⚠️ approximate conversion), valid for three years, so diary the renewal. [Researched] The agent can be you, a role such as "Legal Team", or a service. ⚠️ The guide says a PO box works for the address; one law firm says the service provider's own address must be a physical street address, so check the form.
- [ ] Publish a /copyright page with the agent's details and what a valid notice must include, add a Report button on every piece of user content, and write a repeat infringer policy into the terms (for example, suspension after three valid strikes).
- [ ] Put a line under upload forms: only upload content you own or have permission to share.
- [ ] US law requires platforms to report child sexual abuse material to NCMEC when they become aware of it. For image-heavy apps, look at a scanning service (Cloudflare's CSAM Scanning Tool is free for Cloudflare users) and get legal advice on the reporting process. In the UK, also check the Online Safety Act duties above.

### Privacy policy (CalOPPA)
- [ ] California's online privacy law requires a privacy policy if you collect personal information from California residents, which in practice means any app with a sign-up form.
- [ ] Draft it from what the code actually collects and shares, not a template, and mark points for lawyer review.
