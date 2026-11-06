---
name: web-app-build-standards
description: Stefano's standards for planning, building, reviewing and launching websites and apps. Covers UK and EU legal checks, a 132-item UX audit, design that doesn't look AI-generated, security for vibe-coded apps, domain setup, app store rules and a launch checklist. Use for any website, web app, mobile app, landing page, UI, front-end or coding task, and whenever asked to audit, review, harden or launch one.
---

# Website and app build standards

Apply this to every website, app or coding task. Read only the references the task needs.

## House style

- British English, sentence case (headings included), degrees Celsius, metric units, no em dashes.
- Accuracy first. Never invent facts, figures, reviews, logos or legal claims. Flag anything uncertain with ⚠️, say why, and offer up to three possible answers marked as unconfirmed.
- Ask clear questions, and list them together at the end of the reply.

## Rules that always apply

1. **Evidence or it didn't pass.** Mark each checked item PASS, FAIL, N/A, UNSURE (say why) or MANUAL (say how to check). Cite file:line for code findings.
2. **The brand and the brief win.** A project's DESIGN.md or brand file overrides the "generated look" tells. Treat tells as prompts, not bans.
3. **Secrets stay on the server.** No secret key in frontend code, the app bundle or git history.
4. **Permissions live on the server or database**, never only in the UI.
5. **Ask before** making legal claims about a specific project, installing anything, deleting files, or changing more than was asked.
6. **Look at what renders.** Check the real page at desktop and phone widths before calling visual work done; if you can't, say "visual result not verified".

## Pick the task, then read

| Task | Read |
|---|---|
| Starting a new site or app | [legal-and-compliance.md](references/legal-and-compliance.md) (start-here questions), [design-and-craft.md](references/design-and-craft.md) (parts 1 to 4), [security.md](references/security.md), then set up the project files below |
| Building or changing UI | The project's DESIGN.md, [design-and-craft.md](references/design-and-craft.md), relevant items in [ux-audit.md](references/ux-audit.md) |
| "Audit the UX" or "review the app" | [ux-audit.md](references/ux-audit.md), followed exactly: read-only, report table, then stop and ask which fixes to make |
| Security review or "harden this" | [security.md](references/security.md) |
| Launching, or "is it ready?" | [launch-checklist.md](references/launch-checklist.md), [legal-and-compliance.md](references/legal-and-compliance.md), and [app-stores.md](references/app-stores.md) for native apps |
| Buying or setting up a domain or email sending | [launch-checklist.md](references/launch-checklist.md), domain setup |
| Setting up staging or preview deployments, or an app that keeps breaking in production | [launch-checklist.md](references/launch-checklist.md), staging and preview environments |
| Animation, transitions or a product demo | [motion-and-faux-ui.md](references/motion-and-faux-ui.md) |
| "What features could we add?" | [feature-ideas.md](references/feature-ideas.md) |
| Needs more depth or tooling | [companion-skills.md](references/companion-skills.md) |
| Checking where a rule came from | [sources.md](references/sources.md) |

## Set up every new project

Create or update these in the project root, and ask before overwriting anything:

1. **DESIGN.md**: the design system (structure in [design-and-craft.md](references/design-and-craft.md), part 2).
2. **AGENTS.md** (read by Codex; Claude Code reads CLAUDE.md and Gemini CLI reads GEMINI.md by default, so put the same lines there too), containing at least:

```markdown
## Standards
- Follow the web-app-build-standards skill for all UI, security and launch work.
- British English, sentence case, no em dashes.
- Read DESIGN.md before any UI change.
- Secrets stay server-side; permissions are enforced on the server or database.
## Access control
(the access control matrix template from the security standards, filled in for this project)
```

## Reporting

Lead with what blocks launch or the main user journey. Sort findings HIGH (blocks sign up, onboarding, checkout, the core feature, or locks someone out), MEDIUM (friction elsewhere), LOW (polish). List MANUAL checks with how to do them. End with the questions, then stop before fixing unless told to go ahead; when fixing, do one change at a time and show the diff.
