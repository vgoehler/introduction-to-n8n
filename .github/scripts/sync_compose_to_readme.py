#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

README = Path("lesson_01.md")
COMPOSE = Path("docker-compose.yaml")

START = "<!-- DOCKER_COMPOSE_YAML_START -->"
END = "<!-- DOCKER_COMPOSE_YAML_END -->"

def die(msg: str, code: int = 1) -> None:
    print(msg)
    raise SystemExit(code)

def normalize_newlines(s: str) -> str:
    # normalize line endings and ensure trailing newline
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    if not s.endswith("\n"):
        s += "\n"
    return s

def main() -> None:
    if not README.exists():
        die(f"ERROR: {README} not found.")
    if not COMPOSE.exists():
        die(f"ERROR: {COMPOSE} not found.")

    readme_text = normalize_newlines(README.read_text(encoding="utf-8"))
    compose_text = normalize_newlines(COMPOSE.read_text(encoding="utf-8"))

    if START not in readme_text or END not in readme_text:
        die(f"ERROR: Markers not found in README.md. Expected {START} and {END}")

    start_idx = readme_text.index(START) + len(START)
    end_idx = readme_text.index(END)

    before = readme_text[:start_idx]
    middle = readme_text[start_idx:end_idx]
    after = readme_text[end_idx:]

    # Build replacement block (always includes fenced yaml codeblock)
    replacement = "\n```yaml docker_compose.yaml\n" + compose_text + "```\n"

    # Extract current yaml block content (best-effort) for comparison:
    # We'll compare the exact replacement with what's currently between markers, trimmed.
    current = middle.strip("\n")
    desired = replacement.strip("\n")

    if current == desired:
        print("README is already in sync with docker-compose.yaml.")
        return

    new_readme = before + "\n" + replacement + "\n" + after
    new_readme = normalize_newlines(new_readme)

    README.write_text(new_readme, encoding="utf-8")
    print("README updated to match docker-compose.yaml.")

if __name__ == "__main__":
    main()
