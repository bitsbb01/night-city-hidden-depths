# Night City: Hidden Depths

**Created by Bitsbb01**

A Cyberpunk 2077 mod project for exploring newly accessible locations, underground complexes, rescue missions, rare loot, and claimable vehicles.

## Project status

The feature scope and first authored location are documented, and a CET door-encounter test scaffold is now included under `game-root/`. The scaffold can be installed for testing, but it only rolls/logs encounter outcomes and opens a targeted real door; it does not yet spawn dungeon geometry, NPCs, hostages, or loot.


## CET door encounter test scaffold

The test mod is under `game-root/bin/x64/plugins/cyber_engine_tweaks/mods/night_city_hidden_depths/`. It provides hotkeys to roll the requested 25% dungeon / 65% ambient / 10% stash split, test hostage persistence, and open a targeted real door for a one-time roll. It logs selections; it does not yet spawn rooms, NPCs, or loot. See [the test guide](docs/door-encounter-prototype.md). This per-door prototype is separate from the first authored location's run-level 5% hostage design.

The repository is released under the [MIT License](LICENSE) for original project code and documentation. Cyberpunk 2077 assets and third-party content are not included and remain subject to their own rights and licenses.

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
- [Comic store and in-game reader plan](docs/comic-store-plan.md)
- [Rescued arcade owner and playable arcade network plan](docs/arcade-network-plan.md)
- [Location content definition](content/locations/quiet-track.json)
- [Quest flow definition](content/quests/quiet-track-flow.json)

The JSON definition records layout, pacing, encounter variation, hostage odds, one-time rewards, loot, and save-state requirements. It is validated as design data; it does not run in the game.

## Downloading releases

When an installable build is ready, each version will be published under **Releases** as a ZIP named `NightCityHiddenDepths-<version>.zip`.

To create a release, push a version tag such as `v0.1.0`. GitHub Actions runs the content tests, validates the location definition and game-root payload, packages them, and attaches the ZIP to that GitHub Release. The ZIP will contain the mod's game folders at its root; extract those folders into the Cyberpunk 2077 installation directory and merge them.

The release workflow deliberately stops if `game-root/` contains no actual mod payload, so an empty or documentation-only ZIP cannot be published by accident.

## Repository layout

- `content/locations/` and `content/quests/` — authored location and quest-flow definitions used for content checks.
- `game-root/` — files arranged as they should appear under the Cyberpunk 2077 install directory.
- `scripts/validate_content.py` — checks key design constraints in the location definitions.
- `scripts/validate_quest_flow.py` — checks quest graph transitions, reachability, terminal states, and save facts.
- `tests/` — tests for the location content rules.
- `scripts/package_release.py` — validates and packages the installable payload.
- `.github/workflows/package-release.yml` — tests, validates, and builds a ZIP on version tags, then publishes it as a GitHub Release asset.

## Compatibility

The final release will list its supported Cyberpunk 2077 version and required mod frameworks. Do not treat this development repository as an installable release.
