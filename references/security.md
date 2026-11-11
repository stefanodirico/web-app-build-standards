# Security

Labels: [Saved] from Stefano's saved reels and links; [Researched] checked against sources on 3 November 2026; [Practice] good practice; ⚠️ verify before relying on it. This is a working checklist, not a security audit.

## Five one-minute checks [Saved]

From Lincoln Devine's guide ([lincolndevine.com/guides/secure](https://lincolndevine.com/guides/secure/)). AI coding agents often take shortcuts that make an app work but leave it open; the app runs and tests pass, so nothing looks wrong.

1. **Database access:** in Supabase, is row-level security off on any table? If so, anyone with the public key may read it.
2. **Firebase rules:** are they still in permissive test mode?
3. **Secret keys:** search the source for service-role and secret keys. Server keys must never reach the browser. If one leaked, rotate it and scan the git history.
4. **Server-side authorisation:** log out and call the data endpoints in a browser. If data still loads, the check lives only in the interface.
5. **Storage buckets:** are uploaded files public, especially with guessable file names?

Dashboard settings (RLS toggles, Firebase rules in the console, bucket visibility) can't be seen by an agent reading code. Ask the user to check them, or use the provider's CLI if it is connected. Report findings ranked by blast radius: what an attacker could reach, and how many users it affects.

## Two hands-on tests: shared URLs and logout [Saved]

From a @securedbycasco reel, where the engineer answers a viral "why you shouldn't trust vibe-coded apps" video.

1. **Insecure direct object reference (IDOR).** Signed in as user A, copy the URL of one of their records (for example `app.com/mail/a8f3e1c9`). Sign in as user B in another browser and open it. If B sees A's data, the app exposes an object ID in the URL or request but never checks that the user is authorised to see it. Change the ID, reach someone else's data. This is OWASP "broken access control" (CWE-639). Fix it on the server or database, not by hiding the link.
2. **Logout.** Sign in, copy a private URL, log out, then paste the URL again. If it still loads, or the backend still accepts the old token, logout is cosmetic. A proper logout clears all four (the session token, auth and session cookies, localStorage and sessionStorage) and then invalidates the token on the server, so it can't be reused from any device.

## Hardening prompt, corrected [Saved]

From a @securedbycasco reel, where a security engineer reacts to a popular prompt. The original asked to "review this app and harden its security" with: rate limiting on all public endpoints (IP and user-based, sensible defaults, graceful 429s); strict input validation and sanitisation on all user inputs (schema-based, type checks, length limits, reject unexpected fields); and secure API key handling (remove hard-coded keys, move to environment variables, rotate keys, no keys client-side), following OWASP, with clear comments and without breaking existing functionality.

The engineer's corrections:
- Public endpoints often serve people who aren't signed in yet, so user-based rate limits do little there. Limit by IP and other signals too.
- Keeping keys in environment variables isn't enough. Any call that uses an API key belongs on your server, or better, uses short-lived credentials.
- Put the rules in the project's standing rules file (CLAUDE.md, AGENTS.md, GEMINI.md, Cursor rules), not only in one prompt.
- Write an access control matrix into that file. Most security problems in vibe-coded apps come from the agent not knowing the expected behaviour, not from bad code.

### Access control matrix template

Add to the project's CLAUDE.md or AGENTS.md and keep it current:

```markdown
## Access control
| Resource | Signed out | User | Owner of the record | Admin |
|---|---|---|---|---|
| Public pages | read | read | read | read |
| Profile | none | read own | read, edit, delete | read, suspend |
| Bookings | none | create | read, cancel own | read, cancel any |
Rules: enforce on the server or database, never only in the UI. Anything not listed is denied.
```

## Secrets, access and hardening [Researched and Practice]

### Secrets
- [ ] Never put secret keys in frontend code or the app bundle. Examples are AI API keys, Stripe secret keys, Supabase service-role keys, database credentials and private signing keys.
- [ ] Know the difference: Stripe publishable keys and Supabase anon keys are designed to be public, but their safety depends on correct permissions.
- [ ] Add `.env*` to `.gitignore` before committing.
- [ ] If a secret was committed, rotate it and clean the history. Deleting the latest commit is not enough.
- [ ] Check public environment variables, such as anything prefixed `NEXT_PUBLIC_`.
- [ ] Scan before launch, for example with `semgrep --config=p/secrets --config=p/owasp-top-ten .`

### Access control
- [ ] Enforce permissions on the server or database, never only in the browser.
- [ ] Turn on row-level security on every Supabase table holding user data, with policies limited to the correct user. In Firebase, set equivalent security rules.
- [ ] Test as a logged-out user and as a second user. Change an ID in a request and confirm you cannot see someone else's data.
- [ ] Check authentication on every API route.
- [ ] Logging out clears the session token, cookies, localStorage and sessionStorage, and invalidates the token server-side.

