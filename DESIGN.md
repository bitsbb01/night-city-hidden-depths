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

## Future version: rescued shop owner

A later version may add a separate hostage rescue for a shop owner. After V rescues this person, they settle into one of the new shop areas in the normal world and open a usable store. Keep this character and rescue state separate from the vehicle painter so each reward has its own location and persistent save flag. The shop's inventory can grow with future equipment and building releases.

This is planned post-launch content; it does not change the first location's current 5% hostage pool.

## Future version: Josiah, rescued child and fixer

A later story update may add a hostage rescue for a child named Josiah. After V rescues him, Josiah becomes a fixer contact based in the apartment where V first starts free-roam. He uses a fixer app to offer repeatable jobs around Night City.

Choose jobs from authored mission templates and locations, with randomized targets, objectives, and rewards. Save the active job state so it does not reroll on reload, and track Josiah's rescue and fixer unlock separately from the other hostage rewards. This is a future-version feature and does not alter the initial hostage event odds.

## Future version: gangs and Josiah's arcade network

Add at least **six distinct hostile gang types** to the future faction pool: the stealth-focused gang, the all-female gang, and at least four additional gangs with their own identities, appearances, tactics, dialogue, equipment, and leaders. Each hostile faction should have an authored leader encounter in a building; after V meets that faction there and they are hostile, unlock its members and leader encounters in appropriate real-world city enemy pools. Save each faction's discovery/unlock so the open-world encounters remain consistent after reloads.

Josiah's future storyline also reveals a friendly kid gang that specializes in hiding, scavenging, and theft. The player learns about them only after finding and rescuing Josiah. Some children around the city belong to this group, but their affiliation stays unmarked until the reveal. They can help V with information, distractions, hidden routes, and recovering small stolen items.

Their hideout is a separate old building filled with arcade machines. This is social and exploration content: the kid gang is never hostile, never appears in the new building areas' combat encounters or hostile open-world pools, and is excluded from enemy targeting and faction-changing effects. Persist Josiah's reveal and hideout access in the save. See the [future gangs and arcade hideout plan](docs/future-gangs.md).

## Future version: Nette, rescued ripperdoc

A later update may add a hostage rescue for Nette, a new ripperdoc. After V rescues her, she opens her own clinic in a new area and can install the body's cybernetics and upgrades introduced by this mod.

Her clinic should include a cross-mod cyberware catalog. It should discover cybernetics from installed mods, normalize their item IDs, slots, stats, prices, and installation requirements, and offer the compatible items to V. Use adapters for mods that need special handling, leave other mods' item records untouched, and provide a compatibility report for entries that cannot safely be installed. The goal is broad support for installed cyberware mods; items without usable definitions may need an adapter. See the [cross-mod cyberware integration plan](docs/cross-mod-cyberware.md).

Nette's hair and nail appearance each change to a randomly selected style every **six in-game days**. Save the current styles and next change day so loading a save does not reroll them early. Track her rescue, clinic unlock, cyberware catalog, and appearance cycle separately from the other hostage rewards. This is future-version content and does not alter the initial hostage event odds.

## Future version: Virtual Atelier gear and cosmetics

Add a **Night City: Hidden Depths** Virtual Atelier store in a later version. Clothing, armor, and weapons found in the buildings become available for purchase there after V discovers them; undiscovered rewards stay hidden until found.

Create original makeup and tattoo options as cosmetic assets and unlocks. Integrate them with Virtual Atelier where the supported versions allow cosmetic entries; if an appearance option cannot be sold as a normal item, link the store to a compatible appearance menu. Virtual Atelier provides shop listings for items but does not create or apply the underlying gear or cosmetic assets. See the [Virtual Atelier integration plan](docs/virtual-atelier-integration.md).

## Future version: new appearances for mod-added NPCs

Give NPCs created by this mod—rescuable characters, fixers, shop owners, ripperdocs, gang members, and mutants—original eye colors, tattoos, makeup, scars, and other distinctive appearance options.

Create original exotic eye variants for Hidden Depths characters. Optionally support the installed [Beautiful Exotics Eyes Pack — CCXL Version](https://www.nexusmods.com/cyberpunk2077/mods/25718) when its appearance IDs can be applied safely to our NPCs. Keep this pack optional, do not bundle or copy its assets without the author's permission, and provide original eye looks when it is absent. See the [NPC appearance plan](docs/npc-appearance-plan.md).

## Future version: outskirts city via road tunnel

Add a new, explorable city on the outskirts of Night City, reached by driving through one of the road tunnels. It should feel like a separate city connected by a drivable road route, with its own streets, points of interest, shops, interiors, and side activities. Build it as a large post-launch world expansion, starting with a small tested map slice. See the [outskirts city plan](docs/outskirts-city-plan.md).

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
9. Add the rescued shop owner in a later version after the core location and shop area are ready.
10. Add Josiah's rescue, persistent apartment fixer contact, and replayable city jobs in a later story update.
11. Add Josiah's gang reveal, friendly arcade hideout, and the six hostile factions. Unlock each hostile faction in real-world encounters only after its first hostile building encounter.
12. Add Nette's rescue, clinic, cross-mod cyberware catalog, and six-day hair/nail appearance cycle in a later update.
13. Add the Virtual Atelier store, discovered-item unlocks, and supported makeup/tattoo integrations in a later release.
14. Add original appearances and optional eye-pack compatibility for Hidden Depths NPCs.
15. Build the outskirts city through a road tunnel as a later world expansion.
16. Test installation, saves, quest progression, and release ZIP before publishing a playable release.

## Compatibility and testing notes

World edits, custom quests, NPC behavior, custom equipment, custom vehicle appearances, and dynamic paint use different parts of the modding stack. Each feature must be tested in game on the declared game version. The project should list framework requirements and known compatibility issues in each release. Do not publish a playable release until the payload is installed and tested.
