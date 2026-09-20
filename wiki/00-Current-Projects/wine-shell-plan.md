---
date: 2026-09-20
description: "Open plan: Swift + SwiftUI CrossOver-style Wine shell for Apple Silicon (bottles, run-with-options, backends, winetricks) — full error catalog, 5 fault-injection simulations, phased plan with kill criteria."
tags: [builds, plan, swift, swiftui, wine, macos, crossover-alternative, portfolio]
last_updated: "2026-09-20"
confidence: high
relations:
  relates_to: "[[01-Areas/Programming/repo-coding-interview-university]]"
---

## For future agent
**OPEN plan (greenlit 2026-09-20)** — user builds a CrossOver-style Wine wrapper for Mac in Swift/SwiftUI: NOT a hypervisor/VM, a GUI shell around prebuilt Wine (Gcenx builds) managing isolated bottles on Apple Silicon. Contains the full pre-mortem (error catalog §3), CrossOver feature map (§2), 5 fault-injection simulations (§4), phased execution with kill criteria (§5). Status: planned, Phase 0 not started — needs Xcode + a Mac in hand. Working title "wine-shell" (TBC — user names it at Phase 0).

# Wine-Shell — CrossOver-Style Wine Wrapper for Mac (Plan)

> **North Star alignment:** serves the **builds** goal (portfolio piece with a real interview story: "I ship a Wine shell on macOS") + **coding roles** (runs coding tools on the M1 hunt target). Scope guard from [[Key Decisions]]: CAD stays on labs/home PC, OAs on home PC — this tool targets coding tools + light apps, never CAD/proctoring.

## 1. What it is (and is not)

