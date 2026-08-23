# Research 03 — Integration Universe: All 365 Services Mapped

> The complete integration landscape of the library: all 188 primary folders enumerated, grouped into the 12 official service categories, layered with usage-frequency tiers and credential requirements. This is your supplier catalog — every service here is a component you can sell.

## 1. How Integrations Are Organized

The `workflows/` directory has 188 folders, each named for the workflow's **primary** integration (a workflow touching Telegram + Sheets + OpenAI lives in one folder, chosen by its dominant node). Across those workflows, 365 distinct services appear. The indexer's own `get_service_categories()` groups them into 12 domains:

| Domain | Members (from source code) |
|---|---|
| messaging | Telegram, Discord, Slack, WhatsApp, Mattermost, Microsoft Teams, Rocket.Chat |
| email | Gmail, Mailjet, Email (IMAP), Email (SMTP), Outlook |
| cloud_storage | Google Drive, Google Docs, Google Sheets, Dropbox, OneDrive, Box |
| database | PostgreSQL, MySQL, MongoDB, Redis, Airtable, Notion |
| project_management | Jira, GitHub, GitLab, Trello, Asana, Monday.com |
| ai_ml | OpenAI, Anthropic, Hugging Face, CalcsLive |
| social_media | LinkedIn, Twitter/X, Facebook, Instagram |
| ecommerce | Shopify, Stripe, PayPal |
| analytics | Google Analytics, Mixpanel |
| calendar_tasks | Google Calendar, Google Tasks, Cal.com, Calendly |
| forms | Typeform, Google Forms, Form Trigger |
| development | Webhook, HTTP Request, GraphQL, Server-Sent Events, YouTube |

## 2. The Complete 188-Folder List

Activecampaign, Acuityscheduling, Affinity, Aggregate, Airtable, Airtabletool, Airtoptool, Amqp, Apitemplateio, Asana, Automate, Automation, Autopilot, Awsrekognition, Awss3, Awssns, Awstextract, Bannerbear, Baserow, Beeminder, Bitbucket, Bitly, Bitwarden, Box, Calcslive, Calendly, Chargebee, Clickup, Clockify, Code, Coingecko, Comparedatasets, Compression, Convertkit, Converttofile, Copper, Cortex, Create, Cron, Crypto, Customerio, Datetime, Debughelper, Deep, Discord, Discordtool, Dropbox, Editimage, Elasticsearch, Emailreadimap, Emailsend, Emelia, Error, Eventbrite, Executecommand, Executeworkflow, Executiondata, Export, Extractfromfile, Facebook, Facebookleadads, Figma, Filter, Flow, Form, Functionitem, Getresponse, Github, Gitlab, Gmail, Gmailtool, Googleanalytics, Googlebigquery, Googlecalendar, Googlecalendartool, Googlecontacts, Googledocs, Googledrive, Googledrivetool, Googlesheets, Googlesheetstool, Googleslides, Googletasks, Googletaskstool, Googletranslate, Gotowebinar, Graphql, Grist, Gumroad, Helpscout, Http, Hubspot, Humanticai, Hunter, Intercom, Interval, Invoiceninja, Jira, Jiratool, Jotform, Keap, Lemlist, Limit, Linkedin, Localfile, Mailcheck, Mailchimp, Mailerlite, Mailjet, Manual, Markdown, Matrix, Mattermost, Mautic, Microsoftexcel, Microsoftonedrive, Microsoftoutlook, Microsofttodo, Mondaycom, Mongodbtool, Mqtt, Mysqltool, N8ntrainingcustomermessenger, Netlify, Nocodb, Noop, Notion, Odoo, Onfleet, Openai, Openweathermap, Paypal, Pipedrive, Postgres, Postgrestool, Posthog, Postmark, Process, Quickbooks, Raindrop, Readbinaryfile, Readbinaryfiles, Redis, Removeduplicates, Respondtowebhook, Rssfeedread, Schedule, Send, Shopify, Signl4, Slack, Splitinbatches, Splitout, Sse, Stickynote, Stopanderror, Strapi, Summarize, Supabase, Surveymonkey, Taiga, Telegram, Telegramtool, Templates, Thehive, Todoist, Toggl, Travisci, Trello, Twilio, Twitter, Twittertool, Typeform, Uptimerobot, Wait, Webflow, Webhook, Whatsapp, Wise, Woocommerce, Woocommercetool, Wordpress, Writebinaryfile, Wufoo, Xml, Youtube, Zendesk, Zohocrm

