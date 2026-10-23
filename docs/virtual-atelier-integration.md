# Virtual Atelier Integration Plan

**Created by Bitsbb01 — Night City: Hidden Depths**

This is a future-version design plan. It describes store integration; it is not an implemented store or cosmetic system.

## What the integration does

Virtual Atelier is a shop framework: it lets modders register in-game stores for items that the mod already defines. It does not create clothing, weapons, tattoos, or makeup assets by itself. The [official Cyberpunk modding guide for Atelier stores](https://github.com/CDPR-Modding-Documentation/Cyberpunk-Modding-Docs/blob/main/modding-guides/items-equipment/adding-new-items/adding-items-atelier-integration.md) explains store registration and its dependency requirements. The [Virtual Atelier mod page](https://www.nexusmods.com/cyberpunk2077/mods/2987) describes its item shop and preview features.

The release must declare Virtual Atelier and its required frameworks as dependencies if the store integration needs them. Confirm the supported versions against the selected game patch before release.

## Hidden Depths store

Create a uniquely named **Night City: Hidden Depths** store. Add eligible gear only after V has found it in one of the buildings:

- Hidden Depths clothing and armor
- Hidden Depths weapons
- Compatible supported equipment added by future releases

The discovery flag unlocks the item for purchase in the store. Keep each item ID unique, use explicit price and quality data, and avoid duplicate store IDs or duplicate entries. Do not expose undiscovered rewards in the store.

## Makeup and tattoo content

Create original makeup and tattoo appearance options as mod assets and cosmetic unlocks. Test whether each cosmetic can be represented as a Virtual Atelier purchase entry on the supported game/framework versions. If a makeup or tattoo option is an appearance setting rather than a normal item record, offer it through a compatible appearance menu or a small companion cosmetics screen linked from the Atelier store.

Virtual Atelier should not be treated as the system that creates or applies cosmetic appearances; the mod needs the required assets and appearance behavior separately.

## Save state and compatibility

- Store discovered-item unlocks in save state so the store catalog remains consistent after reload.
- Show purchased items using Virtual Atelier's ownership behavior where available.
- Check for required item records, frameworks, store IDs, localization, and preview assets before registering entries.
- Keep the core building and loot features functional when Virtual Atelier is not installed; disable only the optional store integration and explain the missing dependency.
- Do not copy, replace, or redistribute third-party item assets. Register only item records provided by the player's installed mods or this project, subject to their permissions.

## Test plan

- Find each eligible weapon, clothing, or armor reward and verify it becomes available in the store only afterward.
- Check that undiscovered rewards remain hidden and reload preserves discovery state.
- Test item purchase, ownership indication, and preview where supported.
- Test makeup and tattoos through the supported appearance workflow, including a fallback if they cannot be sold as ordinary item entries.
- Test with Virtual Atelier installed, without it, and with supported dependency versions.
- Verify unique store and item IDs and report missing dependencies cleanly.