- **Is:** SwiftUI bottle manager + launcher around prebuilt Wine. Create bottle → run `.exe` → per-bottle graphics backend → winetricks fixes. Same category as Whisky / Sikarugir / Scotch (all open-source precedents — study them, don't copy).
- **Is not:** Parallels/VMware (no hypervisor, no kernel code), no Windows license needed, no Intel support, no Compatibility-Center crowd DB (explicit non-goal).
- **Hard requirements:** Apple Silicon only, macOS 14+, Rosetta 2, Xcode to build. No sandbox entitlement (sandboxed apps can't spawn Wine).

## 2. CrossOver feature map (from CodeWeavers user guide 2026)

| CrossOver feature | Our version | Phase |
|---|---|---|
| Bottles (Win profiles, C: drive, registry) | Same minus version profiles — Win10/11 only, version-stamped per bottle | 1 |
| Run Command + Browse C: | Same — pick any exe, run it | 1 |
| Run with Options (args + env + log file + Wine channels) | Same — primary debug tool, build early | 1 |
| winecfg / regedit / notepad / cmd | Same (free — just launch them) | 1 |
| Task Manager / Quit All | `wineserver -k` + process list | 1 |
| Simulate Reboot (`wineboot -r`) | One button; recipes declare `needsReboot` | 1 |
| Wine Configuration (DLL overrides, graphics) | Per-bottle settings screen | 1–2 |
| Save Command as Launcher | Launcher shortcut per exe | 2 |
| Export/Import bottle archive | Zip/unzip bottle folder | 2 |
| Open Shell | Copy-env + open Terminal | 2 |
| CrossTie recipes (URL + install detection) | Minimal recipe JSON: name, download URL, post-install exe path, notes, needsReboot | 2 |
| Compatibility Center crowd ratings | **Never** — refusal list instead (`cannot-run.json`: anti-cheat, kernel drivers) | — |

## 3. Error catalog (pre-mortem — every failure mode + tackle)

**A. Setup:** no Rosetta (`bad CPU type` → detect `oahd`, prompt install, block) · macOS <14/Intel → gate with alert · offline GitHub → retry + manual-tarball-drop path · <2 GB disk → pre-flight check with number shown.

**B. Runtime download (the Whisky-death lesson):** upstream release deleted → **pin exact version + SHA-256, N-1 fallback URL, never fetch "latest"** · partial download → resume/re-download, hash-gate extraction · symlink breakage → `.tar.gz` + `tar`, verify `wine64`+`wineserver` post-extract.

**C. Bottles:** `wineboot --init` hang → 90s timeout + kill + retry/delete dialog · prefix version downgrade corruption → stamp Wine version per bottle, refuse older runtime · stale wineserver lock → "Repair bottle" (kill server, drop lockfile, `wineboot --update`) · spaces/Unicode paths → argv arrays always, never shell strings (design rule day one) · WINEARCH confusion → win64-only, no toggle.

**D. Launching:** missing VC++/DX/.NET DLLs (#1 real failure) → parse log, offer exact winetricks verb button · 16-bit/ARM64EC/driver exes → pre-launch PE check, graceful refusal with reason · reboot-needing installers → auto-suggest Simulate Reboot · zombie wineservers → per-bottle Quit All + auto-kill on quit (configurable) · arg quoting → argv arrays + command preview in Run-with-Options.

**E. Graphics:** D3DMetal picked without GPTK → grey out until valid DMG import (validate `D3DMetal.framework` + forwarders, Whisky-importer pattern) · half-installed DXVK → ship each backend as one tested unit (DLLs + env), never mixable halves · wrong backend black screen → per-program override + "try next backend" cycle · fullscreen capture → default windowed + Metal HUD toggle.

**F. Swift app itself:** `Process` pipe deadlock → async `readabilityHandler` drainage from day one · sandbox blocks Wine spawn → do not sandbox, document · Gatekeeper on our own app → notarization needs paid $99/yr Developer Program; ship via GitHub + "right-click → Open" guide until then · corrupt plist → versioned Codable schema, backup + reset with notice · concurrent launches race → serialize per-bottle runs (actor/queue).

**G. Legal:** never redistribute Apple's D3DMetal (user-DMG-import flow only) · DXMT >0.80 is LGPL (0.80 MIT) — pin ≤0.80 or accept source-disclosure duty · MS fonts/redists via user-time winetricks only, never bundled.

## 4. Simulations (fault-injection dry runs — design consequences)

- **S1 first-run offline:** download fails → offline screen (not infinite spinner) + retry + manual drop; wrong tarball → hash rejects with filename. *Consequence: setup screen designed around failure.*
- **S2 happy path (Notepad):** create → init 30–60s → run. Init hang → 90s timeout + repair. Invisible windows → **Wine.app wrapper bundle mandatory in MVP.** *Consequence: Phase 0 must prove wrapper + init + notepad or project stops.*
- **S3 real app needs VC++ (7-Zip installer):** log shows missing DLL → one-click "install vcrun2019 via winetricks". winetricks needs cabextract → **bundle it (Whisky pattern).** *Consequence: winetricks promoted Phase 2 → Phase 1.*
- **S4 D3DMetal picked, no GPTK:** greyed option + one-line why (Apple license); random DMG → validator rejects. *Consequence: validation ships with picker, never after.*
- **S5 kernel anti-cheat app:** PE scan flags driver install → honest refusal in 30s ("needs a Windows kernel — use UTM/VMware"), not 30min debugging. *Consequence: `cannot-run.json` refusal list is a feature.*

## 5. Phased execution

**Phase 0 — Viability spike (kill-or-go):** Swift `Process` → env passthrough → Rosetta Wine → wrapper bundle → `winecfg` appears → notepad types. **Kill criteria: any step fails after 2 sittings → park until post-laptop-hunt.** Test-harness UI only.

**Phase 0 execution log (2026-09-20, STARTED):** scaffold lives at `C:\Users\Vijaykumar\wine-shell\` (outside vault: `README` + `Spike0/main.swift` harness + `Spike0/Runbook.md` Mac steps + `Spike0/pattern_check.py`). Harness pattern (argv arrays, env merge, async pipe drainage, timeout-kill) **proved on Windows/Python** — first run caught a real bug (merged env never passed to child; fixed, green). Swift compile + Wine/Rosetta/winecfg/notepad proof **pending a Mac in hand** — run `Spike0/Runbook.md` there, paste verdict here.

**No-Mac route log (2026-09-20, BLOCKED on env):** WSL Ubuntu 24.04 chosen (Swift 6.4.0 via swiftly + Wine 9.0 + winetricks + xvfb). Wine + deps installed OK. Swift 6.4.0 downloaded 100% but extraction failed; WSL user-db then broke (libc upgraded under live system), distro now fails to boot (error 6 / E_FAIL) — `wsl --shutdown`, terminate, and `--export` backup all fail. Next: Windows reboot → if Ubuntu boots, `dpkg --configure -a` + rerun `swiftly install 6.4.0` → else reinstall Ubuntu distro (WSL-home data at risk) or pivot to pure-CI route (GitHub Actions Linux + macOS-ARM runners, zero local env).

**CI route log (2026-09-20, PHASE 0 LINUX PASSED):** repo https://github.com/Anirudh-2810/wine-shell (public, `gh` CLI installed via winget, user authed via browser). Run 35519522367 ALL GREEN: linux job (Swift build + unit tests + real Wine `wineboot --init` + `cmd /c echo bottle-alive`) and macos-arm job (build + unit tests on real Apple Silicon macOS). One fix needed: GH ubuntu image ships `wine` not `wine64` → CI resolves either binary (same lesson as local Ubuntu). Still manual (MAC-HANDS): visible winecfg/notepad windows, wrapper-bundle activation, D3DMetal import. Phase 1 (WineKit core is already scaffolded: models, env builder, backends, recipes, refusal, async launcher) unblocked — next: wire launcher integration test + winetricks flow.

**Phase 1 log (2026-09-20, CORE GREEN):** `BottleStore` (CRUD + plist + downgrade guard + duplicate), `WineBoot` (init/update/reboot-sim/quit-all/repair), `RuntimeInstaller` (pinned manifest + SHA gate via system tool + tar extract + installed-gate), `Winetricks` (verb runner + log→verb top-5 table), 13 tests. Run 35519990239 green incl. `LauncherIntegrationTests` (our launcher drove real `wineboot --init` → exit 0, `drive_c` created). One real bug caught: wineboot argv passed as single spaced string → exit 1; split into argv array (same argv rule as plan §3). Next: Phase 2 backend picker + GPTK validator + recipe runner (needs Mac for D3DMetal proof; DXVK/DXMT logic testable in CI).

**Phase 2 log (2026-09-20, CORE GREEN):** `BackendDeployer` (prefix-local DLL deploy, validate-all-before-touching, x32 only if syswow64 exists, `next(after:)` cycle DXVK→DXMT→wined3d, D3DMetal never auto-cycled), `GPTKValidator` (DMG `lib`/`redist`/volume locate + framework/forwarders presence + winebuild builtin-marker check, fail-closed), `RecipeRunner` (verbs → installer → reboot-if-needed → exe verify), `BottleArchive` (tar.gz export/import, symlink-safe). Run 35520957256 green both OSes. One CI-caught bug: hardcoded `/bin/tar` missing on macOS → resolve via `/usr/bin/env` (same fix in RuntimeInstaller).

**Phase 3 log (2026-09-20, CORE + FRONTEND-COMPILE GREEN):** `PEParser` (MZ/PE/COFF machine + rsrc scan → refusal upgrade: ARM64/unknown refused with reason), `SteamDetector` (VDF-lite library + manifest parsing, fixture-tested), `DebugTools` (`LogStore` cap/filter, markdown `DebugBundle`, `UpdateCheck` tag parse + semver compare), `WineShell` SwiftUI app (bottle list/detail, Run-with-Options sheet, backend picker + GPTK warning, debug console, clipboard bundle export) behind `canImport(SwiftUI)` + Linux `@main` stub. Run 35522333174 green both OSes after 3 CI-caught fixes (RunRecord needed public init cross-module; top-level print illegal → `@main` stub; `Binding<GraphicsBackend?>` inference → explicit generic; Steam self-listed library double-count → path dedupe; test arithmetic). GUI behavior, wrapper activation, D3DMetal-live, Sparkle, demo videos stay MAC-HANDS.

**UI-test build log (2026-09-20, GREEN):** `WineShellUI` library split (views + AppState) + slim `WineShell` executable + `WineShellUITests` (9 AppState tests: idle/create/duplicate-guard/no-runtime warning/picker default/D3DMetal condition/log filter/bundle smoke/refresh-after-delete). CI green both OSes after 3 fixes (public App + body for cross-module conformance; fixture wineVersion vs open-guard mismatch). `Spike0/Mac-Session-Pack.md` written (A0–A7 + borrowed-Mac variant + verdict boxes). XCUITest stays parked (needs xcodeproj + signing). Remaining: SwiftUI shell + setup wizard + D3DMetal live proof (all MAC-HANDS).

**Phase 1 — MVP:** bottle CRUD + version stamps + plist models · failure-first setup wizard · pinned runtime + SHA + fallback · Run Command + Run with Options + console viewer · wrapper, wineboot init/update, reboot sim, Quit All, repair flow · **winetricks + cabextract** with log→verb suggestions (top 5 verbs) · refusal engine (PE scan + `cannot-run.json`).

**Phase 2 — Compat depth:** backend picker (wined3d → DXVK → DXMT) as tested units · GPTK import validator · per-program overrides + try-next-backend · bottle archive zip · minimal recipe JSON.

**Phase 3 — Portfolio shine:** exe icons (PE parser), Steam detection, Sparkle updates, docs + 3 demo videos (setup / notepad / 7-Zip). Then filed under `projects/` as interview piece.

**Test matrix (run per phase):** `notepad` (builtin) → 7-Zip installer (winetricks path) → one DX11 demo exe (backend path). All three green on the M1 = phase ships.

**Error budget:** Phase 0 zero tolerance (kill switch) · Phase 1 every §3A–D,F error gets a coded path, not a `print` · Phase 2 §3E · §3G legal check before first GitHub release.

## 6. Open items

- [ ] Machine in hand? Needs Xcode + Apple Silicon Mac to start Phase 0 (laptop hunt: 14" @78k decision pending)
- [ ] App name (working title "wine-shell")
- [ ] Close this plan when Phase 3 ships or project is parked (a stale open plan is drift)