Naming patterns decoded: a bare brand folder = classic usage; `*tool` suffix = the AI-agent "tool" variant of that node (Telegramtool, Github tool-style agent integrations); core-node folders (Aggregate, Code, Filter, Schedule, Webhook, Stickynote, etc.) = workflows whose identity is built around that primitive.

## 3. Frequency Tiers (approximate workflow counts)

### Tier 1 — Ecosystem Anchors (>300 each)
- **Telegram (~2,700)** — by far the dominant delivery channel; bots are n8n's killer app
- **OpenAI (~970)** — every second new workflow adds an LLM step
- **Webhook (~800)** — the universal entry point
- **Slack (~550)** — the B2B notification standard
- **Google Sheets (~450)** — the default small-business database
- **Gmail (~350)** — email triage/outreach backbone

### Tier 2 — Workhorses (100–300)
Notion (~250), Airtable (~200), Discord (~190), Google Drive (~180), plus heavy HTTP Request usage everywhere, Typeform, HubSpot, Google Calendar, Twilio, Trello, GitHub.

### Tier 3 — Specialists (<100 each)
Everything else: CRMs (Pipedrive, Zoho, Copper, Keap), finance (QuickBooks, Chargebee, Invoice Ninja, Wise, PayPal, CoinGecko), docs/e-sign adjacent (Google Docs/Slides, Bannerbear), data (BigQuery, Elasticsearch, Supabase, NocoDB, Baserow, Grist, Strapi), ops (UptimeRobot, SignL4, TheHive, Cortex), dev (Netlify, TravisCI, Bitbucket, AMQP/MQTT/SSE).

## 4. Credential Patterns — What You'll Need Per Tier

| Tier | Auth type | Setup friction | Client implication |
|---|---|---|---|
| Google stack | OAuth2 popup in n8n | Low once Google Cloud project exists | Budget 30 min first time per client |
| Telegram/Discord | Bot token from chat | Trivial (minutes) | Great for instant demos |
| OpenAI/Groq/Anthropic | API key | Trivial | Pass cost to client's account |
| Slack | OAuth2 app install | Medium (workspace approval) | IT may gate it in corporates |
| Meta platforms (FB/IG/LI ads) | App review + tokens | High, days of lead time | Start credential setup at kickoff, not delivery week |
| Stripe/PayPal webhooks | Signing secret + endpoint config | Medium | Test-mode first always |
| SQL databases | Host/user/password or connection string | Depends on their network access | Ask about VPN/IP allowlists on discovery calls |

Rule: your proposals should list required credentials as client homework with deadlines; credential waiting is the #1 timeline killer.

## 5. Combo Intelligence — Which Stacks Appear Together

Recurring triads in the corpus (from node co-occurrence across the tree):

1. **Form → Sheets → Telegram** — lead capture alerting (the starter client build)
2. **Webhook → OpenAI → Telegram/Slack** — AI assistant bots
3. **Schedule → API(s) → Sheets → Gmail** — reporting/digest engines
4. **IMAP → OpenAI → Sheets/CRM** — email triage pipelines
5. **GitHub → CI → Slack** — devOps release flows
6. **Typeform → HubSpot/Pipedrive → Calendly → Gmail** — sales funnels
7. **Shopify/WooCommerce → Sheets/Twilio** — order ops & SMS alerts
8. **RSS → OpenAI → WordPress/socials** — content repurposing

Each combo is a productizable template (see pricing file). If you master these eight shapes you can assemble 90% of small-business requests live on a call.

## 6. Strategic Selection for Your Service Menu

Don't learn 365 services. Build your menu around two axes: **demand frequency** (Tier 1–2 above) × **client budget** (who pays for that stack):

| Your offer | Stack to master | Buyer |
|---|---|---|
| AI chatbot/assistant | Telegram/Discord + OpenAI + webhook + Sheets | Coaches, communities, e-com support |
| Reporting retainers | Scheduled + GA/Ads APIs + Sheets + Slack/Gmail | Agencies, marketing teams |
| Sales pipeline glue | Typeform/FB Leads + CRM + Calendar + Gmail | Real estate, recruiters, consultants |
| Ops monitoring | HTTP/UptimeRobot + SignL4/TheHive + Slack | IT services, SaaS startups |
| Content engine | RSS + OpenAI + WordPress + LinkedIn/X | Creators, content agencies |

Depth beats breadth: five stacks done cold > fifty integrations half-known. The other 300+ services remain your lookup library when a niche client appears — clone the matching folder from the repo and adapt.
