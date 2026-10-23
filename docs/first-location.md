# First Location: The Quiet Track

**Created by Bitsbb01 — Night City: Hidden Depths**

This is the first-location build target. It is a content and pacing specification; the in-game sector, props, navigation, encounters, and quest files still need to be authored and tested against Cyberpunk 2077.

## Location premise

An abandoned freight-services building in Watson has two sealed entrances. One leads to a small, defensible safehouse. The other descends into a gang-run salvage operation that has expanded through old utility tunnels and a decommissioned rail spur.

The exact building and coordinates must be chosen from the installed game world in WolvenKit before implementation, so the new door connections align with real geometry and do not cut through active story spaces.

## Entry points

### East entrance: safehouse

A discreet entrance opens to a compact room with:

- Weapon storage access
- A usable bed
- A computer with local messages and location clues
- A locked internal door to the hostile side, opened from this side after the first clear

The safehouse stays available after it is unlocked and does not reset with encounter randomization.

### Freight entrance: hostile route

A separate loading entrance descends to the salvage crew's basement. The route should feel like a believable expansion from the surface building into the city's infrastructure.

## Pacing target

Target: around 20–25 minutes for a first blind run. Optional exploration can extend it.

| Segment | Approx. time | Gameplay |
| --- | ---: | --- |
| Approach and entry | 2–3 min | Read a shard or local message; choose the quiet freight entrance or investigate the safehouse access |
| Loading basement | 3–4 min | First gang patrol, camera/security option, loot and evidence |
| Utility level | 4–5 min | Multiple rooms, a locked shortcut, alternate route through a flooded service corridor |
| Rail tunnel | 5–7 min | Long traversal, cover-based combat, a side room with supplies, optional power restoration |
| Salvage platform | 4–5 min | Main gang group and lieutenant; encounter composition varies by run |
| Exit and aftermath | 2–3 min | Open a return route, resolve objective, collect optional rewards |

Times are a pacing estimate, not a guaranteed completion time.

## Objectives and repeat visits

The initial side activity should have a repeatable core objective such as recovering a data shard or disabling a gang salvage relay. Each run selects from authored encounter variants while preserving the same navigable geometry.

Potential run variations:

- Gang group and lieutenant selection
- Patrol positions and camera states
- Locked door or powered shortcut
- Optional stash location
- Reward container contents
- Mutated experiment encounter on selected variants

The 5% hostage event is rolled once when a new run is generated. If selected, a captive appears in a marked rail-side holding room. Candidate captives include a civilian or captured officer. The vehicle painter is a rare, one-time special rescue, tracked in the save; rescuing him unlocks his persistent garage and paint service. Story-critical named characters are excluded unless their story state is explicitly safe.

## Layout principles

- Keep the freight entrance and safehouse entrance distinct and easy to understand.
- Give the main basement at least two combat approaches after the first level.
- Build readable landmarks across the tunnel: signal lights, numbered service doors, a collapsed platform, and the salvage crane.
- Provide a route back to the surface after the finale; do not force a fast-travel exit.
- Keep the hostage room away from unavoidable splash damage and explosive props.
- Place optional loot off the critical path, including ammunition compatible with weapons found in the complex.
- Test NPC navigation and combat cover in every encounter variant.

## Milestone acceptance criteria

The first location is ready for a playable test only when:

- The player can enter both routes from the city without clipping through geometry.
- Safehouse storage, bed, and computer interactions work and persist.
- The hostile route forms a connected multi-level space with reliable navigation and a clear exit.
- The core side activity completes and does not repeat already claimed one-time rewards.
- The 5% hostage event is tested across seeded outcomes and remains stable when reloading a save.
- A clean install produces no quest softlocks or crashes on the declared game version.
