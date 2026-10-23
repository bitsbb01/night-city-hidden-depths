# Implementation Roadmap

**Created by Bitsbb01 — Night City: Hidden Depths**

This roadmap turns the agreed design into buildable milestones. The location JSON is a checked design definition; it is not loaded by Cyberpunk 2077.

## Toolchain

CD PROJEKT RED provides REDmod and recommends using WolvenKit for its mod authoring workflow. WolvenKit is a community editor for Cyberpunk 2077 assets and REDengine formats. The [official modding support page](https://www.cyberpunk.net/en/modding-support) and the [WolvenKit guide](https://wiki.redmodding.org/wolvenkit) are the starting references.

The game project will need a Windows Cyberpunk 2077 installation and a current WolvenKit project. New geometry and connected interior spaces also need authored assets and in-game placement checks. Runtime quest state, random encounters, persistent rewards, and custom item behavior will need the compatible scripting and data tools for the supported game patch. Confirm framework versions when the first game project is created; mod compatibility can change with game updates.

## Milestones

### 1. First playable location

Build The Quiet Track as one authored Watson site:

- Verify a street approach and two separate entrances in the game.
- Connect the safehouse entrance to a usable room with bed, weapon storage, and computer.
- Build the freight floor, basement, maintenance tunnels, large rail chamber, and a return route.
- Add cover, traversal, lighting, doors, objective interactions, and enemy navigation.
- Complete one fixed quest run from lead to relay shutdown and exit.

This milestone proves that the location can be entered, traversed, fought through, and completed in the target game.

### 2. Replay state and rare event

Add selected authored encounter variants while keeping the building geometry fixed. Save each run's selected state so a save/reload does not reroll the hostage, patrols, or loot. Add the 5% hostage roll, captive variants, safehouse unlock, and one-time reward flags.

The content definition currently treats 5% as a roll per new run. Tune that cadence in-game so the event is rare without making the painter needlessly difficult to find.

### 3. Loot and equipment

Add the original weapon, clothing, armor, cyberware, enemy loadouts, and compatible ammunition as separate tested additions. Gate enemy use of each custom weapon behind the player's first discovery of it. Verify ordinary game weapon and ammo drops still work in the location.

Badge Roulette needs its own per-save awarded flag and careful target filtering. Its allegiance effect should avoid story-critical characters and should be tested around police wanted-state behavior before release.

### 4. Garage and painter

Add a hidden vehicle entrance as a location variant, then implement claimable vehicle rewards using supported vehicle assets. The painter rescue should persist and unlock his garage service in the normal world. Build and test paint presets, mixed colors, color shifting, and the ownership/app interface as a separate feature milestone.

### 5. Future version: hostage shop owner

After the core locations and shop area are established, add a separate hostage event for a shop owner. Rescuing them unlocks a persistent shop in one of the new shop areas. Store the rescue and shop-unlocked flags in the save, keep this person separate from the vehicle painter, and stock the store with appropriate mod rewards as the item pool grows.

This feature is planned for a later version; it is not part of the first playable release.

### 6. Release candidate

For each candidate build:

- Validate the location definitions and run the automated content tests.
- Install the packaged files in a clean game profile with only the documented dependencies.
- Test a new save, an existing save, save/reload during a run, each entrance, the hostage outcome, one-time rewards, and the exit.
- Test the current supported game patch and record required frameworks and known issues.
- Publish the tested install-layout files through the ZIP release workflow.

## Post-launch feature queue: Josiah fixer

A future story update may add a separate rescue for Josiah, a hostage child. After the rescue, make him a persistent fixer contact in the apartment where V first starts free-roam. He offers repeatable city jobs through a fixer app.

Build the jobs from authored mission and location templates, varying targets, objectives, and rewards. Persist each active job across saves so a reload cannot reroll it. Keep Josiah's rescue and fixer unlock in their own save state; this feature does not change the initial 5% hostage odds and is not required for the first playable release.

## Post-launch feature queue: Nette ripperdoc

A future update may add a separate hostage rescue for Nette. After V rescues her, she opens her own clinic and offers installation for the mod's body cybernetics and upgrades.

Add a catalog of cybernetics from installed mods, offering entries that expose the data needed for purchase and installation through the supported frameworks. Test with multiple installed cyberware mods, incompatible entries, and missing definitions so the clinic reports unsupported items instead of breaking.

Change Nette's hair and nail styles independently every six in-game days. Store each current style and next change day, and verify the cycle remains stable through sleep, time skips, and save reloads. Keep Nette's rescue, clinic, catalog, and appearance schedule in separate persistent state. This feature is post-launch and not required for the first playable release.

## Current repository state

The repository currently contains the design documents, a location data definition, a Python validator with tests, and ZIP packaging automation. It does not yet contain game assets, scripts, or an installable build. The release workflow intentionally refuses to create a release ZIP until actual installable files exist under `game-root/`.
