# Door encounter CET prototype

This prototype adds a manually triggered CET door test to the repository's authored-location workflow. It does not change the authored geometry rule or the first location's run-level hostage design. It tests the requested per-door selection model separately:

- 1–25: random dungeon encounter
- 26–90: ambient room, evenly split between empty room, NPC drug-use scene, and consensual adult encounter
- 91–100: stash room
- Within a dungeon result, an independent 5% roll selects an unrescued hostage

The test selects among the eight planned underground archetype labels and a placeholder pool of base-game gangs. These are labels for planning and log output; the prototype does not place NPCs, hostage actors, room geometry, or loot.

## Installation and use

The files are packaged under `game-root/bin/x64/plugins/cyber_engine_tweaks/mods/night_city_hidden_depths/`. Copy the included `bin/` folder into the Cyberpunk 2077 installation directory and merge it.

After loading a save, bind the Night City Hidden Depths hotkeys in CET Overlay → Bindings → Hotkeys:

- **Test encounter roll (no door)** logs a random outcome.
- **Open aimed door and roll encounter** opens a real door currently targeted by the player, logs its outcome, and records that door position so it cannot reroll.
- **Test mark ... rescued** exercises each persistent hostage flag.

The door hotkey is a temporary test control. It deliberately unlocks/opens the targeted door and is not an automatic hook into the game's normal interaction action. Fake doors are not supported. Results appear in the CET console/game log.

## Persistent state and limits

`progress.json` is stored beside the Lua files in the mod folder. It tracks rescued hostages and door positions already rolled. The file is local to the mod installation, not a per-savegame record yet; a later save integration should move this state into game quest facts or another save-aware system.

CET can run Lua logic, but this prototype does not generate geometry or stream custom rooms. Production encounters need authored room variants, tested spawn points and templates, and then hooks that activate them through the normal door interaction path.
