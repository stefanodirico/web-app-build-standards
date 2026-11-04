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

