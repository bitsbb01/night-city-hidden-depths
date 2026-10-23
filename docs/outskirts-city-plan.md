# Future Outskirts City Expansion

**Created by Bitsbb01 — Night City: Hidden Depths**

This is a DLC-sized post-launch expansion plan, not an implemented map. The goal is a substantial, coherent new region with its own cast, quest content, services, factions, and replayable activities—not just an empty map extension.

## Access route and discovery

V first learns about the outskirts city from Nette after rescuing her and unlocking her clinic. Nette provides a lead to a road tunnel that has been sealed by a huge abandoned truck blocking the entire passage. Her job is to clear the blockage. Once V destroys or otherwise removes the truck through the authored quest interaction, the tunnel opens as a drivable route and V can continue through to discover the new area.

Keep the city undiscovered and inaccessible before this lead and blockage objective are completed. Preserve the quest step and tunnel state through save/reload, and do not let ordinary traffic or unrelated missions clear the blockage. Nette gives the lead from her established Night City location, so V does not need access to the outskirts to start the quest.

The tunnel remains the visible road connection between the two places. The transition should feel like a continuous trip, using world streaming or a short concealed transition only if the engine requires it.

## Player route and region

The destination is a distinct small city area with a recognizable center, connected streets, named districts, and a range of points of interest. Its final size, name, districts, and story remain open for later design. Build a compact, polished slice first, then expand the region in authored sectors.

At the heart of the city, build a prominent police station. It is present when V first discovers the region, but remains locked, inactive, and unavailable as a usable service hub. One of the new hostile building activities can contain the captured station captain. Rescuing the captain unlocks the station and its authored services and interactions. Persist the rescue and station unlock separately from tunnel access; reaching the city alone must never activate the station.

## DLC-sized content goals

Treat the region as a full expansion with a connected set of activities and characters:

- Add a new local NPC cast: residents, workers, vendors, allies, quest contacts, police personnel, and faction members, with original appearances and dialogue.
- Give the region its own fixer network, including new fixers who offer authored main and side jobs plus repeatable contracts.
- Add new ripperdocs and clinics that provide services and support Hidden Depths cyberware. Nette may establish a clinic here if it fits the final story and location plan, while her pre-existing lead remains available in Night City.
- Build shops and other social hubs, including the rescued comic-shop owner, bookshelf displays, and an in-game reader for bundled comics.
- Create a main quest arc, side jobs, rescue events, and optional activities that make the region feel connected to the wider Hidden Depths storyline.
- Add a varied set of accessible interiors, underground routes, service tunnels, garages, and other points of interest.
- Add traffic, pedestrians, ambient encounters, and appropriate faction activity across the region.
- Place new gear and rewards through authored activities, while using existing game loot where it fits.

The intended scale is several substantial districts and a meaningful quest/activity set. Exact mission count and map size should be set after the first in-game slice proves the toolchain and performance budget.

## Hostage and rescue character pool

Use the region's hostage events to introduce original local characters who can become part of the city after rescue. The possible captives can include shop owners, a comic-shop owner, ripperdocs, fixers, an ocular specialist/eye doctor, adult sex workers/joytoys, local workers, residents, police officers, and other authored NPCs. A rescued character can return to the outskirts and open or join an appropriate service, offer jobs or information, become an ally, or contribute to a follow-up quest, depending on their role.

Keep the existing rare hostage-event chance and save rules. Choose only from authored, eligible characters; prevent duplicate rescues and avoid selecting a character whose quest state is unavailable. Maintain the police captain as a separate authored rescue required to activate the station, so random selection cannot block that unlock. Include at least two eligible rescued adult NPCs who can later offer optional partner storylines; each can also be recruited as an ally, and rescue alone never starts a romance. All sex-worker characters and potential partners are adults. Make partner and ally choices independent so the player can choose friendship, partnership, both, or neither.

## Hostage specialist: ocular doctor

Add an authored hostage rescue for a new eye doctor (ocular specialist) in one of the outskirts' hostile building activities. Keep her eligible for the rescue pool with a persistent, non-duplicating rescue state. Once rescued, she establishes an eye clinic in the new area and offers both cosmetic eye customization and functional ocular cyberware.

