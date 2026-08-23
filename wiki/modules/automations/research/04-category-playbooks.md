# Research 04 — Category Playbooks: All 16 Categories, Deep

> The library's official taxonomy (from `context/unique_categories.json`) with, per category: what lives there, the flagship workflow archetypes, the node stacks they share, and how each converts into offers. Counts are approximate distributions across the 4,343-workflow corpus.

## 1. AI Agent Development (~largest category)

**What's inside:** LLM chatbots (Telegram/Discord/Slack frontends), RAG-style pipelines with vector stores, AI agent chains using `*tool` nodes (Airtabletool, Telegramtool, Gmailtool — tools are functions an agent can call), document Q&A, summarizers, classifiers, transcription/voice flows (YouTube transcript extraction appears via community nodes).

**Flagship archetypes:** support bot with escalation-to-human; internal knowledge assistant over Docs/Notion; lead-qualifier that reads replies and scores intent; content generator with approval gate.

**Stack signature:** OpenAI/Anthropic + memory (Redis/Postgres) + tool nodes + webhook/chat triggers + human-in-loop branches.

**Offer conversion:** highest price ceiling in the market ($997–2,497 builds). Sell outcomes ("answers 70% of support tickets"), not "AI". Include a fallback path to a human in every build — it de-risks the sale.

## 2. Business Process Automation

**What's inside:** cross-department glue — invoice generation, employee onboarding checklists, document routing, approval chains, e-signature steps, ERP touches (Odoo), notifications to leadership.

**Archetypes:** purchase-request → manager approval → PO creation; new-hire → accounts creation across SaaS; contract → signed → archive → kickoff tasks.

**Stack:** Forms/webhooks + Sheets/Airtable as state + Gmail/Teams + Wait nodes for SLAs.

**Offer:** classic ops consulting for SMBs; retainers thrive because processes mutate constantly ($199–499/mo Care plans).

## 3. CRM & Sales

**What's inside:** lead capture from every source (FB Lead Ads, Typeform, webhooks) into HubSpot/Pipedrive/Zoho/Copper/Keap; enrichment (Hunter for emails, Humantic AI for personality profiles); round-robin assignment; follow-up sequences; deal-stage alerts.

**Archetypes:** speed-to-lead machine; pipeline hygiene sync (two-way CRM↔Sheet); win/loss weekly digest; dead-deal reactivation drips.

**Stack:** CRM nodes + Google Calendar + Gmail/Twilio + AI scoring.

**Offer:** sales teams feel revenue impact directly → value pricing works ($697–1,497). Speed-to-lead demo closes this niche fastest.

## 4. Cloud Storage & File Management

**What's inside:** Drive/Dropbox/OneDrive/S3/Box automation — auto-filing by content type, OCR handoffs (AWS Textract), image resizing, backup mirrors, permission cleanups, binary conversions (Compress, ConvertToFile, ExtractFromFile nodes).

**Archetypes:** invoice PDF arrives → extract → rename → file by vendor/month; photo upload → thumbnail variants → CDN push; nightly Drive→S3 mirror with verification.

**Offer:** quiet but sticky; bundle into any bigger system. Also your own infrastructure: client deliverables auto-filed per project.

## 5. Communication & Messaging

**What's inside:** the notification layer of everything — Telegram bots (dominant), Slack apps, Discord community bots (Discordtool = agent tooling), WhatsApp flows, SMS via Twilio, email fallbacks, Matrix for self-hosters.

**Archetypes:** alert fan-out with severity routing; digest batching (never spam one-by-one); two-way command bots ("/status", "/pause"); broadcast with rate limiting.

**Stack:** messaging nodes + Redis/Set for dedupe + IF severity + error watchdog.

**Offer:** rarely sold alone — it's the delivery mechanism inside every other offer. Master one bot framework cold (recommend Telegram: fastest setup, biggest library representation).

## 6. Creative Content & Video Automation

**What's inside:** blog→newsletter pipelines, podcast publishing chains, YouTube description/chapter generation, transcript repurposing, Bannerbear/APITemplate.io image generation, slides automation (Google Slides).

**Archetypes:** video upload → transcript → blog draft → social clips list; RSS → newsletter issue; template-image generation at scale (ad variants).

**Offer:** creators and agencies pay for consistency, not creativity — sell "publish 5×/week without touching anything" ($297–997 + retainer).

## 7. Creative Design Automation

**What's inside:** Figma-triggered workflows (new frame → export → notify/handoff), dynamic banner generation, template personalization, screenshot services, PDF assembly.

**Archetypes:** design-request form → Figma API render → review link → delivery; 100 localized ad banners from a Sheet spec.

**Offer:** niche but low competition; agencies white-label happily. Pair with marketing category for full-funnel packages.

## 8. Data Processing & Analysis

**What's inside:** ETL jobs — CSV/JSON ingestion, dedupe/comparison (CompareDatasets node), aggregation, BigQuery loads, spreadsheet crunching, scheduled exports, format conversions (XML node), data validation gates.

