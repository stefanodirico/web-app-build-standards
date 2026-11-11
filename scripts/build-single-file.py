"""Rebuild exports/web-app-build-standards-single-file.md from SKILL.md and references/.
Run from the repo root: python3 scripts/build-single-file.py"""
import re, sys
root = sys.argv[1] if len(sys.argv) > 1 else "."
out = sys.argv[2] if len(sys.argv) > 2 else "exports"
order = ["ux-audit", "design-and-craft", "motion-and-faux-ui", "security", "legal-and-compliance",
         "compliance-audit-prompts", "launch-checklist", "app-stores", "feature-ideas", "engineering-topics", "companion-skills", "sources"]
titles = {}
for n in order:
    first = open(f"{root}/references/{n}.md").readline().strip()
    titles[n] = first.lstrip("# ").strip()

def relink(t):
    return re.sub(r"\[[^\]]+\]\((?:references/)?([a-z-]+)\.md\)",
                  lambda m: f'the "{titles[m.group(1)]}" section', t)

skill = open(f"{root}/SKILL.md").read()
fm, body = re.match(r"(---\n.*?\n---\n)(.*)", skill, re.S).groups()
body = relink(body).replace("Read only the references the task needs.",
                            "Read only the sections the task needs; they follow this overview.")
parts = [body.rstrip()]
for n in order:
    t = open(f"{root}/references/{n}.md").read()
    t = re.sub(r"^(#{1,5}) ", lambda m: "#" + m.group(1) + " ", t, flags=re.M)
    # keep fenced code blocks unchanged
    fixed, inside = [], False
    for line in t.split("\n"):
        if line.startswith("```"): inside = not inside
        fixed.append(line[1:] if inside and line.startswith("##") else line)
    parts.append(relink("\n".join(fixed)).rstrip())
single = "\n\n".join(parts) + "\n"
open(f"{out}/web-app-build-standards-single-file.md", "w").write(single)
print(len(single), "chars,", len(single.split()), "words")
