# Night City: Hidden Depths — Build Brief

**Created by Bitsbb01**

This document records the agreed gameplay scope for the mod. It is a design target, not a claim that the features are already implemented.

## Core concept

Open up a curated set of previously inaccessible Night City buildings and turn them into replayable side activities. Each location should feel authored and connected to the city. Randomness selects among prepared locations, encounter layouts, loot, and events; it does not generate arbitrary building geometry at runtime.

The first location is an early-game Watson site. It should become available once the player can freely explore Watson, without requiring late-story progression.

## First location: Watson safehouse and facility

The initial building has two separate routes:

1. **Safehouse entrance** — a safe room with a weapon storage box, bed, and usable computer.
2. **Hostile entrance** — a gang-held basement leading through multiple rooms into a much larger underground area.

The hostile route may continue into maintenance tunnels, abandoned rail tracks, service stations, and connected chambers. It should support roughly 20 minutes of exploration and combat for an average playthrough, using multiple encounters, clues or security obstacles, optional loot, and a hostage objective. Actual playtime will vary with player skill and build.

## Replayable building activities

- Add locations through side-quest leads, such as fixer messages, terminals, or discovered evidence.
- Choose from hand-authored building layouts and encounter variations.
- Vary gang type, guard positions, boss, loot, hostage state, and optional objectives.
- Preserve quest and one-time reward state in the save.
- Expand the location pool over time, including large tunnel and rail complexes.

## Hostages and the vehicle specialist

A hostage event has a **5% chance per building run**. The captive may be a civilian or a captured officer. A rare named rescue can also occur when it will not conflict with the character's existing story state.

One special hostage is a vehicle painter. Once rescued, he appears at a persistent garage in the normal world. He can install custom paint technology and give V an in-game paint app/menu for upgraded vehicles. It should support a color picker, two-tone paint, and a color-shifting finish. The shifting finish must be installed on each supported vehicle before remote color changes are available.

## Enemies and mutations

- Include ordinary gang encounters plus selected bio-experiment encounters.
- Create mutated-looking hostile NPC variants using custom appearances and suitable equipment.
- Keep mission-critical NPCs out of random faction-changing effects.
- Build the underground areas as authored spaces with navigation, cover, combat sightlines, working doors, and safe exits.

## Loot and equipment

- Use the game's existing weapon, ammunition, and item loot where appropriate.
- Add original standalone weapons, clothing/armor, and functional cyberware as rewards.
- Give custom weapons compatible ammunition so players can find more rounds in containers and on enemies.
- Add custom weapons to selected gang loadouts and drops. After V first discovers a weapon, selected later encounters may start using it.
- Keep early-game rewards balanced and distribute rare gear in optional or dangerous areas.

### One-off weapon: Badge Roulette

Badge Roulette is a unique weapon awarded once per save. Its shots temporarily scramble the allegiance of nearby ordinary NPCs: police may turn hostile, gang members may behave like police, and civilians may randomly join either side. The effect should use a clear visual cue and avoid story-critical characters. The unique award must not be duplicated by replaying the location or reloading after collection.

## Claimable vehicles

- Some buildings may roll a hidden garage, tunnel depot, or rail-side vehicle bay.
- Found compatible cars or bikes can be claimed and added to V's summon list.
- Add custom appearances for selected rewards, including altered paint, textures, body kits, bumpers, lights, rims, fenders, and bike fairings.
- Register modified rides as separate summonable variants so the original game vehicle remains intact.
- Make the rescued vehicle painter's color app work only with vehicles configured for the paint system.

## GitHub releases and creator credit

- Credit the project as **Created by Bitsbb01** in the repository and release documentation.
- Keep installable game files under `game-root/` in Cyberpunk 2077 folder layout.
- A version tag (for example, `v0.1.0`) triggers GitHub Actions to validate the payload, create `NightCityHiddenDepths-<version>.zip`, and attach it to a GitHub Release.
- The packaging script refuses to create a documentation-only or empty mod ZIP.

## Suggested implementation order

1. Establish the project against a specific Cyberpunk 2077 version and required frameworks.
2. Build and test the first Watson safehouse/interior entry and a compact basement encounter.
3. Add quest progression, persistent safehouse interactions, and hostage rescue.
4. Expand the first site into the tunnel/rail complex and meet the 20-minute gameplay target.
5. Add loot, custom weapons, clothing/armor, cyberware, and gang loadouts.
6. Add Badge Roulette and test its NPC behavior and one-time save reward.
7. Add a garage vehicle claim, then custom vehicle appearances and the painter/color app.
8. Add more building variants, the rare hostage roll, and mutated enemy encounters.
9. Test installation, saves, quest progression, and release ZIP before publishing a playable release.

## Compatibility and testing notes

World edits, custom quests, NPC behavior, custom equipment, custom vehicle appearances, and dynamic paint use different parts of the modding stack. Each feature must be tested in game on the declared game version. The project should list framework requirements and known compatibility issues in each release. Do not publish a playable release until the payload is installed and tested.
