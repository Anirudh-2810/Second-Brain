# Category Deep-Dive: DevOps & IT Automation

> ~300 workflows in the source library fall here. DevOps clients pay well because downtime costs them money per minute.

## Why This Niche Pays

- Pain is measurable (uptime, MTTR, missed backups)
- Buyers are technical → shorter sales cycles, less hand-holding
- Retainers natural: "monitoring as a service"

## Workflow Recipes

### 1. Uptime Sentinel — E
Schedule (*/5 min) → HTTP Request ping list of URLs from Sheet → status != 200 or timeout → Telegram/Slack alert with URL + code + last-seen-ok time. Recovery message on return.
**Sell:** $99–199/mo per client, near-zero maintenance.

### 2. SSL & Domain Expiry Watchdog — E
Daily cron → check cert expiry via `https://...` response headers or SSL APIs → alert at 30/14/7/1 days. Same sheet pattern for domain renewals.

### 3. Backup Verification (not just backup) — M
After nightly backup job → n8n checks file size delta / restore-test flag / row count in DB dump manifest → success tick to channel; anomaly = page the owner.
**Key insight:** unverified backups fail silently; verification is the sellable part.

### 4. Deployment Notifier — E
GitHub/GitLab webhook (`push` to `main`) → parse commits → format release note → post to Slack/Teams/Discord with author + diff link + build status placeholder.
Extend: after CI webhook success/fail → update the same thread (human-friendly deploy trail).

### 5. Log Triage Digest — M
Cron hourly → pull error lines from log API (Loki/Datadog/CloudWatch) grouped by fingerprint → AI node clusters and summarizes top 3 recurring errors → digest to #eng-alerts only when new fingerprints appear (dedupe via Redis/Set node).

### 6. Container Health Loop — A
Cron → SSH/HTTP to Docker host or portainer API → list containers → any `unhealthy`/`exited` → attempt restart endpoint → if still down after 2 tries → escalate Telegram + create incident row.
**Caution:** auto-restart needs guardrails; log every action.

### 7. Disk Space Canary — E
Cron daily on VPS (via Execute Command node locally, or small agent script) → df output parsed → threshold breach → alert with cleanup suggestions. Prevents the classic "disk full at 3am" outage.

### 8. Incident Postmortem Collector — A
Incident channel message reaction `:postmortem:` → workflow collects timeline messages, alerts fired, resolution commit links → drafts postmortem doc in Notion/Google Docs → review task assigned.

## Common Node Stack

| Need | Node |
|---|---|
| Polling | Schedule Trigger + HTTP Request |
| Alerts | Telegram / Slack / Discord |
| State/dedupe | Redis, or Google Sheets as poor-man's store |
| SSH-ish tasks | Execute Command (local) / HTTP to agent |
| Parsing | Code node (JS), Item Lists |

## Client Pitch Angle

"Your systems already email you when things break — after you've lost the logs. I flip it: you get paged before customers notice, and everything lands in one place."
Package anchor: setup $397–697 + Monitor retainer $149/mo (see pricing file).

## Gotchas

- Alert fatigue kills trust: always dedupe + batch before notifying
- Never hardcode prod tokens in Code nodes — credentials only
- Rate-limit friendly polling intervals (5 min fine for uptime; 60 s only if paid)
