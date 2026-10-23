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

## Future version: rescued arcade owner and arcade network

Add a separate adult arcade owner to the future hostage pool. After V rescues them, they open several arcades across Night City and later the outskirts city. Each venue has playable cabinets, a persistent unlock, and optional high-score rewards. Keep this character and commercial arcade network separate from Josiah's friendly kid-gang hideout.

Use the base game's own cabinet activations for **Trauma Drama** and **Roach Race** at the new venues if supported hooks allow it; do not copy or redistribute base-game logic or assets. Create the arcade games ourselves as original, free-to-play minigames for the mod, with original names, code, graphics, and sound. Start with maze-chase, falling-block, and a retro first-person maze-shooter, using only the general genres as inspiration. Avoid the Pac-Man/Tetris/Doom brands, characters, art, music, and other protected expression. Third-party open-source or public-domain games can be optional additions only after verifying code, engine, and asset licenses and meeting attribution/source obligations. Prefer an in-game UI prototype and do not launch external executables. See the [arcade owner and network plan](docs/arcade-network-plan.md).

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

Add a new, explorable outskirts city as a DLC-sized post-launch expansion. After rescuing Nette, V learns of it from her and clears a huge truck blocking the connecting road tunnel; only then can V drive through and discover the region. The city includes a central police station that is initially unusable and unlocks only after rescuing its captured captain from a hostile building. Add local NPCs, quests, fixers, ripperdocs, shops, and a pool of authored random hostile building activities. Gate gang appearances behind their hostile building introductions, and keep Josiah's kid gang friendly and out of combat pools. Build and test the route and map in slices before expanding the region. See the [outskirts city plan](docs/outskirts-city-plan.md).

## Future version: outskirts hostage cast, allies, and partners

Expand the outskirts hostage pool with authored local characters who can join the region after rescue: shop owners, additional ripperdocs, fixers, adult sex workers/joytoys, residents, workers, captured police, and other NPCs. Based on their role, rescued characters can open or join local services, provide jobs or information, or become allies. Keep the existing rare hostage-event chance and eligibility rules. Named rescues must be tracked separately, and the police captain remains a dedicated authored rescue required to unlock the central station.

