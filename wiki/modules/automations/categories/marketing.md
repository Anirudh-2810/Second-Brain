# Category Deep-Dive: Marketing Automation

> ~350 workflows in the source library. Marketing tasks are repetitive by design — perfect automation territory and the easiest category to sell to non-technical owners.

## Where the Manual Pain Lives

| Task | Typical manual cost | Automated flow |
|---|---|---|
| Lead follow-up | hours/day, inconsistent | instant reply + nurture sequence |
| Social posting | 30–60 min/post | batch → schedule → auto-publish |
| Review management | missed replies | alert + draft response |
| Reporting (weekly) | 1–2 h/Monday | auto digest from ad platforms |
| Content repurposing | per-platform rewriting | 1 source → all platform drafts |

## Workflow Recipes

### 1. Speed-to-Lead Machine — M
Form/DM/call webhook → CRM row → AI qualifies (budget/timeline/fit questions answered?) → hot lead: instant SMS/WhatsApp with booking link + sales ping; warm: nurture email sequence (Wait nodes between sends).
**Stat to sell with:** responding in <5 min converts 8–10× better than in an hour.

### 2. Nurture Drip Engine — M
Tag-based: new subscriber → Day 0 welcome → Day 2 value email → Day 4 case study → Day 6 offer. Implement with Wait node or date-triggered sheet scan. Unsubscribe/click webhooks update tags.
**Nodes:** Gmail/SMTP or Resend, Sheets/Airtable for audience, IF on engagement.

### 3. Social Auto-Publisher — M
Content queue sheet (`status=approved`) → cron checks daily → post via platform APIs or Buffer/Make-webhook bridge → mark posted + store permalink → weekly performance pull into same row.
Human approval gate (Pattern F) keeps brand safety.

### 4. Review & Mention Radar — E
Cron → Google Places/Yelp/APIs or RSS of mentions → new review? → sentiment check (AI) → positive: thank-you draft; negative: urgent Telegram ping + draft acknowledgment for owner approval.

### 5. Monday Morning Ad Report — E→M
Cron Mon 7am → Meta Ads + Google Ads APIs (or exported sheets) → compute spend, CPC, ROAS vs last week → AI writes 5-bullet "what changed & what to do" → email client + Slack.
**This is a classic $149/mo retainer** — agencies hate building it manually every week.

### 6. Content Repurposing Pipeline — M
One blog/RSS item → AI generates LinkedIn post, X thread, Instagram caption + hashtag set, short-video script → drafts land in review sheet → approved versions feed recipe #3.
Full JSON skeleton lives in `templates/starter-workflows.md` (#4).

### 7. SEO Watchdog — E
Weekly → fetch target keywords positions (API or SERP scraper) + backlink count → threshold drops → alert; monthly trend chart data appended for client calls.

### 8. Webinar/Launch Funnel — A
Registration webhook → calendar invite + reminders at T-24h/T-1h/T-10min → no-show list post-event → replay link sequence → attendee follow-up with offer. All steps logged so nothing slips during launch chaos.

## Node Stack Cheat Sheet

| Job | Go-to |
|---|---|
| Capture | Webhook / Typeform / FB Lead Ads trigger |
| Store | Google Sheets → Airtable when client-facing |
| Send | Gmail (small), SMTP, Resend/SendGrid (volume) |
| Social | Platform HTTP APIs, Buffer bridge |
| Write | OpenAI/Groq node with strict output template |
| Approvals | Slack interactive buttons / Telegram callback |

## Selling It

Niche-first pitch (see playbook): pick ONE vertical, demo recipe #1 or #5 live on their own data in a Loom.
Package anchor: Growth package $697–1,497 setup + Care retainer $199/mo.

## Gotchas

- Email sending limits: warm domains, keep cold volume <50/day/address
- Platform API approvals (Meta, X) take days — start credential setup early
- Always keep human-approval before public posting until client explicitly opts out
