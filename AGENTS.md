# Maintaining this repo

Rules for any agent (Claude, Codex, Gemini) editing these standards. For using the standards on a project, read [SKILL.md](SKILL.md) instead.

## Workflow
- Commit straight to `main`. No branches, no pull requests, no asking first.
- After any change to `SKILL.md` or `references/`, run `python3 scripts/build-single-file.py` and commit the rebuilt export in the same commit.
- A new reference file needs a row in the task table in `SKILL.md` and an entry in the `order` list in `scripts/build-single-file.py`.

## Adding saved material (reels, screenshots, guides)
- Put each point in the reference file it belongs to; don't create a new file for one reel.
- Label it [Saved], and add the creator or source to `references/sources.md`.
- Check any fact, figure, date or law before adding it. Mark checked items [Researched] with the date, add the source link to `references/sources.md`, and correct the saved claim if it's wrong (say what the original said).
- Mark anything unchecked, cut off or likely to change with ⚠️ and say why.

## House style
- British English, sentence case (headings included), metric units, degrees Celsius, no em dashes.
- Amounts in £ or $ show the original first, with an approximate € conversion marked ⚠️.
- This repo is public: no personal details about the owner or private individuals (names, email addresses, phone numbers, addresses, clients, private projects). Credit public creators and sources by their public handle.