### Hardening [Practice]
- [ ] Validate all input on the server.
- [ ] Keep detailed errors in server logs and out of API responses.
- [ ] Set security headers, including Content-Security-Policy, HSTS and clickjacking protection.
- [ ] Do not use overly permissive CORS.
- [ ] Add rate limits to login, forms and costly AI endpoints.
- [ ] Set spending limits on paid APIs.
- [ ] Run dependency audits, such as `npm audit`, and review what an AI tool installed.
- [ ] Review the app against the OWASP Top 10. ⚠️ Check the latest edition directly.

### Working with AI coding tools [Practice]
- [ ] Read and test the code. Passing a demo does not make an app secure.
- [ ] Use version control, and commit before major AI changes.
- [ ] Keep test and production data separate. Never use real personal data for testing.
- [ ] Do not paste live secrets or personal data into AI chats.
- [ ] Test the main user journeys and failure states before launch.
- [ ] Set up backups and test a restore.

## Things to keep safe [Saved]

From the @tinchosms reel "Who's gonna tell Vibecoders about...", a scrolling list of engineering topics. Only the safety-related topics are here, grouped by me, with names as shown on screen. The full list is in [engineering-topics.md](engineering-topics.md). The reel gives names only, so "What safe looks like" is [Practice]. In a security review, mark each row PASS, FAIL, N/A or UNSURE.

| Area | Topics from the reel | What safe looks like |
|---|---|---|
| Sign-in | Authentication, Password Hashing, Salting, Hashing vs Encryption, Session Management, JWTs, OAuth, Two-Factor Authentication, Magic Links, Passkeys, Single Sign-On (SSO), Password Reset Flows, Email Verification, Account Lockout, Brute Force Protection, Token Expiration and Refresh, Cookie Flags (HttpOnly, Secure, SameSite) | Prefer an established auth provider. Hash passwords with a modern salted algorithm, and never store them in a reversible form. Keep tokens short-lived, set the cookie flags, and limit attempts on sign-in and reset flows. |
| Permissions | Authorization, Principle of Least Privilege, Role-Based Access Control, Row-Level Security, IDOR (Insecure Direct Object References), Mass Assignment, Multi-Tenancy, Admin Panels, UUIDs vs Auto-Increment IDs | Check ownership of every record on the server. Accept only the fields you expect, and keep each customer's data separate. Give admin panels stricter access. Unguessable IDs help but never replace a permission check. |
| Secrets | Environment Variables, Secrets Management, API Keys, Secret Rotation, SSH Keys, .gitignore | Keep secrets out of the browser and git. Limit each key to what it needs, and be able to rotate any key without an outage. |
| Web attacks | Input Validation, Data Validation on the Server, SQL Injection, XSS (Cross-Site Scripting), CSRF, SSRF (Server-Side Request Forgery), Open Redirects, Path Traversal, Command Injection, File Upload Security, Webhooks, Clickjacking, CORS, Content Security Policy, Security Headers | Validate on the server and use parameterised queries. Escape output. Use allowlists for redirects and server-side requests. Check the type and size of uploads, and store them away from the app. Verify webhook signatures. |
| Personal data | HTTPS / TLS, Encryption in Transit, Encryption at Rest, Presigned URLs, PII in Logs, Log Retention, Data Retention Policies, Data Privacy (GDPR), Data Export and Deletion Requests | Use HTTPS everywhere and encrypt stored sensitive data. Keep file links short-lived and personal data out of logs. Set retention periods, and be able to export or delete one person's data (see [legal-and-compliance.md](legal-and-compliance.md)). |
| Payments | PCI Compliance, Payment Webhooks, Refunds and Chargebacks, Money Handling (Never Use Floats) | Never let raw card details touch your servers: use a payment provider's hosted checkout. Verify payment webhooks, and make sure a repeated one can't charge or credit twice. Store money in whole minor units, such as pence or cents. |
| Abuse and cost | Rate Limiting, Bot Protection, CAPTCHA, DDoS Protection, WAF (Web Application Firewall), Firewalls, VPCs, Spam and Abuse Prevention, Content Moderation, Third-Party API Limits, Cost Monitoring | Limit public and costly endpoints. Expose only the services that must be public. Set spending alerts and caps, and have a way to report and remove harmful content. |
| AI features | Prompt Injection, LLM API Costs, Token Limits, Evaluating AI Output | Treat user and retrieved content as untrusted. Don't let model output trigger a sensitive action without a server-side check. Set per-user limits and a spending cap. |
| AI-written code and dependencies | Reviewing AI-Generated Code, Hallucinated Dependencies, Dependency Vulnerabilities, Supply Chain Attacks, Lockfiles, Dependency Pinning, Security Scanning (SAST / DAST), Penetration Testing, OWASP Top 10, Code Review | Check that every package an AI adds is real and is the one you meant. Commit lockfiles, scan before launch, and have someone review changes to sign-in, permissions and payments. |
| Recovery | Backups, Point-in-Time Recovery, Testing Backup Restores, Disaster Recovery, Rollbacks, Audit Logs, Monitoring, Uptime Monitoring, Alerting, SSL Certificate Renewal, Domain Names | Test a real restore and know how to roll back a release. Log admin and sensitive actions. Alert someone when things fail, and auto-renew certificates and domains. |