Her cosmetic catalog can unlock original eye colors and tints, iris shapes and patterns, and robotic or partly mechanical eye styles. Her functional ocular catalog can include night vision, a hostile-target tracker, and a sniper enhancer that improves supported scope magnification or target clarity while V uses a sniper rifle. Additional ocular upgrades can include optic zoom and glare reduction. Treat cosmetic eyes and functional implants as separate catalog entries so a player can change appearance without replacing their installed cyberware.

Connect ocular implants to the shared cyberware catalog used by Nette, with stable item IDs, slot and capacity rules, prices, and optional compatibility adapters. Define toggle behavior, balance, and prerequisites. Prototype the night-vision filter, hostile marking, and sniper-scope changes in game before committing them as guaranteed features; provide a clear fallback or mark an effect unsupported if the required game hooks are unreliable. The clinic and catalog remain available after rescue, and rescue/unlock state persists across saves.

## Comic-shop owner and in-game reader

Add a separate authored hostage rescue for a comic-shop owner. Once rescued, they open a persistent comic shop in the outskirts with comic covers displayed on bookshelf props. Selecting a book opens a custom in-game comic viewer.

The mod already includes a comic-related readable shard in the base game, **Dr. Havoc & Radon**, but that is not a full comic PDF or an existing in-game comic-reader library. Use it only as an in-world reference; do not extract or redistribute the game's shard or assets.

The starter shelf should include the user's original **Last Instinct — Issue 1** once its final PDF is available, plus online comics with verified redistribution rights. **Sharing Creative Works: An Illustrated Primer** is a public-domain comic with a downloadable PDF. Keep author credit and source/license metadata with it. Follow the detailed [comic store and reader plan](comic-store-plan.md).

Prepare approved PDFs during mod packaging by converting pages into optimized textures and generating a manifest and cover thumbnails. Use the custom UI to page through them; test the widget and resource loading in-game. Do not assume the game can render PDFs directly. Only bundle files with clear rights to redistribute and convert.

## Arcade venues

Once V rescues the separate adult arcade-owner hostage, the owner can open several arcades across Night City. Add one or more venues in the outskirts as those districts become available. Keep these commercial locations and unlock state distinct from Josiah's friendly kid-gang hideout. Reuse Trauma Drama and Roach Race through native cabinet interactions only when supported and tested. The arcade network's catalog should grow to at least ten original, free-to-play games, including maze-chase, falling-block, flying games, and other distinct arcade genres. Use original names and presentation; record licensing and attribution for any optional third-party content. See the [arcade network plan](arcade-network-plan.md).

## Random hostile building activities

The outskirts has its own pool of hostile building activities. As V explores and receives local leads, select from authored, hand-built locations and encounter variants across the region. Vary the building, gang, patrol layout, boss, loot, optional objectives, and hostage outcome while keeping mission-critical interiors and characters authored and reliable. Random selection chooses from prepared content; it does not procedurally invent arbitrary building geometry.

Some locations may connect to tunnels, rail lines, large basements, garages, or other extended spaces. Track each activity's selected state, completed objectives, unique rewards, and rescue outcomes in the save so reloads cannot reroll a run or duplicate rewards.

The captured police captain is a rare authored rescue target in one of these new building areas, with a clear quest path and persistent state. Do not make the captain's rescue a transient random roll that could prevent the police station from ever becoming usable.

## Captain's lead: the scrapyard and Scrapper network

After V rescues the police captain and unlocks the central station, the captain tells V about an injured old man stranded in a junkyard on the outskirts of the new city. The old man is known for finding useful equipment and vehicle parts.

Make the scrapyard a hostile rescue mission with multiple aggressive dogs roaming the yard. V must fight through the dogs and reach the hut in the middle, where the injured man cannot safely escape. He explains that three large automatic turrets mounted high on poles are offline and need power. A gang leader controlling the dogs is positioned below one of the turret poles and carries the power unit. V must defeat the leader, recover the unit, and restore power to all three turrets.

