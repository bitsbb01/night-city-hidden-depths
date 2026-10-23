# Future Comic Store and Reader

**Created by Bitsbb01 — Night City: Hidden Depths**

This plan adds a rescued comic-shop owner and an in-game store where V can browse shelves and read bundled comics.

## Hostage and store unlock

Add an authored hostage rescue for a comic-shop owner in an outskirts hostile building. When rescued, the owner establishes a persistent comic shop in the new area. Store rescue and shop unlock state in the save, prevent duplicate versions of the NPC, and keep the shop inventory persistent.

The shop displays comic front covers on bookshelf props alongside other comics. Interacting with a displayed comic opens its entry in the store's comic catalog.

## Comic viewer

The catalog should read any compatible comic PDF included in the mod's build input. The game runtime is not assumed to render PDF files directly. During packaging, convert each licensed PDF into optimized page image assets and generate a manifest with the title, author, cover thumbnail, page order, source, and license. The store UI then displays each cover and opens a paginated comic viewer with next/previous page, close/return-to-store, and readable page scaling.

Use a custom UI widget and loaded image resources. Cyberpunk modding documentation describes loading custom resources and UI widgets through ArchiveXL; a small in-game prototype must verify page rendering, input, memory use, and performance on the supported patch before the full library is packaged.

The build tool should reject files without a recorded rights status, validate the PDF and page count, and generate low-resolution thumbnails plus reader-sized pages to keep the game package manageable. Keep an offline copy of each original PDF in project source only when distribution rights allow it.

## Starter shelf and rights

The base game has a readable comic-related data shard titled **Dr. Havoc & Radon**, but this is not a complete multipage comic PDF or a ready-made comic-store library. Reference the in-world title in shop dialogue or shelf dressing if appropriate; do not extract or redistribute game assets or shard text as a PDF.

Initial reader content:

- **Last Instinct — Issue 1**, the user's original zombie comic, once the final PDF is available for the mod package.
- **Sharing Creative Works: An Illustrated Primer**, by Alex Roberts, Rebecca Rojer, and Jon Phillips. Creative Commons states this comic is dedicated to the public domain and provides a downloadable PDF. Keep its credit and rights note in the manifest, and do not imply Creative Commons endorsement of the mod.

Additional online comics may be added only after checking the specific work and edition's redistribution license. "Free to read" alone is not permission to bundle a PDF. Prefer public-domain, CC0, or licenses that explicitly allow redistribution and any needed conversion. Keep source links, author credits, license text, and required attribution with each title. Avoid titles with unclear scan rights, third-party elements, noncommercial restrictions that conflict with distribution, or no-derivatives terms that would block page conversion.

## Acceptance tests

- The rescued shop owner appears once, establishes the shop, and remains available after save/reload.
- Comic covers appear on bookshelf displays and open the correct catalog entry.
- The viewer renders every page in order, supports page navigation and returning to the shop, and does not lose progress or crash on longer PDFs.
- Build validation rejects corrupt PDFs and items without recorded rights metadata.
- Test the original Last Instinct issue and the public-domain starter comic in a clean install.
- Record package size, memory use, load time, readability, and any supported page-count limits.
