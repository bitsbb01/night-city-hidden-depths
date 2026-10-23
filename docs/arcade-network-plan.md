# Arcade Owner and Playable Arcade Network

**Created by Bitsbb01 — Night City: Hidden Depths**

This is a future-version design plan, not an implemented feature. The repository does not yet contain a playable game mod.

## Rescue and unlock

Add a distinct adult arcade owner as an eligible hostage in the authored rescue pool. After V rescues them, they return to the normal world and open several arcade venues across Night City and, once available, the outskirts city. Track the rescue and venue unlock in save data, prevent duplicate rescues, and keep this character separate from Josiah and the friendly kid gang.

Each venue should have accessible cabinets, signage, a service counter or owner interaction, ambient NPCs where feasible, and a small location-specific layout. Use the venues to provide repeatable casual activities and optional high-score rewards, not to block main-story progression.

This commercial arcade network is separate from the kid gang's old-building hideout, which is revealed through Josiah's story and remains friendly social/exploration content.

## Cabinet catalog

### Existing Cyberpunk games

CD PROJEKT RED's Night City guide identifies functioning **Trauma Drama** and **Roach Race** arcade cabinets in the base game. The mod should make those existing games available at its new venues by using the game's own cabinet interactions or supported activation hooks. Reuse the installed game's game logic and assets; do not copy or redistribute them in the mod package.

Prototype the interaction first. If the supported game patch exposes no reliable way to start a built-in minigame from a mod-added cabinet, keep the native cabinets as decoration and document the limitation until a safe integration is possible. Do not claim an existing game is playable at every new venue until verified in game.

### New classics-inspired games

Build **at least ten** cabinet games ourselves as original, free-to-play minigames for this mod. They will have original names, code, graphics, sounds, and scoring, so the core arcade catalog will not depend on obtaining third-party games or licenses. The first catalog should include these distinct game types:

- **Maze chase** — a Pac-Man-like maze game with original character designs, maze layouts, sounds, and name.
- **Falling blocks** — a Tetris-like block-stacking puzzle with original shapes, UI, scoring, and name. Do not use the Tetris name, logo, or protected visual/audio presentation.
- **Retro first-person maze shooter** — a small retro maze shooter using original code and original content; it should not use Doom branding or assets.
- **Skyline Ace** — an original side-view flying game with flight lanes, obstacles, and rescue or delivery objectives.
- **Neon Runway** — an original overhead flight-dodging game with fuel and score pickups.
- **Scrapstorm** — an original arcade space-flight survival game with waves of debris and hostile drones.
- **Turbo Circuit** — an original top-down racing game with short tracks and lap records.
- **Byte Serpent** — an original grid-based growing-tail game.
- **Wallbreaker 2099** — an original paddle-and-brick game with power-ups.
- **Signal Beat** — an original rhythm and timing game using a new soundtrack.
- **Drone Salvage** — an original score-attack game about piloting a salvage drone through hazards.
- **Gridlock Tactics** — an original quick puzzle game with rotating routes and timed objectives.

All names and creative assets are working titles until checked against existing works. Keep their code, characters, levels, visuals, sound, UI, and scoring original; use familiar genres as high-level inspiration only. The optional Freedoom-content shooter has a separate licensing and technical review and is not required for the ten-game target.

A simple custom UI game is the preferred first prototype. Do not launch arbitrary external executables from the game. Third-party free/open games may be optional additions only after checking the code and asset licenses. An embedded engine or renderer must be reviewed for game compatibility, platform support, dependencies, package size, and performance.

## Rights and packaging rules

“Freeware” or “free to play” alone does not grant redistribution rights. For each third-party game, codebase, engine, sound, font, and art asset, record the exact source/revision and applicable license in a package manifest. Confirm that redistribution, modification, in-game embedding, and any commercial use allowed by the mod's distribution model are covered. Include required attribution, copyright and license notices, source or offer-of-source obligations, and modifications as required by that license. Public-domain material can be included only after its status and provenance are documented.

Do not bundle copyrighted commercial arcade games or base-game minigame assets. For a game with split code and asset licenses, review both. If a dependency's requirements cannot be met, use original assets or omit that dependency.

## Save state and rewards

Persist each cabinet's unlocked/available game list and the player's best scores where the framework supports it. Rewards should be modest and optional: small eddies, a cosmetic token, or a one-time item. Save one-time reward flags to prevent score reload exploits and duplicate claims. High scores and venue access must survive saving and reloading.

## Implementation and test sequence

1. Build one arcade-room slice and verify cabinet placement, interaction, player exit, and save/reload.
2. Test how native Trauma Drama and Roach Race activations can be invoked at a mod-added venue on the supported game version.
3. Prototype one original 2D cabinet minigame with controller, keyboard, pause, exit, focus, input-lock, and accessibility checks.
4. Build the catalog in stages, reaching at least ten original playable games after the in-game runtime, controls, and score persistence are validated. Any optional third-party game or content pack gets a separate license and technical review.
5. Add the owner rescue and unlock several venues in Night City; add outskirts venues with the city expansion.
6. Test cabinet interactions, score persistence, rewards, performance, NPC navigation, and conflicts with other interaction mods.

## Verified references

- CD PROJEKT RED confirms Trauma Drama and Roach Race are playable at functioning arcade cabinets in Night City: <https://www.cyberpunk.net/en/news/50116/your-trip-to-night-city-best-entertainment>
- Freedoom's repository describes its content and publishes its license: <https://github.com/freedoom/freedoom> and <https://github.com/freedoom/freedoom/blob/master/COPYING.adoc>

