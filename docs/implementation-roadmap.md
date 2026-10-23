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

## Post-launch feature queue: gangs and Josiah's arcade hideout

Add at least six hostile gang types: the stealth faction, the all-female faction, and at least four additional distinct factions. Give every hostile faction its own identity, combat style, equipment, leader, and authored leader encounter.

Introduce each hostile faction in a building. Only after V encounters it there as hostile should its members and leader encounters become eligible in the appropriate real-world city enemy pools. Persist the discovery flag per faction so saves and reloads do not unlock groups early or reroll their status.

After Josiah's rescue, his story reveals a friendly kid gang that uses hiding, scavenging, and theft. Some child NPCs around the city belong to it. They can offer information, diversions, hidden routes, and help recovering small stolen items. Josiah reveals their separate old-building hideout, which is filled with arcade machines.

Keep the kid gang out of hostile pools and the new building combat areas. Exclude its members from enemy targeting and faction-changing effects. Persist the reveal and hideout access. Follow the [future gangs and arcade hideout plan](future-gangs.md).

## Post-launch feature queue: Nette ripperdoc

A future update may add a separate hostage rescue for Nette. After V rescues her, she opens her own clinic and offers installation for the mod's body cybernetics and upgrades.

Build the clinic catalog around a shared cyberware registry. Read installed item definitions through the selected supported frameworks, normalize stable item IDs, slots, stats, prices, installation requirements, and source mod, and expose compatible items to Nette's vendor. Use optional adapters for mods that need special handling, never edit another mod's records, and report unsupported definitions clearly. Follow the detailed [cross-mod cyberware integration plan](cross-mod-cyberware.md).

Change Nette's hair and nail styles independently every six in-game days. Store each current style and next change day, and verify the cycle remains stable through sleep, time skips, and save reloads. Keep Nette's rescue, clinic, catalog, and appearance schedule in separate persistent state. This feature is post-launch and not required for the first playable release.

## Post-launch feature queue: Virtual Atelier store

Create a uniquely named Hidden Depths store once gear discovery and reward flags are in place. When V finds a Hidden Depths clothing, armor, or weapon reward, unlock that entry for later purchase in the store; keep undiscovered rewards hidden.

Create makeup and tattoo assets as separate cosmetic content, then add them to Atelier where the supported store integration accepts them. If an appearance option is not a normal purchasable item, link a compatible appearance menu from the shop instead. Virtual Atelier registers stores for existing item records; it does not create the underlying items. Follow the [Virtual Atelier integration plan](virtual-atelier-integration.md).

Declare Virtual Atelier and required frameworks as dependencies for the optional store package. Test with the framework installed and missing, check store and item ID uniqueness, verify discovery unlocks persist across reloads, and test item previews and cosmetic application. This feature is post-launch and not required for the first playable release.

## Post-launch feature queue: NPC appearance library

Create original eyes, tattoos, makeup, scars, and other appearance options for characters added by Hidden Depths, including rescuable characters, fixers, shop owners, ripperdocs, gangs, and mutants. Keep custom presets available when optional appearance packs are absent.

Optionally integrate eye colors from the installed Beautiful Exotics Eyes Pack — CCXL Version if its IDs can be safely assigned to mod-added NPCs. Keep the pack optional, do not bundle or copy its assets without permission, and provide original exotic eye variants as a fallback. Follow the [NPC appearance plan](npc-appearance-plan.md).

Test NPC appearances with and without the optional pack, verify unsupported or missing appearance IDs fall back cleanly, and check the supported body types.

## Post-launch feature queue: outskirts city

Build a DLC-sized outskirts expansion. After rescuing Nette, V learns of the region from her and clears a huge truck blocking the road tunnel; the route stays closed until that quest objective is complete. Prove tunnel travel, streaming, save behavior, vehicle state, traffic, navigation, and performance first. Build a central police station that is unusable at discovery and unlocks only after V rescues its captured captain from an authored hostile building. Add a new NPC cast, main and side quests, fixers, ripperdocs and clinics, shops, interiors, underground spaces, repeatable contracts, and an authored pool of randomly selected hostile building activities. Integrate gangs into appropriate regional and building pools only after their hostile building introductions; keep Josiah's kid gang friendly and outside combat pools. Add leaders and authored introductions for new region-specific hostile factions. Follow the detailed [outskirts city plan](outskirts-city-plan.md).

This is a major post-launch world project, not part of the first playable release. Build and test it in staged slices before treating it as a complete DLC-sized release.

## Post-launch feature queue: outskirts hostage cast, allies, and partners

Expand the outskirts hostage pool with authored local characters who can join the region after rescue: shop owners, additional ripperdocs, fixers, adult sex workers/joytoys, residents, workers, captured police, and other NPCs. Depending on their role, rescued characters can open or join local services, provide jobs or information, or become allies. Keep the existing rare hostage-event chance and eligibility rules. Persist individual rescue outcomes and prevent duplicate or story-ineligible captures. The station captain remains a dedicated authored rescue required to unlock the police station.

Build original recruitable allies with a companion feature set inspired by [Night City Allies — Immersive Companion System](https://www.nexusmods.com/cyberpunk2077/mods/27625): hangouts, squad recruitment, phone/contact-based summoning, follow and combat behavior, supported commands, outfit/equipment options, persistent unlocks, and selected apartment or safe-location interactions. Implement Hidden Depths characters and assets independently; do not copy that mod's code or assets. Optional integration must use documented, permitted compatibility hooks and be tested with the other mod both installed and absent.

At least two eligible rescued adult NPCs may have optional, choice-driven partner storylines and can also be recruited as allies. Keep romance and ally recruitment as independent choices; neither is automatic upon rescue. Add equipment/loadout support so every mod-added combat-capable NPC, including allies and partners, can use discovered Hidden Depths weapons with compatible ammunition. Use role-appropriate peaceful and combat loadouts and preserve existing Cyberpunk 2077 story states. Follow the detailed [outskirts city plan](outskirts-city-plan.md).

## Current repository state

The repository currently contains the design documents, a location data definition, a Python validator with tests, and ZIP packaging automation. It does not yet contain game assets, scripts, or an installable build. The release workflow intentionally refuses to create a release ZIP until actual installable files exist under `game-root/`.
