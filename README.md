<p align="center">
  <img src="docs/assets/logo.png" alt="RestedXP addon logo" width="112" height="112">
</p>

<h1 align="center">RestedXP for WoW Forever</h1>

<p align="center">198 unencrypted guides. Both factions. No user ID or BattleTag activation.</p>

<p align="center">
  <a href="https://github.com/ah682/restedxp-jailbroken-decrypted/releases/latest/download/RestedXP-Forever-Complete.zip"><strong>Download the complete addon</strong></a>
  ·
  <a href="https://github.com/ah682/restedxp-jailbroken-decrypted/releases/latest">All downloads</a>
</p>

## Install

1. Close World of Warcraft.
2. Download [RestedXP Forever Complete](https://github.com/ah682/restedxp-jailbroken-decrypted/releases/latest/download/RestedXP-Forever-Complete.zip).
3. Open your World of Warcraft folder, then `_forever_`, `Interface`, and `AddOns`.
4. Extract **both** `RXPGuides` and `RXPDecryptedGuides` directly into `AddOns`.
5. Start the game. On the character screen, open **AddOns** and enable **RestedXP Guides** and **RXP Decrypted Guides**.
6. Enter the game and open the RestedXP guide selector. Choose **RestedXP Forever Guide (A)** for Alliance or **RestedXP Forever Guide (H)** for Horde.

The folders should look like this:

```text
World of Warcraft/
  _forever_/
    Interface/
      AddOns/
        RXPGuides/
          RXPGuides.toc
        RXPDecryptedGuides/
          RXPDecryptedGuides.toc
          Forever_Leveling_Guide_Both_Factions.lua
```

Keep the two addon folders beside each other. Putting the companion inside `RXPGuides`, or putting an extra ZIP folder around both addons, prevents the game from finding it.

There is no user ID entry, account activation, paid login or text import required to load the included guides. Once both addons are enabled, select a route and play.

### Already have RXPGuides?

Download the smaller [guide companion](https://github.com/ah682/restedxp-jailbroken-decrypted/releases/latest/download/RXPDecryptedGuides.zip) and extract `RXPDecryptedGuides` into `AddOns`. Keep your existing RXPGuides installation enabled. It must be a version with Forever support.

Use the companion download if you already maintain RXPGuides through an addon manager. The complete bundle includes v4.11.36; copying it over a newer installation would replace that newer version.

Use the release downloads linked above. GitHub's **Source code** archives contain the repository and are not the complete addon bundle.

## What is included

The companion contains **198 English guides** from one Forever export. It covers both factions, with leveling routes through level 60, dungeon routes, dungeon quests and class specific routes. The normal RXPGuides addon supplies the starter guides and the interface.

**Complete download:** RXPGuides v4.11.36, the guide companion, installation instructions and the original addon license notices.

**Companion download:** The guide data only. Normal RXPGuides is a required dependency.

This snapshot was packaged on **12 November 2026**. The exported guide revision is **24**, and the tested Forever interface version is **16001**. English text is used on all 11 client locales listed in the companion manifest.

## How it works

The original export was tied to an account. It was converted once into readable guide text and packaged as a separate addon named `RXPDecryptedGuides`.

At startup, the companion passes that text to `RXPGuides.RegisterGuide`. The normal RXPGuides addon handles the guide window, navigation, quest tracking and step progression. Its code does not need patching.

The companion has no user ID check, BattleTag activation or paywall check at runtime. It contains the guide text directly and declares `RXPGuides` as its dependency, so the main addon loads first. The original account named export and personal game settings are not part of this repository or its release downloads.

## Updates and compatibility

**The main addon and the guide content are separate.** A normal RXPGuides update should leave the companion installed because each has its own folder. Compatibility still depends on RXPGuides continuing to support Forever and the same guide registration interface.

**This is a snapshot.** Updating RXPGuides does not refresh the companion's guide text. If a future guide pack grows from 198 guides to 206, this companion still contains the original 198. Adding those eight guides requires a fresh export, another conversion and a new release here.

Nothing in this package downloads new guide content automatically. This repository also does not promise a release for every upstream update.

To update the companion, close the game and replace only the `RXPDecryptedGuides` folder with the one from a newer release. Keep a copy of the previous folder if you want an easy rollback.

## Troubleshooting

### The companion says its dependency is missing

Enable **RestedXP Guides** as well as **RXP Decrypted Guides**. Confirm that `RXPGuides.toc` is directly inside `AddOns/RXPGuides/`.

### Only starter guides appear

Confirm that the companion is enabled and that `RXPDecryptedGuides.toc` is directly inside `AddOns/RXPDecryptedGuides/`. Restart the game after adding a new addon folder. Guides are filtered for your character, so a single character will not see all 198 entries.

### I selected a dungeon route by mistake

Choose the **RestedXP Forever Guide** group for the regular leveling route. **Dungeon Guide** and **Dungeon Quests** are separate groups.

### I cannot find the settings

Enter `/rxp` in chat to open the normal RestedXP settings.

### I want to remove it

Close the game and remove `AddOns/RXPDecryptedGuides/`. Your normal RXPGuides installation can stay in place.

## Verification

The packaged Lua file passes Lua 5.1 syntax checks. All 198 guides were registered through the installed RXPGuides v4.11.36 loader across all 11 listed locales with the account API made unavailable. The registered text matches the validated export, and both release archives are checked for file integrity.

These are offline checks. Live gameplay, individual quest progression and future addon versions have not been verified.

For the registration check, install Python 3 and Lua 5.1, then run this from the repository:

```bash
python3 tests/verify.py "/path/to/Interface/AddOns/RXPGuides" lua5.1
```

The check reads the supplied RXPGuides folder. It does not change the game installation and does not require an account export.

The installable source is in `RXPDecryptedGuides/`. The complete bundle is attached to each release so the repository stays focused on the companion and its documentation.

## Credits

RXPGuides and the logo shown above are by **RestedXP**. The logo is the actual addon texture converted to PNG without changing its pixels. The base addon is bundled without code changes, with its license notices preserved.

The guide conversion uses [imSp4rky's converter](https://gist.github.com/imSp4rky/17759ae4bd9a78fdc898c901c2436be1), version 1.0.3. The companion preserves the original guide text and authorship.

This is an independent community package, not an official RestedXP release. See [NOTICE.md](NOTICE.md) for asset attribution and the included license information.
