Night City Hidden Depths - CET encounter test scaffold

INSTALL
Copy the night_city_hidden_depths folder into:
Cyberpunk 2077/bin/x64/plugins/cyber_engine_tweaks/mods/

The folder should contain init.lua and door_encounter.lua directly.

IN GAME
1. Start Cyberpunk 2077 and load a save.
2. Open the CET overlay, go to Bindings > Hotkeys, and assign keys to the
   Night City Hidden Depths entries. CET requires manual key binding.
3. Use “NCHD: Test encounter roll (no door)” to print a random result in the
   CET console/log.
4. Aim at a real door and use “NCHD: Open aimed door and roll encounter”. It
   opens the targeted Door and prints the selected result. Each door position
   is only rolled once; the record is kept in progress.json in this mod folder.
5. The three “Test mark ... rescued” hotkeys exercise the persistent rescue
   flags. After a hostage is marked rescued, future dungeon rolls skip them.

CURRENT TEST SCOPE
This checks the encounter percentages, door targeting/opening, saved door
rolls, and saved hostage rescue flags. It does not yet create dungeon rooms,
spawn NPCs/hostages, or place loot. Those need working spawn templates and
tested coordinates. This test hotkey intentionally opens the targeted door;
it is not yet a transparent replacement for the game's normal interact action.

The progress file is local to this CET mod folder and is separate from game
save slots. Back it up before deleting or reinstalling the mod.
