# Quick-Start Guide — Zero to First Dollar in 14 Days

> Assumes: a computer, internet, ~2 focused hours/day. No coding required (basic JS helps later).

## Phase 1 — Install (Day 1)

### Option A: Docker (recommended)
```powershell
docker volume create n8n_data
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```
Open http://localhost:5678 → create owner account.

### Option B: npm
```powershell
npm install n8n -g
n8n start
```

### Webhooks from the internet (needed for demos)
Install cloudflared or ngrok, then:
```
cloudflared tunnel --url http://localhost:5678
```
Use the generated public URL as your webhook base when demoing.

### Get free API keys today
- Telegram bot: talk to @BotFather → `/newbot` → save token
- OpenAI (or Groq free tier) for AI nodes
- Google Sheets: create service credential in n8n via OAuth popup

## Phase 2 — Learn by importing (Day 2–3)

1. Go to https://zie619.github.io/n8n-workflows
2. Search "telegram", "webhook", "digest", pick 5 workflows → download JSONs.
3. Import each into your local n8n. Re-link credentials. Run once manually.
4. Read the canvas left-to-right until you can explain each node out loud.

**Milestone: you can import, run, and modify any workflow.**

## Phase 3 — Build your 3 portfolio pieces (Day 4–7)

Build these yourself (templates exist in `templates/starter-workflows.md`):

| # | Build | Pattern | Demo value |
|---|---|---|---|
| 1 | Lead capture form → Sheets + instant Telegram alert | Webhook responder | Universal client need |
| 2 | Daily 8am briefing: weather + calendar + top news → email/Telegram | Scheduled digest | The retainer seller |
| 3 | Blog/article URL → AI summary → LinkedIn + X post drafts | AI enrichment | Content clients pay premium |

Record a 60–90s screen video of each running. These videos ARE your storefront.

## Phase 4 — Set up shop (Day 8–10)

- [ ] Upwork profile: title "Automation Developer — n8n / Make / Zapier", portfolio = your 3 videos
- [ ] Fiverr gig #1: "I will build a custom workflow automation bot" ($50 starter)
- [ ] Fiverr gig #2: "I will automate your business reports to Slack/Telegram" ($100)
- [ ] Gumroad product: bundle of 10 cleaned-up workflows ($19–29)
- [ ] LinkedIn post announcing your niche (pick one: real estate agents, e-com stores, coaches, agencies)
- [ ] Payment rails: Stripe payment links OR PayPal OR Wise (international)

## Phase 5 — Outreach engine (Day 9–14, runs forever)

Daily quota (45 min/day):
- 5 cold DMs/emails to niche businesses (scripts in `money/client-acquisition-playbook.md`)
- 1 community contribution (r/n8n answer, forum reply) with soft signature
- 1 content post (workflow tip with short video)

Follow up day 3 and day 7 on non-replies. First client typically lands between outreach #30–80.

## Phase 6 — Deliver like a pro (when client says yes)

1. Discovery call → fill the 10-question form (playbook file)
2. Send proposal within 24h using pricing file template
3. 50% upfront via payment link
4. Clone closest library workflow → customize → test with their accounts
5. Loom walkthrough video at handoff
6. Offer maintenance retainer ($99–299/mo) BEFORE closing ticket #1

## When to formalize (company stuff)

- Under ~$2k/mo side income: operate as individual/freelancer, keep invoices + separate bank account.
- Consistent clients or >$2k/mo: register entity (LLC/Pvt Ltd per your country), business bank, simple contract template, consider professional liability insurance.
- Full playbook for operating the company itself: `company/company-ops-automation.md`.

## Troubleshooting first-week blockers

| Blocker | Fix |
|---|---|
| Webhook not reachable | Tunnel not running / wrong URL prefix — recheck |
| Google OAuth fails | Add exact redirect URL shown in n8n credential screen |
| OpenAI quota errors | Use Groq/OpenRouter free tier while testing |
| Workflow works manual but not trigger | Check timezone (`GENERIC_TIMEZONE` env) and activation toggle |
