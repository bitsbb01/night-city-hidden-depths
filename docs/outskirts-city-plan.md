# Future Outskirts City Expansion

**Created by Bitsbb01 — Night City: Hidden Depths**

This is a large post-launch world expansion plan, not an implemented map.

## Player route

Add a new explorable city on Night City's outskirts. V reaches it by driving through a selected existing road tunnel; the tunnel remains the visible road connection between the two places. The transition should feel like a continuous trip, using world streaming or a short concealed transition only if the engine requires it.

The destination is a distinct small city area, not just another interior. Its size, name, districts, and story are open for later design.

## Content goals

- Create a recognizable city center and connected streets for exploration and driving.
- Add original points of interest, accessible interiors, shops, and side activities.
- Extend the gang and faction storylines into the outskirts after their introduction in Night City.
- Place authored routes, encounters, traffic, pedestrians, and clear ways back through the tunnel.
- Keep any new hostile faction gated by the existing building-first discovery rule.

## World-building approach

Cyberpunk world-editing tools document adding native world edits and new structures; the World Builder workflow exports edits into WolvenKit. Use the [world-editing guide](https://wiki.redmodding.org/cyberpunk-2077-modding/modding-guides/world-editing) and [World Builder guide](https://wiki.redmodding.org/cyberpunk-2077-modding/modding-guides/world-editing/object-spawner) when starting this milestone.

Treat the city as a major map project: build a small vertical slice first, verify the road tunnel connection and loading boundary in-game, then expand streets and interiors in authored sectors. Confirm the supported game patch and toolchain before committing to map size or seamless streaming.

## Test plan

- Drive both directions through the tunnel from multiple approaches and at different speeds.
- Verify map boundaries, player position, vehicle state, mission state, and save/reload at both ends.
- Check traffic and NPC navigation, collision, lighting, occlusion, and performance across the city sectors.
- Confirm existing Night City routes and quests remain unaffected.
