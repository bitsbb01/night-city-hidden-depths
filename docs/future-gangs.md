# Future Gangs and Josiah's Arcade Hideout

**Created by Bitsbb01 — Night City: Hidden Depths**

This is a future-version design brief for new groups. It is not implemented in the current mod.

## Hostile faction roster

Add at least six distinct hostile gangs:

1. A stealth gang that favors silent weapons, ambushes, flanking, and breaking contact.
2. An all-female gang with its own identity, appearance, dialogue, tactics, and equipment.
3. At least four additional hostile gang types, each with a distinct identity, combat style, equipment, appearance, and leader.

Give every hostile faction a leader and an authored leader encounter in one of the new buildings. Keep the gang names and detailed themes open for later design.

## Building discovery unlocks city encounters

Introduce each hostile faction in a building first. The first time V encounters one of its groups as hostile, set a persistent faction-discovered flag. After that, add that faction's members and occasional leader encounters to appropriate real-world city enemy pools.

Before the building encounter, that faction must not appear as a new hostile group in the open world. Save/reload must preserve the discovery state and the active encounter's selected faction. Weight the open-world spawns so the new groups add variety without replacing the existing gangs.

## Josiah's kid gang

This is a friendly, non-hostile child group focused on hiding, scavenging, and theft. The player first learns about them through Josiah after rescuing him. Before that reveal, children who belong to the group should not be identified to V as a gang or trigger a gang quest.

After Josiah reveals the group:

- Some child NPCs around the city can be identified as members through subtle clothing, dialogue, or behavior.
- They can help V with local information, distractions, finding hidden routes, or recovering small stolen items.
- Their hideout is a separate old building full of arcade machines, unlocked through a lead from Josiah.
- Their encounters are social/exploration content, not combat encounters.

### Safety and placement rules

- Never add the kid gang to the hostile enemy pool or to the new building areas' combat encounters.
- Keep child NPCs noncombatant and exclude them from hostile faction changes, Badge Roulette effects, and enemy targeting.
- Keep their affiliation hidden until Josiah's reveal; save the reveal and hideout-unlocked state so reloads do not reset it.

## Random encounter and save behavior

The six or more hostile factions share the building-first discovery rule, then become eligible for selected open-world encounters. Keep the kid gang on its own friendly-world and hideout system, gated by Josiah's rescue/reveal state.

Test faction discovery in each building, faction unlocks after save/reload, hostile leader encounters, and the open-world spawn weights. Separately verify that the kid gang never enters combat pools or hostile NPC targeting.
