# Version and Release Plan

**Created by Bitsbb01 — Night City: Hidden Depths**

This plan sets the release order: finish and test the first playable version, then add the larger feature set in compatible, downloadable updates until the agreed scope is implemented. Version numbers below are provisional and may shift as game testing reveals scope or compatibility work.

## Release rule

Each public version must be an installable, tested build with a matching GitHub ZIP. Do not label a design document, content definition, or empty package as a playable release. Keep each release save-safe, document dependencies and upgrade notes, and test the published ZIP in a clean install profile.

The project can move into a new feature milestone when the previous milestone's acceptance checks pass. A broad feature remains marked planned until its in-game implementation and tests are complete.

## Version sequence

### Version 1.0 — The Quiet Track: first playable release

Build one complete Watson location as the stable foundation:

- Two distinct entrances, including a persistent safehouse with weapon storage, bed, and computer.
- An authored hostile basement and connected tunnel/rail route targeting about 20 minutes of first-run play.
- One complete side activity, enemies, basic loot/ammunition, objective interactions, and a reliable exit.
- Stable save/reload behavior, tested navigation, and a clean installable ZIP for a declared game version.

Keep the outskirts city and large future systems out of this first release. The goal is a small, polished, testable mod that proves the content and packaging pipeline.

### Version 1.1 — Replayable locations and rescue events

Add authored encounter variants, stable random run selection, the existing rare hostage-event chance, captive variants, and the first special rescue rewards. Add more prepared building sites only after the first location remains stable across saves.

### Version 1.2 — Gear, mutations, and faction behavior

Add original weapons and matching ammunition, clothing/armor, cyberware, mutated enemy variants, and Badge Roulette as a one-time-per-save reward. Add custom weapons to suitable enemy loadouts after V discovers them, with persistence and combat tests.

### Version 1.3 — Garages, vehicles, and stores

Add claimable cars or bikes, supported custom vehicle variants, the rescued painter and paint app, and the rescued shop owner. Add the Virtual Atelier store and discovery-gated entries where its current interfaces support the content.

### Version 1.4 — Josiah and the gang network

Add Josiah's rescue, fixer jobs, friendly arcade gang and hideout, and at least six hostile gangs with leaders. Unlock hostile world encounters only after each gang's authored hostile building introduction. Add original looks and test that the friendly kid gang stays outside combat pools.

### Version 1.5 — Nette and the companion-ready NPC foundation

Add Nette's rescue, clinic, cyberware catalog, and six-day hair/nail cycle. Establish the NPC equipment/loadout framework and companion foundation needed by the outskirts story. Validate optional cross-mod integrations and keep unsupported mods from breaking the base package.

### Version 2.0 — Outskirts city: first playable district

Make the city discoverable only after Nette's lead and the quest-cleared truck blockage in the road tunnel. Add a tested tunnel route and first district, local cast and main activity, the central police station in its locked/inactive state, and an authored hostile building rescue for the captain. Unlock the station only after the captain rescue. Package the city as a significant expansion while retaining Night City content compatibility.

### Versions 2.1 and later — Outskirts expansion waves

Expand district by district, adding authored hostile building pools, underground and rail spaces, local fixers, ripperdocs, clinics, shops, quests, gangs, leaders, hostages, loot, garages, and ambient NPCs. After the police-captain rescue, add the junkyard mission: rescue an injured old man from aggressive dogs, retrieve the gang leader's turret power unit, activate three pole-mounted turrets, and unlock the Scrapper vendor network. Add randomized mod-weapon and vehicle-part stock, including tested speed, armor, and hood-weapon upgrades for Hidden Depths cars and bikes.

Add multiple eligible rescued adults with optional partner storylines; those characters can separately join V as allies. Complete companion interactions, phone/contact summoning, follow and combat behavior, commands, gear controls, and save persistence. Equip every mod-added combat-capable NPC—including gangs, allies, and partners—with compatible loadouts for the new weapons V has discovered. Keep peaceful service NPCs in role-appropriate noncombat scenes.

Continue releases until the planned city, character, faction, rescue, equipment, and companion features have passed in-game tests. Keep a feature checklist and mark items complete only when verified in the game.

## Acceptance gate for each release

- Content validation and automated tests pass.
- Install and remove the ZIP in a clean profile using the documented dependencies.
- Test new and existing saves, save/reload during quests, persistent rewards, and prior-release save migration.
- Test the declared Cyberpunk 2077 patch and record known compatibility limits.
- Check crashes, softlocks, NPC navigation, combat behavior, balance, and performance for the features added in that version.
- Publish the ZIP only after the build contains actual installable game files and passes the release workflow.

## Current starting point

The repository currently contains design and content validation scaffolding, but no playable world, quest, NPC, item, or script payload under game-root/. Version 1.0 therefore has not been built or released yet. It needs authored game content and in-game testing before later version milestones can begin.
