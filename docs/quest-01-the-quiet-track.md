# Side Activity 01: The Quiet Track

**Created by Bitsbb01 — Night City: Hidden Depths**

Quest outline for the first Watson location. This is authored content for implementation; it is not yet an in-game quest file.

## Hook

After V reaches free roam in Watson, an unmarked data shard or a fixer message points to a freight-services building near an abandoned rail spur. A small crew has been stripping cargo and routing stolen cyberware through the old service tunnels.

The lead is optional. The player can investigate the building, discover the safehouse entry, or return later.

## Main objective

Recover the crew's route ledger and disable its salvage relay. The ledger identifies where stolen gear is being moved. The side activity can be completed by stealth, direct combat, or a mixture of both.

### Quest beats

1. **Find the freight building.** A short lead points to Watson without marking every entrance.
2. **Choose an entry.** The freight entrance leads directly into the hostile route. The side entrance leads to the safehouse room.
3. **Work through the lower levels.** Gather evidence, identify the gang's work, and choose whether to disable cameras or power.
4. **Reach the rail tunnel.** The route opens into the longer maintenance and track complex, with optional rooms and alternate approaches.
5. **Confront the salvage crew.** A lieutenant protects the relay. Encounter composition and selected enemy equipment vary by run.
6. **Recover the ledger and shut down the relay.** A terminal or physical relay provides the objective interaction.
7. **Open the return route.** Restore a freight lift or service gate so the player can exit without fast travel.

## Run variations

The location geometry and core objectives stay fixed so the player can learn the site. Each new run selects from authored options:

- Patrol path and starting positions
- Gang members and lieutenant archetype
- Camera and power states
- Optional stash placement
- Mutated experiment encounter: absent on common runs, present on selected variants
- Randomized compatible weapon, ammo, crafting component, and clothing drops

The system must record the active run so saving and reloading does not reroll enemies, the hostage result, or one-time rewards midway through a run.

## Rare hostage event

At the start of a new run, roll a 5% chance for a captive event. If it triggers, add a holding room off the rail tunnel and a rescue objective.

Possible captives:

- A civilian kidnapped for leverage
- A captured NCPD officer
- The one-time vehicle painter

The painter's appearance is a one-time special rescue. If he is not rescued on one run, the captive event may roll again on a later run. Once rescued, he moves to the persistent garage location and unlocks vehicle paint services. Store the rescue and service-unlocked state in the save so he is never duplicated.

The hostage must not be placed where splash damage or unavoidable gang fire can kill them before V can intervene. A stealth route should make it possible to reach the holding room unseen; a combat route should provide cover and a clear extraction path.

## Safehouse unlock

The safehouse entrance is initially discoverable from the street. The room can be entered during the first visit. After the relay is disabled, V can open the internal connection between the safehouse and the hostile floors.

Safehouse interactions:

- Weapon storage
- Bed with sleep/time-skip interaction
- Computer with crew notes and one new lead after the first clear

Safehouse state is persistent. The bed, storage, and computer continue to function after the randomized encounter resets.

## Rewards

- Regular run: eddies, standard weapon/ammo loot, and a variable cache.
- Hidden rooms: higher rarity gear or optional crafting materials.
- First clear: unlock the internal safehouse connection.
- Unique reward pool: Badge Roulette can appear once per save, never duplicated by reruns.
- Rare special hostage rescue: permanent vehicle painter and his workshop/app service.
- Later variants: custom weapons become eligible for selected gang loadouts after V discovers each weapon.

## Failure and replay rules

- Leaving before objective completion pauses the run state; returning should not create duplicate hostages or loot.
- Completing the core objective marks that run cleared and makes a new authored encounter variant eligible later.
- One-time quest rewards use persistent save facts.
- Badge Roulette and the painter cannot be awarded twice.
- If a captive dies, complete the location objective but do not grant the painter's service; the rare rescue can roll again on a future run.

## Content needed for in-game implementation

- Pick the final Watson building and verify both entrance connections in the game world.
- Build the connected lower floors, tunnel, rail spur, doors, cover, loot positions, and return route.
- Author the side-quest graph, journal entries, messages, interactions, reward flags, and encounter state.
- Add enemy loadouts and the rare captive variants.
- Test each route, randomized state, save/reload behavior, and the 5% event in-game.
