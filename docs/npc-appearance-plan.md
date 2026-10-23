# Mod-Added NPC Appearance Plan

**Created by Bitsbb01 — Night City: Hidden Depths**

This is a future-version design plan for the appearance options used by characters added by Night City: Hidden Depths.

## Original appearance library

Create original appearance presets for the mod's hostages, fixers, shop owners, ripperdocs, vehicle specialist, gang members, and mutant enemies. Include new:

- Eye colors and exotic eye looks
- Tattoos and makeup
- Scars and other facial details
- Hairstyles and nail styles where appropriate for the character

Give important characters distinct combinations so they remain recognizable. Make sure custom appearances have a safe fallback if an optional appearance mod is absent.

## Optional compatibility: Beautiful Exotics Eyes Pack

The linked [Beautiful Exotics Eyes Pack — CCXL Version](https://www.nexusmods.com/cyberpunk2077/mods/25718) adds 39 eye colors to character creation and lists ArchiveXL and TweakXL as requirements. Its creator's Nexus permissions prohibit reupload and require permission for asset use.

Plan two compatible paths:

1. Create original exotic eye looks for Hidden Depths NPCs so they work without other appearance mods.
2. Optionally detect and use eye options from the player's installed CCXL pack on Hidden Depths NPCs if the pack exposes compatible appearance IDs and in-game tests confirm NPC assignment works.

Do not bundle, rehost, modify, or copy the pack's assets without the author's permission. Treat the pack as an optional dependency; it must not be required for the mod's NPC appearance library to work.

## Integration and testing

- Keep appearance references optional and isolated from quest logic.
- Verify missing or changed appearance IDs fall back to a Hidden Depths original preset.
- Test custom NPCs with no cosmetic mods installed and with the eye pack installed.
- Verify all added appearance variants load on each supported body type and do not replace the player's existing appearance options.
- Check asset permissions before including any third-party files in a release.
