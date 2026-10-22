# makp0 Homebrew tap

Install [switchpack](https://github.com/makp0/switchpack), a declarative manager
for Nintendo Switch homebrew apps:

```sh
brew install makp0/tap/switchpack
switchpack init
switchpack install --mtp --dry-run
```

Or use `--target <mounted SD root>` for Hekate USB Mass Storage or a card reader.
Homebrew installs libmtp and compiles the USB helper automatically. switchpack
0.2.0 and later also install sevenzip for `.7z` packages, plus sysmodule examples
under `$(brew --prefix)/share/switchpack/examples`. Bun is not
required. Supports macOS 15+ and Linux on ARM64 and x64.

Upgrade with `brew update && brew upgrade switchpack`.

## Maintaining the formula

The workflow checks switchpack's latest stable release hourly. It validates
the four release checksums, generates the formula, installs and tests it on
macOS, then commits any update using this repository's own GitHub token.
No cross-repository credential is required. A failed installation prevents
the update from being committed.

Run it immediately after a release:

```sh
gh workflow run update.yml --repo makp0/homebrew-tap
```

Or regenerate locally with `python3 scripts/update.py`. Test the generator with
`python3 -m unittest discover -s scripts`. The updater only uses Python's
standard library.
