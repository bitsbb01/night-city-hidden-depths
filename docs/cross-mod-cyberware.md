# Cross-Mod Cyberware Integration Plan

**Created by Bitsbb01 — Night City: Hidden Depths**

This document defines the future integration layer for Nette's clinic. It is a design contract for implementation, not a currently working in-game feature.

## Goal

Nette's clinic should offer cyberware and compatible cybernetic upgrades from this mod and other cyberware mods installed by the player. The integration should read existing item definitions and add supported entries to her clinic catalog without editing or replacing another mod's files.

TweakXL provides a framework for changing TweakDB data and supports declarative tweaks and script extensions. The [TweakXL project](https://github.com/psiberx/cp2077-tweak-xl) and [Codeware project](https://github.com/psiberx/cp2077-codeware) are implementation references. Select exact framework versions only after the target game patch is established.

## Catalog interface

Normalize discovered items into a shared catalog entry with:

- Stable item record ID and owning mod ID, when available
- Display name and localization key
- Cyberware slot or equipment area
- Install and removal requirements
- Capacity/stat information needed to show the player what it does
- Price data, if available
- Required frameworks and compatibility status
- An explanation when the item cannot be offered safely

Use stable IDs for deduplication. Never rewrite another mod's item record as part of discovery.

## Integration layers

1. **Native definitions:** Include this mod's custom cyberware in the same catalog.
2. **Installed item discovery:** At runtime, inspect available cyberware definitions and register items that expose the fields needed for safe vendor and installation behavior.
3. **Optional adapters:** Add small compatibility adapters for popular cyberware frameworks or mods where their item definitions need special handling. Keep each adapter isolated so one incompatible mod cannot break the entire clinic.
4. **Validation and fallback:** Check slot, required records, installation data, and dependencies before exposing an item. Skip unsafe or incomplete entries and show the reason in a compatibility report.

The design goal is broad support for installed cyberware mods. Universal support cannot be promised for mods whose items do not expose usable definitions or require private behavior; those cases need an adapter or must be marked unsupported rather than causing broken installations.

## Nette clinic behavior

- Show all compatible catalog entries, grouped by slot and source mod.
- Distinguish base-game items, Hidden Depths items, and third-party mod items.
- Use available vendor pricing and install data. If required fields are absent, do not invent defaults that could corrupt equipment or progression.
- Refresh the catalog when the game loads so newly installed or removed mods are reflected.
- Preserve purchases and installed cyberware through save/reload.
- Keep Nette's rescue and clinic unlock independent from Josiah, the shop owner, and the vehicle painter.

## Test plan

Test the clinic with:

- No extra cyberware mods installed
- Several installed cyberware mods from different authors
- Duplicate item IDs or overlapping slot definitions
- Missing optional frameworks and required dependencies
- Items with incomplete localization, price, slot, or install data
- Save/reload before and after purchase and installation
- The game's current supported patch and documented framework versions

A failed adapter should disable only its own integration and report the affected mod/item IDs for troubleshooting.

## Related appearance schedule

Nette's hair and nail styles change independently every six in-game days. Persist each selected style and its next change day; catalog refreshes and save reloads must not reset that schedule.
