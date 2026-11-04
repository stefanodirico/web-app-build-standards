# Legal and compliance (UK, EU, Spain)

Labels: **[Saved]** from Stefano's saved reels and files; **[Researched]** checked against sources on 3 November 2026; **[Practice]** good practice, not a legal rule; **⚠️** weaker source, background knowledge or likely to change, so verify before relying on it.

This is a working checklist, not legal advice. Have a solicitor check anything high-risk, particularly payments, health data, children's data or user-generated content. Ask before making legal claims about a specific project.

## Start here: which rules apply?

Answer these before building:

- Who is the legal operator, and where is it established?
- Does the site or app target people in the UK, the EU or both?
- Does it collect personal data, including through forms, analytics or embeds?
- Does it sell anything to consumers? Is it a one-off purchase or a subscription?
- Could under-18s use it?
- Can users post content or talk to each other?
- Does it use an AI chatbot or publish AI-generated content?
- Does it handle health or other special category data?

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

## EU rules [Researched]

### Cookies and data protection
- [ ] Apply the GDPR and the national ePrivacy rules. A UK company targeting EU users may still be caught. ⚠️ Confirm for the specific project.
- [ ] Do not build to the proposed Digital Omnibus cookie or GDPR changes. As of October 2026 the proposal was still at first reading. ⚠️ Recheck before launch.
- [ ] Consider whether an EU representative is needed under GDPR Article 27 if there is no EU establishment. ⚠️ Background knowledge.

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
- [ ] Check Spanish consumer law for any sales, including the withdrawal function. ⚠️ Not fully verified here.
- [ ] Add other countries only after checking their local rules.