Once powered, the turrets take out the remaining hostile dogs and other hostile intruders that enter the scrapyard. Their targeting must exclude V, rescued people, civilians, and recruited allies. The encounter should have clear turret arcs, safe routes, readable activation feedback, and fail-safe behavior if a turret cannot find a valid target.

Rescuing the old man unlocks him as the first Scrapper vendor. He contacts his Scrapper friends, making additional non-hostile Scrapper NPCs appear at authored outskirts locations. Their inventories draw random selections from Hidden Depths guns and vehicle parts. Persist each vendor's current stock and refresh timing so saving and reloading does not reroll purchases or duplicate items.

Scrapper vehicle parts are upgrade modules for cars and bikes added by Hidden Depths. Possible parts include engine/speed upgrades, added armor, and hood-mounted weapons. Give each part a defined compatible vehicle/slot list, balanced stats, installation/removal flow, and save-persistent ownership and configuration. Do not promise compatibility with every base-game or third-party vehicle unless it has been explicitly tested.

## Gangs and encounter pools

Bring the Hidden Depths factions into the outskirts' appropriate encounter pools. A hostile faction already discovered through its required hostile building encounter may appear in suitable city locations. A hostile faction that has not yet been discovered must first be introduced through an authored hostile building encounter; only after that encounter should it join real-world hostile pools, including eligible outskirts building activities. Persist each faction's unlock state so reloads do not change it.

The outskirts can also introduce new region-specific factions, with authored leaders and introduction missions. Keep their city appearances gated by the same discovery rule. Define their identities, number, and tactics during the faction design milestone.

Josiah's kid gang remains friendly social content: it can appear in suitable safe or civilian spaces and support information or story events, but never joins hostile combat pools or the random building combat encounters. The arcade-hideout revelation remains tied to Josiah's rescue and story.

## Characters, services, and quests

Develop local characters with clear roles and persistent story states. New fixers can provide a local job board, while new ripperdocs can operate clinics and offer compatible cyberware services. Include vendors, shopkeepers, allies, quest givers, police staff, and faction leaders as the region's content grows. Nette, Josiah, and the rescued shop owner may connect to the region where appropriate, while preserving their established rescue prerequisites and character-specific features.

After the station captain is rescued, the police station can become a usable hub through its planned interactions and services. Define those services in the quest and systems design, and make their availability depend on the captain rescue flag.

Use authored quest templates and location-specific variations for repeatable work. Keep mission-critical NPCs and hostage states out of arbitrary randomization. Save quest progress, faction discoveries, service unlocks, unique rewards, and rescue outcomes independently.

## Allies and partners

