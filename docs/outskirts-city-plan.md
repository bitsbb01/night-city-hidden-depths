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
- Build shops and other social hubs, including space for future rescued shop-owner characters.
- Create a main quest arc, side jobs, rescue events, and optional activities that make the region feel connected to the wider Hidden Depths storyline.
- Add a varied set of accessible interiors, underground routes, service tunnels, garages, and other points of interest.
- Add traffic, pedestrians, ambient encounters, and appropriate faction activity across the region.
- Place new gear and rewards through authored activities, while using existing game loot where it fits.

The intended scale is several substantial districts and a meaningful quest/activity set. Exact mission count and map size should be set after the first in-game slice proves the toolchain and performance budget.

## Hostage and rescue character pool

Use the region's hostage events to introduce original local characters who can become part of the city after rescue. The possible captives can include shop owners, ripperdocs, fixers, adult sex workers/joytoys, local workers, residents, police officers, and other authored NPCs. A rescued character can return to the outskirts and open or join an appropriate service, offer jobs or information, become an ally, or contribute to a follow-up quest, depending on their role.

Keep the existing rare hostage-event chance and save rules. Choose only from authored, eligible characters; prevent duplicate rescues and avoid selecting a character whose quest state is unavailable. Maintain the police captain as a separate authored rescue required to activate the station, so random selection cannot block that unlock. All sex-worker characters and any potential romantic partners are adults. Use consensual, optional relationship storylines; rescuing someone never automatically creates a romance.

## Random hostile building activities

The outskirts has its own pool of hostile building activities. As V explores and receives local leads, select from authored, hand-built locations and encounter variants across the region. Vary the building, gang, patrol layout, boss, loot, optional objectives, and hostage outcome while keeping mission-critical interiors and characters authored and reliable. Random selection chooses from prepared content; it does not procedurally invent arbitrary building geometry.

Some locations may connect to tunnels, rail lines, large basements, garages, or other extended spaces. Track each activity's selected state, completed objectives, unique rewards, and rescue outcomes in the save so reloads cannot reroll a run or duplicate rewards.

The captured police captain is a rare authored rescue target in one of these new building areas, with a clear quest path and persistent state. Do not make the captain's rescue a transient random roll that could prevent the police station from ever becoming usable.

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

Some new adult characters may have optional partner/romance storylines in the outskirts. Treat relationship progression as separate from companion recruitment: consent and story choices determine romance, and the player can use allies as friends or squad members without pursuing a relationship. Preserve existing Cyberpunk 2077 character story states.
 
## World-building approach

Cyberpunk world-editing tools document adding native world edits and new structures; the World Builder workflow exports edits into WolvenKit. Use the [world-editing guide](https://wiki.redmodding.org/cyberpunk-2077-modding/modding-guides/world-editing) and [World Builder guide](https://wiki.redmodding.org/cyberpunk-2077-modding/modding-guides/world-editing/object-spawner) when starting this milestone.

Treat the city as a major map project: build a small vertical slice first, verify the road tunnel connection and loading boundary in-game, then expand streets and interiors in authored sectors. Confirm the supported game patch and toolchain before committing to map size or seamless streaming.

## Staged build sequence

1. Prove the blocked tunnel route, quest-controlled truck removal, and one small city block, including streaming, return travel, and save/reload.
2. Establish the city geography, districts, road network, boundaries, and performance budget.
3. Add the central inactive police station and its captain-rescue unlock state.
4. Add the first hub, local NPCs, and a small set of interiors; test navigation and crowd behavior.
5. Add the main quest arc, side activities, local fixers, clinics, vendors, and their persistent unlocks.
6. Build the authored hostile-building and eligible hostage-character pools, including the captain rescue, and test selection and save behavior.
7. Add gang introduction missions, leaders, and faction-pool integration with building-first discovery gating.
8. Add recruitable allies, companion interactions, and optional adult partner storylines; test persistence and combat balance.
9. Expand the map with more districts, underground spaces, garages, rewards, and repeatable contracts.
10. Run compatibility, save migration, streaming, performance, and full quest regression passes before packaging.

## Test plan

- Verify the tunnel stays blocked before Nette's lead and opens only after the truck-removal objective; test both directions afterward.
- Check the tunnel quest lead, objective, and cleared state across save/reload and after unrelated missions.
- Verify map boundaries, player position, vehicle state, mission state, and save/reload at both ends.
- Confirm the central police station is visible but unusable before the captain rescue, and its planned services unlock only after the rescue.
- Check traffic and NPC navigation, collision, lighting, occlusion, and performance across the city sectors.
- Test random building selection, fixed authored geometry, encounter variation, eligible hostage rescues, captain rescue persistence, and one-time rewards.
- Verify rescued specialists return to the intended shop, clinic, fixer hub, or social location; test companion recruitment, phone/contact summon, follow/combat behavior, commands, outfits/equipment, apartment interactions, and save persistence.
- Check relationship paths are optional, adult-only, choice-driven, and separate from ally recruitment.
- Confirm gangs enter regional pools only after their required hostile building introduction; verify the friendly kid gang stays out of combat pools.
- Test fixers, clinics, shops, quest progression, services, unique rewards, and save/reload persistence.
- Confirm existing Night City routes and quests remain unaffected.
