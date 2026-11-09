#!/usr/bin/env python3
"""Validate the repo: Agent Skills format, plugin manifests, and internal Markdown links.

Usage: python scripts/validate.py
Exit code 0 = all checks passed, 1 = at least one error.
Requires PyYAML (pip install pyyaml).
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
errors: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


# ---------------------------------------------------------------- skills
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def check_skills() -> int:
    skill_files = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if not skill_files:
        err("skills/: no SKILL.md files found")
    for path in skill_files:
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not m:
            err(f"{rel}: missing YAML frontmatter")
            continue
        try:
            meta = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError as e:
            err(f"{rel}: invalid YAML frontmatter ({e})")
            continue
        name = meta.get("name", "")
        desc = meta.get("description", "")
        folder = path.parent.name
        if not isinstance(name, str) or not NAME_RE.match(name) or len(name) > 64:
            err(f"{rel}: name '{name}' must be 1-64 chars of a-z, 0-9 and single hyphens")
        if name != folder:
            err(f"{rel}: name '{name}' must match folder '{folder}'")
        if any(w in str(name) for w in ("anthropic", "claude")):
            err(f"{rel}: name must not contain reserved words")
        if not isinstance(desc, str) or not (1 <= len(desc) <= 1024):
            err(f"{rel}: description must be 1-1024 characters (got {len(str(desc))})")
        if re.search(r"<[^>]+>", str(desc)):
            err(f"{rel}: description must not contain XML tags")
        if len(text.splitlines()) > 500:
            err(f"{rel}: SKILL.md should stay under 500 lines")
    return len(skill_files)


# ------------------------------------------------------- plugin manifests
def check_manifests() -> None:
    parsed = {}
    for rel in (".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"):
        path = ROOT / rel
        if not path.exists():
            err(f"{rel}: missing")
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            err(f"{rel}: invalid JSON ({e})")
            continue
        parsed[rel] = data
        if not data.get("name"):
            err(f"{rel}: 'name' is required")
    data = parsed.get(".claude-plugin/marketplace.json")  # None if missing or invalid
    if data is not None:
        if not data.get("owner", {}).get("name"):
            err(".claude-plugin/marketplace.json: owner.name is required")
        for p in data.get("plugins", []):
            if not p.get("name") or not p.get("source"):
                err(".claude-plugin/marketplace.json: each plugin needs name and source")


# ------------------------------------------------------- markdown links
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def slugify(heading: str) -> str:
    h = re.sub(r"`([^`]*)`", r"\1", heading.strip())
    h = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", h)
    h = h.replace("**", "").replace("*", "").lower()
    out = []
    for ch in h:
        cat = unicodedata.category(ch)
        if ch in " -_" or cat[0] in ("L", "N") or cat == "Mn":
            out.append(ch)
    return "".join(out).replace(" ", "-")


def anchors(path: Path) -> set[str]:
    found, counts, in_code = set(), {}, False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            s = slugify(m.group(2))
            n = counts.get(s, 0)
            found.add(s if n == 0 else f"{s}-{n}")
            counts[s] = n + 1
    return found


def check_links() -> int:
    md_files = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]
    for path in md_files:
        text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
        for target in LINK_RE.findall(text):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            file_part, _, anchor = target.partition("#")
            dest = path if not file_part else (path.parent / file_part).resolve()
            rel = path.relative_to(ROOT).as_posix()
            if not dest.exists():
                err(f"{rel}: broken link -> {target}")
            elif anchor and dest.suffix == ".md" and anchor not in anchors(dest):
                err(f"{rel}: missing anchor -> {target}")
    return len(md_files)


def main() -> int:
    n_skills = check_skills()
    check_manifests()
    n_md = check_links()
    if errors:
        print(f"FAILED: {len(errors)} problem(s)")
        for e in errors:
            print("  -", e)
        return 1
    print(f"OK: {n_skills} skills, 2 manifests, {n_md} Markdown files checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
