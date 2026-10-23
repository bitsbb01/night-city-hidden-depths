#!/usr/bin/env python3
"""Package the installable Cyberpunk 2077 game-root payload as a release ZIP."""

from __future__ import annotations

import os
import re
import sys
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
GAME_ROOT = REPO_ROOT / "game-root"
DIST = REPO_ROOT / "dist"
ALLOWED_GAME_ROOTS = {"archive", "bin", "mods", "r6", "red4ext"}
IGNORED_NAMES = {"README.md", ".gitkeep", ".DS_Store"}


def main() -> int:
    if not GAME_ROOT.is_dir():
        print("ERROR: game-root/ is missing.", file=sys.stderr)
        return 1

    payload = [
        path for path in GAME_ROOT.rglob("*")
        if path.is_file()
        and not path.is_symlink()
        and path.name not in IGNORED_NAMES
    ]

    if not payload:
        print(
            "ERROR: game-root/ has no installable files yet; refusing to publish an empty ZIP.",
            file=sys.stderr,
        )
        return 1

    unexpected = sorted({
        path.relative_to(GAME_ROOT).parts[0]
        for path in payload
        if path.relative_to(GAME_ROOT).parts[0] not in ALLOWED_GAME_ROOTS
    })
    if unexpected:
        print(
            "ERROR: unexpected top-level game-root path(s): "
            + ", ".join(unexpected)
            + ". Use Cyberpunk 2077 install folders such as archive/, bin/, mods/, r6/, or red4ext/.",
            file=sys.stderr,
        )
        return 1

    tag = os.environ.get("GITHUB_REF_NAME", "development")
    safe_tag = re.sub(r"[^A-Za-z0-9._-]+", "-", tag).strip("-") or "development"
    DIST.mkdir(parents=True, exist_ok=True)
    zip_path = DIST / f"NightCityHiddenDepths-{safe_tag}.zip"

    install_note = (
        "Night City: Hidden Depths\n"
        f"Version: {tag}\n\n"
        "Installation: extract this ZIP into your Cyberpunk 2077 installation folder "
        "and merge the included folders. Install any required frameworks listed in "
        "the release notes before launching the game.\n"
    )

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        archive.writestr("README-INSTALL.txt", install_note)
        for path in sorted(payload):
            archive.write(path, path.relative_to(GAME_ROOT).as_posix())

    print(f"Created {zip_path.relative_to(REPO_ROOT)}")
    print(f"Packaged {len(payload)} mod file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
