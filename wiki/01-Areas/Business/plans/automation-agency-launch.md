---
course_code: "BUSINESS"
course_name: "Business — Automations Agency"
unit: "Plans"
date: "2026-11-08"
tags: [business, automations, make-com, crm, freelancing, agency, plan, money]
last_updated: "2026-11-08"
confidence: high
description: "Execution plan to launch a solo automation agency on Make.com with an agency CRM and reach first dollar. Scope + order only, no timing estimates. Serves North Star freelancing-start goal."
relations:
  relates_to: "[[earn-with-n8n]]"
  depends_on: "[[client-acquisition-playbook]]"
---

## For future agent

This is the **owner's agency launch plan**: Make.com (platform choice confirmed 2026-11-08 — NOT maake.com, the textile printer) + a free agency CRM to track leads, ending at first paid client and a retainer. It is the execution layer over the strategy already in `automations/money/` — it does not restate pricing or outreach scripts; it says **what to do in what order**. No timing estimates by design (plans law). Update or **close** this note when the first client is delivered; a stale open plan is drift. Stack facts (Make free-tier limits, CRM choice) are volatile — re-verify before relying on them.

# Automation Agency Launch — Make.com + CRM

**Serves:** [[North Star]] → "Freelancing start — pick a first-offer strategy."

## Stack (decided 2026-11-08)

| Layer | Choice | Why |
|---|---|---|
| Automation platform | **Make.com** | Owner's pick. Visual scenarios, free tier to start `(limits TBC — verify on signup)` |
| Agency CRM | **HubSpot Free CRM** | Free forever core: contacts, deal pipeline, tasks, email log. Attio/Folk are alternates if HubSpot feels heavy |
| Bootstrap CRM | Google Sheet, only if HubSpot blocked | One Make scenario later re-points to HubSpot — don't over-invest in the sheet |
| Payments | PayPal / Wise first; Stripe when revenue justifies entity | Per [[pricing-and-packages]] |
| Blueprint library | n8n JSON library = **patterns only** | JSON won't import into Make — rebuild the *logic* as a Make scenario ([[automations-catalog]]) |

The strategy pages stay source-of-truth: [[earn-with-n8n]] (paths) · [[client-acquisition-playbook]] (niche, scripts, calls) · [[pricing-and-packages]] (packages, contracts) · [[quick-start-guide]] (shop setup — re-read Phase 4–6 with Make instead of n8n).

## The offer (first-offer strategy)

**One productized service, sold repeatedly:**

> **Lead-to-CRM speed machine** — form/DM lead → instantly in your CRM → owner gets an alert → lead gets a reply/booking link → follow-up if no response.
> **Price:** [[pricing-and-packages#Three Core Packages (productized)|STARTER $297–497]] setup + optional Monitor/Care retainer. First 2 client builds may go lower for reviews only — then never discount (reduce scope instead).

Why this offer: universal pain, demo-able in 2 minutes, every vertical in the niche table needs it, and it **is** your own agency pipeline (dogfood — see Step 3).

## Ordered steps (scope, not schedule)

Do them in order; a step is done only when its check passes.

### 1. Accounts
- [ ] Make.com account (free tier)
- [ ] HubSpot Free CRM account
- [ ] PayPal or Wise receiving rail
- [ ] Telegram bot for alerts ([[quick-start-guide#Phase 1 — Install (Day 1)|BotFather]])

### 2. Niche gate (from [[client-acquisition-playbook#1. Pick a Niche (do this first)|§1]])
- [ ] Pick ONE niche where you can name **20 real businesses** you could email today
- [ ] Write the one-liner: "I automate {{painful task}} for {{niche}} so you stop losing {{hours/leads}}"
- [ ] Do not proceed to outreach until this exists (building without a niche = drift)

### 3. Dogfood your own CRM pipeline (also portfolio piece #1)
Build in Make, end-to-end:
- [ ] Lead form (Tally/Google Form/webhook) → HubSpot contact + deal in **Outreach** pipeline
- [ ] Instant Telegram alert to you on every lead
- [ ] Auto-reply email/DM with booking link
- [ ] Day-3 no-response follow-up task created in HubSpot
- [ ] **Check:** submit a test lead → appears in HubSpot < 1 min → alert fires → follow-up task exists
- This scenario is simultaneously: your agency ops, your proof-of-competence, and the demo you'll record.

### 4. Two more portfolio pieces (adapt [[quick-start-guide#Phase 3 — Build your 3 portfolio pieces (Day 4–7)|Phase 3]])
- [ ] Scheduled daily digest (calendar + priorities → Telegram/email) — the retainer seller
- [ ] Content/URL → AI summary → post drafts — the premium add-on demo
- [ ] 60–90s screen recording of each running; these videos = storefront

### 5. Storefront (from [[quick-start-guide#Phase 4 — Set up shop (Day 8–10)|Phase 4]], Make-flavored)
- [ ] Upwork profile: "Automation Developer — Make / n8n / Zapier" + 3 videos
- [ ] Fiverr gig: custom workflow automation ($50 starter) + reporting automation ($100)
- [ ] LinkedIn profile/post stating the niche one-liner from Step 2
- [ ] HubSpot **your own** pipeline live: Outreach → Contacted → Call booked → Proposed → Won/Lost

### 6. Outreach engine (scripts: [[client-acquisition-playbook#3. Outreach Scripts|§3]])
- [ ] Daily quota forever: 5 niche contacts + 1 community answer + 1 content post
- [ ] Follow-ups day 3 and day 7; log every send in HubSpot (the CRM is useless if unlogged)
- [ ] First client typically lands between outreach #30–80 — volume is the plan, not luck

### 7. First paid build (process: [[quick-start-guide#Phase 6 — Deliver like a pro (when client says yes)|Phase 6]])
- [ ] Discovery call → proposal within 24h ([[client-acquisition-playbook#6. Proposal Template (send within 24 h)|template]])
- [ ] 50% upfront before any build work
- [ ] Clone/adapt your Step 3 machine to their stack; handoff video
- [ ] Offer retainer BEFORE closing the ticket ([[pricing-and-packages#Retainer Menu (the real business)|retainer menu]])
- [ ] Ask: "What's the second most annoying manual thing here?"

### 8. Repeat → formalize
- [ ] Every handoff → next-sale question → second build or retainer
- [ ] Raise prices 10–15% every 3 delivered projects ([[pricing-and-packages#Rate Raiser Schedule]])
- [ ] Register entity only after consistent clients or >₹/€/$2k mo side income ([[quick-start-guide#When to formalize (company stuff)|formalize rules]]); full company ops: [[company-ops-automation]]

## Metrics (log weekly in HubSpot or a sheet)

| Metric | Target signal |
|---|---|
| Outreach sent / replies / calls booked | engine healthy if reply rate > 0 after #20 |
| Proposals → win rate | < 20% = fix proposal or niche, not more outreach |
| MRR (retainments) vs project $ | retainer $ should overtake project $ by client #5 |
| Hours saved per client (their number) | pricing ammunition for upsell |

## Close condition

Close this plan when: **first client delivered + retainer offered (accepted or declined) + metrics logged once.** After that the live operating system is [[earn-with-n8n]] weekly rhythm + [[client-acquisition-playbook]].

## Related

[[earn-with-n8n]] · [[client-acquisition-playbook]] · [[pricing-and-packages]] · [[quick-start-guide]] · [[automations-catalog]] · [[company-ops-automation]] · [[01-Areas/Roadmaps/INDEX]] · [[North Star]]