Add original local allies who can be recruited after their rescue or quest introduction. Aim for an immersive companion feature set inspired by [Night City Allies — Immersive Companion System](https://www.nexusmods.com/cyberpunk2077/mods/27625): invite allies to hang out, form a combat squad, call unlocked companions through an in-game phone/contact flow, have them follow and fight beside V, and provide supported interaction, command, outfit, equipment, and persistence options. Where practical, allow allies to visit or stay at suitable apartments and interact with selected safe locations.

Implement Hidden Depths characters and assets independently. Do not copy the referenced mod's code or assets. If optional integration is feasible, use only documented compatibility hooks and respect the other author's permissions; otherwise provide a standalone Hidden Depths companion system. Keep companion count, combat balance, navigation, and save reliability within the tested game limits.

At least two eligible rescued adult characters may offer optional partner/romance storylines. A character with a partner storyline can also be recruited as an ally, but partnership and squad recruitment are separate player choices. Add a mod-weapon-compatible equipment/loadout system for every new NPC archetype, including rescued specialists, allies, and partners. Give NPCs role-appropriate default loadouts; when recruited or in combat, eligible allies and partners can be assigned Hidden Depths weapons V has discovered, with matching ammunition and tested animations/behavior. Keep custom weapon use discovery-gated where appropriate, preserve quest-critical states, and do not force civilian service NPCs to carry weapons in peaceful scenes.
 
## World-building approach

Cyberpunk world-editing tools document adding native world edits and new structures; the World Builder workflow exports edits into WolvenKit. Use the [world-editing guide](https://wiki.redmodding.org/cyberpunk-2077-modding/modding-guides/world-editing) and [World Builder guide](https://wiki.redmodding.org/cyberpunk-2077-modding/modding-guides/world-editing/object-spawner) when starting this milestone.

Treat the city as a major map project: build a small vertical slice first, verify the road tunnel connection and loading boundary in-game, then expand streets and interiors in authored sectors. Confirm the supported game patch and toolchain before committing to map size or seamless streaming.

## Staged build sequence

1. Prove the blocked tunnel route, quest-controlled truck removal, and one small city block, including streaming, return travel, and save/reload.
2. Establish the city geography, districts, road network, boundaries, and performance budget.
3. Add the central inactive police station and its captain-rescue unlock state.
4. Add the first hub, local NPCs, and a small set of interiors; test navigation and crowd behavior.
5. Add the main quest arc, side activities, local fixers, clinics, vendors, the comic shop/reader, and their persistent unlocks.
6. Build the authored hostile-building and eligible hostage-character pools, including the captain rescue and ocular doctor rescue, and test selection and save behavior.
7. Add gang introduction missions, leaders, and faction-pool integration with building-first discovery gating.
8. Add the captain's scrapyard lead, dog encounter, three-turret power objective, and Scrapper vendor unlock.
9. Add Scrapper stock rotation and installable vehicle-part upgrades for Hidden Depths cars and bikes; test stats, targeting, purchases, and save persistence.
10. Add the eye clinic, cosmetic eye catalog, and ocular implant prototypes; integrate supported items with the shared cyberware registry.
11. Add recruitable allies, companion interactions, and optional adult partner storylines; test persistence and combat balance.
12. Expand the map with more districts, underground spaces, garages, rewards, and repeatable contracts.
13. Run compatibility, save migration, streaming, performance, and full quest regression passes before packaging.

## Test plan

- Verify the tunnel stays blocked before Nette's lead and opens only after the truck-removal objective; test both directions afterward.
- Check the tunnel quest lead, objective, and cleared state across save/reload and after unrelated missions.
- Verify map boundaries, player position, vehicle state, mission state, and save/reload at both ends.
- Confirm the central police station is visible but unusable before the captain rescue, and its planned services unlock only after the rescue.
- Check traffic and NPC navigation, collision, lighting, occlusion, and performance across the city sectors.
- Test random building selection, fixed authored geometry, encounter variation, eligible hostage rescues, captain rescue persistence, and one-time rewards.
- Verify rescued specialists return to the intended shop, clinic, fixer hub, or social location; test companion recruitment, phone/contact summon, follow/combat behavior, commands, outfits/equipment, apartment interactions, and save persistence.
- Confirm at least two eligible rescued adult NPCs support optional partner stories and can independently be recruited as allies; test custom weapon loadouts and ammunition for every mod-added combat-capable NPC type, including partners.
- Check relationship paths are optional, adult-only, choice-driven, and separate from ally recruitment.
- Confirm gangs enter regional pools only after their required hostile building introduction; verify the friendly kid gang stays out of combat pools.
- Test the captain-to-scrapyard quest chain, aggressive dog encounter, gang leader power-unit drop, three-turret activation, and safe target filtering for V and friendly NPCs.
- Test the eye doctor rescue and clinic unlock, eye color/tint/iris/robotic appearance choices, ocular cyberware slots and capacity, night vision, hostile tracking, and sniper enhancement on supported weapons.
- Test the comic-shop hostage unlock, bookshelf covers, PDF-to-page asset build, license manifest, reader navigation, page readability, and package-size limits.
- Verify Scrapper vendors unlock only after the old man's rescue; test randomized stock persistence, purchase behavior, and vehicle-part compatibility, installation, removal, and stats.
- Test fixers, clinics, shops, quest progression, services, unique rewards, and save/reload persistence.
- Confirm existing Night City routes and quests remain unaffected.