Add original recruitable allies with a companion feature set inspired by [Night City Allies — Immersive Companion System](https://www.nexusmods.com/cyberpunk2077/mods/27625): hangouts, recruitable squad members, phone/contact-based summoning, follow and combat behavior, supported commands, outfit and equipment options, persistent unlocks, and selected apartment or safe-location interactions. This is a feature reference, not permission to reuse its code or assets. Build Hidden Depths companions independently; optional compatibility should use permitted, documented hooks only.

At least two eligible rescued adult NPCs may have optional, choice-driven partner storylines and can also be recruited as allies. Keep romance separate from ally recruitment and respect player choices; rescuing a character does not automatically create a relationship. All mod-added NPC archetypes, including allies and partners, need compatible equipment/loadout support for the new weapons. Combat-capable NPCs can use discovered Hidden Depths weapons with compatible ammunition; use role-appropriate gear and preserve peaceful service scenes. Preserve existing story-critical characters and state. See the [outskirts city plan](docs/outskirts-city-plan.md).

## Future version: scrapyard rescue and Scrapper vendors

After V rescues the outskirts police captain and unlocks the station, the captain gives V a lead about an injured old man stranded in a junkyard at the edge of the new city. V must fight multiple aggressive dogs to reach the man's hut. The old man explains that three elevated automatic turrets are offline and require a power unit carried by the gang leader below one of the turret poles. Defeat the leader, recover the unit, and restore power to all three turrets so they eliminate remaining hostile dogs and other hostile intruders. Turret targeting must never harm V, rescued characters, civilians, or recruited allies.

Rescuing the old man unlocks him as a Scrapper vendor and prompts him to contact his Scrapper friends. Additional non-hostile Scrapper NPCs then appear at authored outskirts locations and sell random selections of Hidden Depths weapons and vehicle parts. Persist vendor inventories and refresh state to prevent reload rerolls and duplicate purchases.

Add vehicle parts for Hidden Depths cars and bikes, including speed, armor, and hood-weapon upgrades. Define compatible vehicles and slots, balanced effects, installation and removal, controls for any added weapons, and persistent vehicle configurations. Compatibility with base-game or third-party vehicles requires separate testing. See the [outskirts city expansion plan](docs/outskirts-city-plan.md).

## Future version: rescued ocular doctor and eye cyberware

Add a new eye doctor/ocular specialist as an authored hostage rescue in the outskirts building pool. After rescue, she opens an eye clinic in the new area and offers cosmetic eye customization plus new ocular cyberware. Track her rescue and clinic unlock persistently and prevent duplicate appearances.

Cosmetic options include new eye colors and tints, iris shapes and patterns, and robotic or partly mechanical eyes. Keep appearance options separate from functional implants. Her ocular implants can include night vision, a hostile tracker, and a sniper enhancer that improves supported sniper-scope magnification or target clarity, with further options such as optic zoom and glare reduction. Add item IDs, ocular slots/capacity, costs, activation rules, and balance.

Integrate supported ocular implants into the shared cyberware catalog with Nette, without modifying other mods' records. Validate the night-vision effect, hostile highlighting, and sniper-scope support in game before release; document any unsupported behavior and provide a fallback. See the [cross-mod cyberware integration plan](docs/cross-mod-cyberware.md) and [outskirts city plan](docs/outskirts-city-plan.md).

## Future version: rescued comic-shop owner and comic reader

Add a comic-shop owner as a separate authored hostage rescue in the outskirts. After the rescue, they open a persistent store with comic covers on the shelves. Selecting a cover opens a custom in-game reader for compatible comics bundled with the mod.

Cyberpunk 2077 has a readable comic-related shard called **Dr. Havoc & Radon**, but it is not a full issue PDF or an in-game multipage comic-store reader. Use the title only as a lore reference; do not extract or redistribute the game's shard or assets.

The starter library should include the user's original **Last Instinct — Issue 1** when its final PDF is ready, plus online comics whose redistribution rights are verified. **Sharing Creative Works: An Illustrated Primer** is a downloadable comic dedicated to the public domain. Keep author, source, and rights details in the package manifest.

Since direct PDF rendering in the game is not established, convert licensed PDFs to optimized page images and cover thumbnails during packaging, then display them in a custom page-turning UI. Verify feasibility, input, memory use, and performance in an in-game prototype before expanding the library. See the [comic store and reader plan](docs/comic-store-plan.md).

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
- Provide compatible loadouts for all mod-added combat-capable NPCs, including recruitable allies and partner characters; allow assigned discovered weapons and ensure compatible ammunition and combat behavior.
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
15. Build the outskirts city as a DLC-sized expansion: unlock discovery through Nette's lead and quest-cleared truck blockage, then add the city map, inactive central police station and captain-rescue unlock, local cast and quest arc, fixers, ripperdocs, shops, authored hostile building and hostage pools, faction introductions, and gated regional encounter pools.
16. Add the rescued comic-shop owner, bookshelf displays, rights-checked comic library, PDF-to-page build step, and in-game reader.
16. After the captain rescue, add the scrapyard mission, injured old man, three powered turrets, Scrapper vendor network, randomized mod-gear stock, and vehicle-part upgrades for Hidden Depths vehicles.
17. Add rescued local service NPCs, recruitable companions, optional partner storylines, and tested compatibility hooks; keep new assets/code original and companion features independently implemented.
18. Test installation, saves, quest progression, and release ZIP before publishing a playable release.

## Compatibility and testing notes

World edits, custom quests, NPC behavior, custom equipment, custom vehicle appearances, and dynamic paint use different parts of the modding stack. Each feature must be tested in game on the declared game version. The project should list framework requirements and known compatibility issues in each release. Do not publish a playable release until the payload is installed and tested.
