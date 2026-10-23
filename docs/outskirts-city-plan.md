# Future Outskirts City Expansion

**Created by Bitsbb01 — Night City: Hidden Depths**

This is a DLC-sized post-launch expansion plan, not an implemented map. The goal is a substantial, coherent new region with its own cast, quest content, services, factions, and replayable activities—not just an empty map extension.

## Player route and region

Add a new explorable city on Night City's outskirts. V reaches it by driving through a selected existing road tunnel; the tunnel remains the visible road connection between the two places. The transition should feel like a continuous trip, using world streaming or a short concealed transition only if the engine requires it.

The destination is a distinct small city area with a recognizable center, connected streets, named districts, and a range of points of interest. Its final size, name, districts, and story remain open for later design. Build a compact, polished slice first, then expand the region in authored sectors.

## DLC-sized content goals

Treat the region as a full expansion with a connected set of activities and characters:

- Add a new local NPC cast: residents, workers, vendors, allies, quest contacts, and faction members, with original appearances and dialogue.
- Give the region its own fixer network, including new fixers who offer authored main and side jobs plus repeatable contracts.
- Add new ripperdocs and clinics that provide services and support Hidden Depths cyberware. Nette may establish a clinic here if it fits the final story and location plan.
- Build shops and other social hubs, including space for future rescued shop-owner characters.
- Create a main quest arc, side jobs, rescue events, and optional activities that make the region feel connected to the wider Hidden Depths storyline.
- Add a varied set of accessible interiors, underground routes, service tunnels, garages, and other points of interest.
- Add traffic, pedestrians, ambient encounters, and appropriate faction activity across the region.
- Place new gear and rewards through authored activities, while using existing game loot where it fits.

The intended scale is several substantial districts and a meaningful quest/activity set. Exact mission count and map size should be set after the first in-game slice proves the toolchain and performance budget.

## Gangs and encounter pools

Bring the Hidden Depths factions into the outskirts' appropriate encounter pools. A hostile faction already discovered through its required hostile building encounter may appear in suitable city locations. A hostile faction that has not yet been discovered must first be introduced through an authored building encounter; only after that encounter should it join real-world hostile pools. Persist each faction's unlock state so reloads do not change it.

The outskirts can also introduce new region-specific factions, with authored leaders and introduction missions. Keep their city appearances gated by the same discovery rule. Define their identities, number, and tactics during the faction design milestone.

Josiah's kid gang remains friendly social content: it can appear in suitable safe or civilian spaces and support information or story events, but never joins hostile combat pools or the random building combat encounters. The arcade-hideout revelation remains tied to Josiah's rescue and story.

## Characters, services, and quests

Develop local characters with clear roles and persistent story states. New fixers can provide a local job board, while new ripperdocs can operate clinics and offer compatible cyberware services. Include vendors, shopkeepers, allies, quest givers, and faction leaders as the region's content grows. Nette, Josiah, and the rescued shop owner may connect to the region where appropriate, while preserving their established rescue prerequisites and character-specific features.

Use authored quest templates and location-specific variations for repeatable work. Keep mission-critical NPCs and hostage states out of arbitrary randomization. Save quest progress, faction discoveries, service unlocks, unique rewards, and rescue outcomes independently.

## World-building approach

Cyberpunk world-editing tools document adding native world edits and new structures; the World Builder workflow exports edits into WolvenKit. Use the [world-editing guide](https://wiki.redmodding.org/cyberpunk-2077-modding/modding-guides/world-editing) and [World Builder guide](https://wiki.redmodding.org/cyberpunk-2077-modding/modding-guides/world-editing/object-spawner) when starting this milestone.

Treat the city as a major map project: build a small vertical slice first, verify the road tunnel connection and loading boundary in-game, then expand streets and interiors in authored sectors. Confirm the supported game patch and toolchain before committing to map size or seamless streaming.

## Staged build sequence

1. Prove the tunnel route and one small city block, including streaming, return travel, and a safe save/reload.
2. Establish the city geography, districts, road network, boundaries, and performance budget.
3. Add the first hub, local NPCs, and a small set of interiors; test navigation and crowd behavior.
4. Add the main quest arc, side activities, local fixers, clinics, vendors, and their persistent unlocks.
5. Add gang introduction missions, leaders, and faction-pool integration with building-first discovery gating.
6. Expand the map with more districts, underground spaces, garages, rewards, and repeatable contracts.
7. Run compatibility, save migration, streaming, performance, and full quest regression passes before packaging.

## Test plan

- Drive both directions through the tunnel from multiple approaches and at different speeds.
- Verify map boundaries, player position, vehicle state, mission state, and save/reload at both ends.
- Check traffic and NPC navigation, collision, lighting, occlusion, and performance across the city sectors.
- Confirm gangs enter regional pools only after their required hostile building introduction; verify the friendly kid gang stays out of combat pools.
- Test fixers, clinics, shops, quest progression, services, unique rewards, and save/reload persistence.
- Confirm existing Night City routes and quests remain unaffected.
