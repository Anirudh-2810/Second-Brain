# Personal Daily Automation

> 12 recipes that give back 1–2 hours/day. Difficulty: E (easy, <30 min) / M (medium) / A (advanced). All runnable on free local n8n.

## The Flagship: Morning Briefing — M

**Time:** daily 7:00 (`0 7 * * *`)
**Flow:** Schedule → Weather API node (or HTTP to open-meteo, free) → Calendar events (Google) → Tasks due (Sheets/Notion) → top headlines RSS → AI node writes 5-line summary in your tone → Telegram message.
**Why first:** you'll feel the value every single day; template exists in library ("daily briefing telegram").

## Email Triage Assistant — M

Gmail trigger (every 5 min) → rules:
- Receipts/invoices → label + extract amount to expense sheet
- Newsletters → skip inbox, weekly digest folder
- From VIP list → Telegram ping
- AI optional: draft reply for common asks → save to Drafts for review

## Expense Auto-Tracker — E

Bank/payment emails arrive → regex extracts merchant + amount → append row (date, merchant, amount, category guess) → Sunday cron sends week total by category to Telegram.
No bank email? Forward payment confirmations from PayPal/stripe manually to a filter address.

## Bill Guard — E

Sheet of bills (name, day, amount) → cron monthly checks upcoming 5 days → Telegram reminders → after payment confirmation email arrives, row auto-checks green.

## Habit & Health Logger — M

Telegram bot with inline buttons (Water / Gym / Read / Meditate) → callback logs timestamp to sheet → nightly summary streak message. Miss 2 days → nudge message next morning.

## Downloads Folder Janitor — E

Schedule hourly (machine with n8n local access) → read directory → move files by extension into subfolders (PDF→docs, images→pics, installers→delete-after-7d).
Node tip: use Execute Command or Read/Write Files nodes.

## Price-Drop & Restock Watcher — M

List of product URLs → every 6 h fetch page → compare price/XPath vs stored value → changed? Telegram alert + update sheet. Works for flight prices too (scrape politely; respect ToS).

## Job/Application Tracker — E

Applied somewhere? Forward the application email to your bot address → parsed into tracker sheet → cron nudges follow-up after 7 days if no interview invite.

## Learning Journal Auto-Log — E

End-of-day Telegram prompt at 21:30: "3 lines about today?" → reply appended to monthly note file with date header. Zero-friction diary.

## Reading Queue Digest — E

Save articles to a "read later" sheet/bookmark tag → Sunday AI summarizes each unread item to 2 lines + link → pick what's worth deep reading.

## Birthday & Relationship Radar — E

Contacts with birthdays in sheet → 7-day and same-day alerts → suggested message draft via AI using last-interaction note column.

## Focus Guardian — A

Calendar shows "deep work" block → phone-forward/DND trigger via automation platform or macro app → auto-status in Slack/Teams → calls silenced; ends when block ends.
(Requires companion integration like IFTTT/Tasker bridging webhook.)

---

## Setup Order

1. Morning briefing (instant daily payoff)
2. Expense tracker + bill guard (money clarity)
3. Email triage (biggest time sink removed)
4. Everything else by annoyance level

## Hygiene Rules

- One Telegram bot = your universal notification hub
- Name workflows clearly: `PERSONAL | morning-brief v2`
- Error branch on every workflow → pings YOU (silent failures are why people quit automations)
- Review monthly: delete workflows you ignore; keep the ones that actually fire
