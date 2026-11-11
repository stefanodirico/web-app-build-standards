# Website and app build standards

An agent skill for planning, building, reviewing and launching websites and apps: UK, EU and US legal checks, a 132-item UX audit, design that doesn't look AI-generated, security, domain setup, app store rules and a launch checklist.

It follows the open Agent Skills format: `SKILL.md` is the entry point and `references/` holds the detail each task loads.

## Install

This repo is public, so any tool can install from it without signing in. Only the owner can change it.

| Tool | How |
|---|---|
| Codex | Clone or copy this folder into `~/.agents/skills/web-app-build-standards/` (all projects) or `.agents/skills/` in a repo |
| Gemini CLI | `gemini skills install https://github.com/stefanodirico/web-app-build-standards.git`, or copy into `~/.agents/skills/` |
| Claude Code | Copy this folder into `~/.claude/skills/web-app-build-standards/` |
| Claude app | Save it from Claude's skill card. That copy is a short loader that reads the latest files from this repo each time, so it never goes stale. Or upload a zip of `SKILL.md` and `references/` |
| Google AI Studio, Gemini Gems, ChatGPT | Paste or upload `exports/web-app-build-standards-single-file.md` as instructions or knowledge |

## Updating

Edit `SKILL.md` or a file in `references/`, then rebuild the single-file export:

```
python3 scripts/build-single-file.py
```

Agents working on this repo follow [AGENTS.md](AGENTS.md).

## Credits

Design and motion sections summarise ideas from [Impeccable](https://github.com/pbakaus/impeccable), [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill), [Emil Kowalski's skills](https://github.com/emilkowalski/skills), [Oil UI](https://github.com/oil-oil/oil-ui), [Stageshow](https://benji.org/stageshow) and [awesome-design-md](https://github.com/VoltAgent/awesome-design-md). Full sources are in `references/sources.md`. This is a working checklist, not legal advice.