**Archetypes:** nightly sales CSV → clean → BigQuery → Monday chart; multi-source merge into single reporting sheet; anomaly detection with threshold alerts.

**Stack:** Code node (JS) comfort required here — this category is where scripting pays.

**Offer:** "reporting automation" retainers; charge for correctness guarantees (validation summaries in every run).

## 9. E-commerce & Retail

**What's inside:** Shopify/WooCommerce order events → fulfillment/alerts; inventory sync; review requests post-delivery; abandoned-cart nudges; Gumroad sales → accounting rows; Chargebee subscription events.

**Archetypes:** order → label → tracking → SMS; low-stock → supplier PO draft; daily store KPI digest; fraud-flag alerts.

**Stack:** store webhooks + Sheets/Airtable + Twilio/Gmail + Stripe/PayPal.

**Offer:** e-com owners are the best-retainer buyers online (revenue-linked, always busy). $397–997 setups convert well with a live cart-abandonment demo.

## 10. Financial & Accounting

**What's inside:** QuickBooks/Invoice Ninja invoicing flows, expense collection from email receipts, Wise payments triggers, crypto price monitors (CoinGecko), payment reconciliation against bank exports.

**Archetypes:** receipt email → parse → expense sheet → month-end summary; unpaid-invoice reminder ladder; exchange-rate alerting; Stripe payout → books matching.

**Offer:** accountants/bookkeepers are automation-starved and refer aggressively. Compliance caution: never auto-post without a review step unless contracted otherwise.

## 11. Marketing & Advertising Automation

**What's inside:** campaign ops — FB Lead Ads ingestion, drip sequences (Mailchimp/MailerLite/ConvertKit/GetResponse/Mautic/Lemlist outreach), social posting, SEO/rank checks, UTM governance, ad-spend digests, webinar funnels (GoToWebinar).

**Archetypes:** see dedicated `categories/marketing.md` playbook — speed-to-lead, nurture drips, Monday ad reports, review radar.

**Offer:** the most crowded freelance space BUT also most demand; differentiate by vertical packaging, not generic gigs.

## 12. Project Management

**What's inside:** Jira/Asana/Trello/ClickUp/Monday/Taiga synchronization, standup digest builders, time-tracking rollups (Clockify, Toggl), release-note compilation, ticket triage with AI.

**Archetypes:** form → ticket with smart routing; due-soon daily digest; cross-tool status mirror; sprint-close report.

**Offer:** agencies/dev shops buy internal efficiency quietly; sell via the ops manager, not the owner.

## 13. Social Media Management

**What's inside:** posting schedulers, engagement capture, mention monitoring, follower analytics pulls, Twitter/X tool-node agents, content calendar syncing with Notion/Sheets.

**Archetypes:** queue → publish → log permalink → weekly stats pull; keyword mentions → sentiment → alert/draft reply.

**Offer:** volume play — sell monthly content-engine subscriptions rather than builds ($149–299/mo).

## 14. Technical Infrastructure & DevOps

**What's inside:** server monitoring (UptimeRobot, SignL4 paging), CI/CD notifications (TravisCI, Bitbucket, Netlify deploys), message-queue bridges (AMQP, MQTT, SSE), security triage (TheHive, Cortex incident feeds), backups, SSH-ish ExecuteCommand patterns.

**Full recipes:** `categories/devops.md`. **Offer:** uptime sentinels + deploy notifiers = near-zero-maintenance retainers ($99–199/mo each).

## 15. Web Scraping & Data Extraction

**What's inside:** HTTP Request scraping loops, HTML/XML parsing, pagination handlers, API harvesting, RSS monitoring, screenshot-diff approaches, anti-block pacing (Wait jitter), export to Sheets/Datastores.

**Archetypes:** competitor price watch; job-board aggregation; directory lead lists; SERP tracking.

**Legal note:** respect ToS/robots; position as monitoring public data. **Offer:** data-as-a-service retainers (weekly refreshed lists) — recurring by nature.

## 16. Uncategorized (the junk drawer)

Everything the classifier couldn't place — often experimental single-service toys, training examples (note the `N8ntrainingcustomermessenger` folder), or hyper-niche integrations. Mining tip: occasional gems hide here; sort by newest and skim monthly for novel node combinations nobody else has productized yet.

---

## Cross-Category Portfolio Strategy

Build your service menu as a pyramid:

- **Base (volume):** Communication+Marketing combos — fast builds, steady demand
- **Middle (margin):** Sales/E-com/Business-process systems — value-priced projects
- **Apex (moat):** AI Agent + DevOps/Data specialties — few competitors, premium rates

Each delivered project should reuse components across categories (your Telegram notifier, your Sheets logger, your AI scorer are shared organs between all sixteen categories). That compounding library — not the category count — is the actual asset you're building.
