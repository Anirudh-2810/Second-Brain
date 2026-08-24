# Client Acquisition Playbook

> System for finding businesses that will pay for automation. Core insight: sell *removed pain*, not "n8n workflows".

## 1. Pick a Niche (do this first)

| Niche | Painful manual task | Workflow to sell | Price anchor |
|---|---|---|---|
| Real estate agents | Chasing leads across portals | Lead → instant SMS + CRM + follow-up sequence | $497 + $99/mo |
| E-com store owners | Order/review/inventory juggling | Order digest, review requests, low-stock alerts | $397–$997 |
| Coaches/course creators | DMs, scheduling, onboarding | Booking → welcome email series → reminder bot | $297 + $79/mo |
| Recruiters | Screening floods of CVs | Resume intake → AI screening score → shortlist | $697 setup |
| Agencies | Client reporting every Monday | Auto weekly performance report to Slack/email | $499 + $149/mo |
| Clinics/gyms | No-shows | Reminder cascade via WhatsApp/Telegram | $297 + $59/mo |

Rule: choose the niche you can name 20 real businesses in.

## 2. Where They Hang Out

- Upwork/Fiverr (active buyers — fastest)
- LinkedIn search: job title + "operations" / "founder"
- Facebook groups for the niche ("Real Estate Agents Mastermind")
- Reddit: r/smallbusiness, r/ecommerce, niche subreddits
- Local: Google Maps → businesses with active ads but clunky sites
- Your own network: everyone knows a business owner drowning in manual work

## 3. Outreach Scripts

### Cold Email A (audit offer)
Subject: quick question about {{Business}}

Hi {{Name}} — noticed your team handles {{manual task}} manually
(saw it on {{specific observation}}).

I build small automations that remove exactly this. Happy to send a
2-min video showing what it would look like for {{Business}} — free,
no strings.

Worth a look?

{{Your name}}

### Cold Email B (result-first)
Subject: saved {{similar business}} ~10 hrs/month

Hi {{Name}} — I recently built an automation for {{analogous task}}
that saves {{hours}} hours monthly. Recording here: {{Loom link}}.

If useful, I can map the same flow to your process. Free audit,
reply "send it" and I'll record it.

### LinkedIn DM (short)
Hi {{Name}} — do you still handle {{task}} by hand? I automate that
for {{niche}} owners (recent example: {{one-liner}}). Want me to send
a free walkthrough video?

### Follow-up 1 (day 3)
Adding the 2-min demo I mentioned: {{link}}. If now's not the time,
all good — should I check back next quarter?

### Follow-up 2 (day 7, breakup)
Closing the loop on this — I'll stop emailing. If {{task}} ever
becomes a bottleneck, my calendar is here: {{link}}.

## 4. Community Posts That Convert (r/n8n etc.)

Structure: problem you solved → screenshot/GIF of canvas → what it saves → "happy to share the template". Never lead with selling; the DMs come to you.

## 5. Discovery Call Script (15 min)

1. "Walk me through how {{task}} works today, step by step." (listen)
2. "How often does this happen? Who does it?"
3. "What breaks or gets dropped?"
4. "What would it mean for the business if this ran itself?" (value framing)
5. "Who else needs to approve something like this?"
6. "Budget range you had in mind for removing this entirely?"

Then: summarize their words back, propose the smallest workflow that removes the biggest pain.

## 6. Proposal Template (send within 24 h)

```
Goal: replace {{manual process}} with an automated workflow.
Deliverables:
 - Workflow handling X → Y → Z (list steps from call)
 - Error alerts to your inbox/Telegram
 - 1 revision round + handoff video
Timeline: X days from kickoff payment.
Price: $______ (50% to start, 50% at handoff)
Optional care plan: $____/mo — monitoring, fixes, minor tweaks.
Payment link: [Stripe]
```

## 7. Objection Handling

| Objection | Response |
|---|---|
| "Too expensive" | Compare against salary-hours saved × 12 months; offer smaller phase 1 |
| "Can't I use Zapier myself?" | "Yes — and many pay after hitting task limits. I design, build, monitor, own the outcome." |
| "Is my data safe?" | Self-hosted instance, credentials encrypted, least-privilege keys (see security checklist in catalog) |
| "Let me think" | Book explicit follow-up date before ending call |

## 8. Red Flags (walk away)

- No clear owner for the process on their side
- Wants "everything automated" vague mega-scope on small budget
- Refuses upfront payment
- Requests access violating platform ToS (fake engagement, scraping gated data)

## 9. After Delivery = Next Sale

Every handoff meeting ends with: "What's the second most annoying manual thing here?" That question converts delivered clients into retainer clients.
