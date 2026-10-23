# Future Gangs and Josiah's Arcade Hideout

**Created by Bitsbb01 — Night City: Hidden Depths**

This is a future-version design brief for three new groups. It is not implemented in the current mod.

## Stealth gang

Add an adult hostile gang variant to appropriate random enemy pools. They specialize in silent weapons, stealth approaches, ambushes, flanking, and disappearing between cover. Use authored encounter options and weighted selection so they appear as a distinct, occasional threat rather than replacing every gang encounter.

Do not assign child NPCs to hostile gang loadouts.

## All-female gang

Add a separate gang whose members are all women. Give them their own identity, look, dialogue, combat roles, and equipment. Add them to appropriate hostile enemy pools and authored building encounters as a randomized gang option.

## Josiah's kid gang

This is a friendly, non-hostile child group focused on hiding, scavenging, and theft. The player first learns about them through Josiah after rescuing him. Before that reveal, children who belong to the group should not be identified to V as a gang or trigger a gang quest.

After Josiah reveals the group:

- Some child NPCs around the city can be identified as members through subtle clothing, dialogue, or behavior.
- They can help V with local information, distractions, finding hidden routes, or recovering small stolen items.
- Their hideout is a separate old building full of arcade machines, unlocked through a lead from Josiah.
- Their encounters are social/exploration content, not combat encounters.

### Safety and placement rules

- Never add the kid gang to the hostile enemy pool.
- Never spawn them in the new building areas' gang combat encounters.
- Keep child NPCs noncombatant and excluded from hostile faction changes, Badge Roulette effects, and enemy targeting.
- Keep their affiliation hidden until Josiah's reveal; save the reveal and hideout-unlocked state so reloads do not reset it.

## Random encounter and save behavior

The stealth gang and all-female gang are eligible for selected hostile encounter variants. Store the chosen group for an active run so saves do not reroll it. The kid gang uses a separate friendly-world and hideout system, gated by Josiah's rescue/reveal state.

Test the three groups separately, verify faction selection across reloads, and confirm the child group never appears in combat pools or hostile NPC targeting.
