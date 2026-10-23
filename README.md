# Night City: Hidden Depths

A Cyberpunk 2077 mod project for exploring newly accessible locations, underground complexes, rescue missions, rare loot, and claimable vehicles.

## Project status

This repository is the project home and release-packaging scaffold. The playable mod files are still being developed; this repository does not yet contain an installable game mod.

## Downloading releases

When an installable build is ready, each version will be published under **Releases** as a ZIP named `NightCityHiddenDepths-<version>.zip`.

To create a release, push a version tag such as `v0.1.0`. GitHub Actions will validate the game-root payload, package it, and attach the ZIP to that GitHub Release. The ZIP will contain the mod's game folders at its root; extract those folders into the Cyberpunk 2077 installation directory and merge them.

The release workflow deliberately stops if `game-root/` contains no actual mod payload, so an empty or documentation-only ZIP cannot be published by accident.

## Repository layout

- `game-root/` — files arranged as they should appear under the Cyberpunk 2077 install directory.
- `scripts/package_release.py` — validates and packages the installable payload.
- `.github/workflows/package-release.yml` — builds a ZIP on version tags and publishes it as a GitHub Release asset.

## Compatibility

The final release will list its supported Cyberpunk 2077 version and required mod frameworks. Do not treat this development repository as an installable release.
