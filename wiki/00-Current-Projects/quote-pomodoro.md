---
module: "current-projects"
topic: "Quote Pomodoro — Dark-Mode Focus Timer with Motivational Quotes"
tags: [builds, productivity, tkinter, pomodoro, focus, desktop-app, windows, notifications]
last_updated: "2026-08-26"
confidence: "high"
source: "Desktop/Anirudh/My apps/Focus app/flightproductivity.py"
description: "Tkinter Pomodoro timer with editable session length, progress bar, rotating motivational quotes, system beep notifications, Windows toast notifications (plyer), pause/resume, preset buttons (25/5, 50/10, 15/3). Dark theme (#000000/#00ff88)."
---

# Quote Pomodoro — Dark-Mode Focus Timer

> **Source:** `Desktop/Anirudh/My apps/Focus app/flightproductivity.py`
> **Stack:** `tkinter`, `ttk`, `threading`, `plyer` (notifications), `winsound` (Windows beeps)
> **Platform:** Windows (primary), Linux/macOS (fallback beeps)
> **Theme:** Pure black background, mint green (#00ff88) accents

---

## For future agent
This is a **personal productivity build** — a minimal, distraction-free Pomodoro timer with motivational quotes. Demonstrates Tkinter threading pattern (UI thread + timer thread), cross-platform sound/notifications, and clean dark UI. Cross-links: [[wiki/01-Areas/Self-Dev/]], [[wiki/01-Areas/Productivity/]], [[wiki/00-Current-Projects/budget-tracker]].

---

## 1. Features

| Feature | Implementation |
|---------|----------------|
| **Editable Timer** | Click time display → type `mm:ss` → Start |
| **Presets** | 25/5 (classic), 50/10 (deep work), 15/3 (quick) |
| **Progress Bar** | ttk.Progressbar, mint green fill |
| **Quotes** | 10 rotating focus quotes, auto-refresh ~every 5 min |
| **Sounds** | Start: 800Hz beep, End: 600Hz+450Hz (winsound) |
| **Notifications** | Windows toast via `plyer` (optional) |
| **Pause/Resume** | Button toggles text |
| **Reset** | Restores to last preset |
| **Keyboard** | Enter to start, Space to pause (could add) |

---

## 2. Architecture

```mermaid
flowchart TD
    A[Main Thread: Tkinter UI] --> B[Timer Thread]
    B --> C[Sleep 1s loops]
    C --> D[Update remaining]
    D --> E[root.after(0, tick_ui)]
    E --> F[Update display + progress]
    F --> G{Phase complete?}
    G -->|Yes| H[finish_phase]
    H --> I[Beep + Notification]
    H --> J[Reset UI state]
    B --> K[Quote rotation every ~5 min]
```

**Threading Pattern:**
- Timer runs in `daemon=True` background thread
- UI updates via `root.after(0, callback)` (thread-safe)
- Pause flag checked each loop iteration

---

## 3. Code Structure

```python
class QuotePomodoro:
    def __init__(self, root):
        self.root = root
        self.is_running = False
        self.is_break = False
        self.remaining = 0
        self.total = 0
        self.build_ui()  # Dark theme, progress bar, quotes

    def start_timer(self):
        # Parse time, start daemon thread
        threading.Thread(target=self.loop, daemon=True).start()

    def loop(self):
        while self.is_running and self.remaining > 0:
            time.sleep(1)
            if paused: continue
            self.remaining -= 1
            self.root.after(0, self.tick_ui)
            # Quote rotation logic

    def tick_ui(self):
        self.time_var.set(format_time(self.remaining))
        self.progress["value"] = self.total - self.remaining
```

---

## 4. UI Details

| Element | Style |
|---------|-------|
| **Background** | `#000000` (pure black) |
| **Accent** | `#00ff88` (mint green) |
| **Font** | Segoe UI / Consolas (monospace for timer) |
| **Progress Bar** | `troughcolor="#111111"`, `background="#00ff88"` |
| **Buttons** | `#222222` bg, `#ffffff` fg, hover `#333333` |
| **Window** | 600×320, non-resizable |

---

## 5. Quote Bank (10 Quotes)

```python
QUOTES = [
    "Focus is a muscle; train it every day.",
    "Small consistent sessions beat long distracted ones.",
    "Deep work now, freedom later.",
    "Discipline is choosing what you want most.",
    "One Pomodoro at a time.",
    "Silence the noise, follow the task.",
    "You don't rise to your goals, you fall to your systems.",
    "Future you is grateful for this focus.",
    "Less scrolling, more solving.",
    "Progress, not perfection."
]
```

---

## 6. Cross-Platform Sounds

```python
def play_beep_start():
    if winsound and sys.platform.startswith("win"):
        winsound.Beep(800, 160)
    else:
        print("\a", end="")  # Terminal bell

def play_beep_end():
    if winsound and sys.platform.startswith("win"):
        winsound.Beep(600, 220)
        winsound.Beep(450, 220)
    else:
        print("\a\a", end="")
```

**Notifications (Windows):**
```python
from plyer import notification
notification.notify(title="Time's up", message="Pomodoro complete.", timeout=4)
```

---

## 7. Usage

```bash
# Install deps
pip install plyer  # Optional, for Windows toast

# Run
python flightproductivity.py
```

**Workflow:**
1. Launch → shows "25:00" default
2. Edit time or click preset (25/5, 50/10, 15/3)
3. Click **Start** → beep, timer counts down, progress bar fills
4. **Pause** / **Resume** as needed
5. At 0:00 → double beep, toast notification, "Done" phase
6. **Reset** to restart

---

## 8. Cross-References

- [[wiki/01-Areas/Self-Dev/]] — Pomodoro, Deep Work, productivity systems
- [[wiki/01-Areas/Productivity/]] — Atomic Habits, GTD, timeboxing
- [[wiki/00-Current-Projects/budget-tracker]] — Another personal productivity tool
- [[wiki/01-Areas/Programming/learn-python-fast-system]] — Tkinter GUI basics

---

## 9. Known Limitations / TODOs

- **No session logging** — no CSV/DB export of completed Pomodoros
- **No task association** — can't link timer to specific task
- **No statistics** — no daily/weekly totals, streaks
- **Single timer** — no multi-project support
- **No auto-break** — doesn't auto-start break timer after focus
- **Windows-only sounds** — Linux/macOS only get terminal bell
- **No system tray** — can't minimize to tray

---

## See Also
- [[wiki/01-Areas/Self-Dev/learning-methodology]] — Pomodoro in learning context
- [[wiki/01-Areas/Productivity/atomic-habits-systems]] — Habit tracking