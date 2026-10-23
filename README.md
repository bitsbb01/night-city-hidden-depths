# Night City: Hidden Depths

**Created by Bitsbb01**

A Cyberpunk 2077 mod project for exploring newly accessible locations, underground complexes, rescue missions, rare loot, and claimable vehicles.

## Project status

The feature scope, first Watson location, quest outline, and machine-readable content definition are in the repository. Playable world, quest, and mod files are still being developed; this repository does not yet contain an installable game mod.

## Design and content

- [Full feature brief](DESIGN.md)
- [First Watson location: The Quiet Track](docs/first-location.md)
- [First side activity outline](docs/quest-01-the-quiet-track.md)
- [Implementation roadmap](docs/implementation-roadmap.md)
- [Version and release plan](docs/version-release-plan.md)
- [Nette's cross-mod cyberware integration plan](docs/cross-mod-cyberware.md)
- [Virtual Atelier integration plan](docs/virtual-atelier-integration.md)
- [Mod-added NPC appearance plan](docs/npc-appearance-plan.md)
- [Future gangs and arcade hideout plan](docs/future-gangs.md)
- [Outskirts city expansion plan](docs/outskirts-city-plan.md)
- [Location content definition](content/locations/quiet-track.json)

The JSON definition records layout, pacing, encounter variation, hostage odds, one-time rewards, loot, and save-state requirements. It is validated as design data; it does not run in the game.

## Downloading releases

When an installable build is ready, each version will be published under **Releases** as a ZIP named `NightCityHiddenDepths-<version>.zip`.

To create a release, push a version tag such as `v0.1.0`. GitHub Actions runs the content tests, validates the location definition and game-root payload, packages them, and attaches the ZIP to that GitHub Release. The ZIP will contain the mod's game folders at its root; extract those folders into the Cyberpunk 2077 installation directory and merge them.

The release workflow deliberately stops if `game-root/` contains no actual mod payload, so an empty or documentation-only ZIP cannot be published by accident.

## Repository layout

- `content/locations/` — authored location definitions used for content checks.
- `game-root/` — files arranged as they should appear under the Cyberpunk 2077 install directory.
- `scripts/validate_content.py` — checks key design constraints in the location definitions.
- `tests/` — tests for the location content rules.
- `scripts/package_release.py` — validates and packages the installable payload.
- `.github/workflows/package-release.yml` — tests, validates, and builds a ZIP on version tags, then publishes it as a GitHub Release asset.

## Compatibility

The final release will list its supported Cyberpunk 2077 version and required mod frameworks. Do not treat this development repository as an installable release.
