# Starter Workflows — Copy, Import, Run

> Minimal valid n8n JSON skeletons. Import: canvas menu → **Import from File**, or copy JSON → paste onto empty canvas → re-link credentials → activate.

## 1. Webhook Lead Capture → Sheet + Telegram

The universal client demo. Replace `YOUR_CHAT_ID`, re-link Google Sheets + Telegram creds.

```json
{
  "name": "Lead Capture Basic",
  "nodes": [
    {
      "parameters": { "httpMethod": "POST", "path": "lead-capture", "responseMode": "onReceived" },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [250, 300],
      "webhookId": "lead-capture"
    },
    {
      "parameters": { "documentId": "REPLACE_SHEET_ID", "sheetName": "Leads", "columns": { "mappingMode": "autoMapInputData" } },
      "name": "Append Lead",
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.5,
      "position": [460, 300]
    },
    {
      "parameters": {
        "chatId": "=YOUR_CHAT_ID",
        "text": "=New lead!\nName: {{ $json.body.name }}\nEmail: {{ $json.body.email }}\nMessage: {{ $json.body.message }}"
      },
      "name": "Alert Me",
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [670, 300]
    }
  ],
  "connections": {
    "Webhook": { "main": [[{ "node": "Append Lead", "type": "main", "index": 0 }]] },
    "Append Lead": { "main": [[{ "node": "Alert Me", "type": "main", "index": 0 }]] }
  },
  "settings": {}
}
```

Test:
```powershell
curl.exe -X POST "http://localhost:5678/webhook/lead-capture" -H "Content-Type: application/json" -d '{\"name\":\"Test\",\"email\":\"t@x.com\",\"message\":\"hello\"}'
```

## 2. Daily Briefing (Schedule → Weather + AI → Telegram)

```json
{
  "name": "Morning Briefing v1",
  "nodes": [
    {
      "parameters": { "rule": { "interval": [{ "triggerAtHour": 7 }] } },
      "name": "Every Day 7am",
      "type": "n8n-nodes-base.scheduleTrigger",
      "typeVersion": 1.2,
      "position": [250, 300]
    },
    {
      "parameters": { "url": "=https://api.open-meteo.com/v1/forecast?latitude=12.97&longitude=77.59&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=auto" },
      "name": "Weather",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [450, 300]
    },
    {
      "parameters": {
        "promptType": "define",
        "text": "=Write a short friendly morning briefing. Weather data: {{ JSON.stringify($json.daily) }}. Max 5 lines, mention umbrella if rain > 0."
      },
      "name": "AI Writer",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [650, 300]
    },
    {
      "parameters": { "chatId": "=YOUR_CHAT_ID", "text": "={{ $json.message?.content || $json.output || 'briefing ready' }}" },
      "name": "Send Brief",
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [850, 300]
    }
  ],
  "connections": {
    "Every Day 7am": { "main": [[{ "node": "Weather", "type": "main", "index": 0 }]] },
    "Weather": { "main": [[{ "node": "AI Writer", "type": "main", "index": 0 }]] },
    "AI Writer": { "main": [[{ "node": "Send Brief", "type": "main", "index": 0 }]] }
  },
  "settings": {}
}
```

Adjust latitude/longitude to your city (example: Bengaluru). If the OpenAI node shape differs in your n8n version, swap in any LLM node — the wiring stays identical.

## 3. Error Watchdog (attach to any workflow)

Create once; reference from every workflow's Settings → Error Workflow.

```json
{
  "name": "SYSTEM | error-watchdog",
  "nodes": [
    {
      "parameters": {},
      "name": "Error Trigger",
      "type": "n8n-nodes-base.errorTrigger",
      "typeVersion": 1,
      "position": [250, 300]
    },
    {
      "parameters": {
        "chatId": "=YOUR_CHAT_ID",
        "text": "=WORKFLOW FAILED\nWorkflow: {{ $json.workflow.name }}\nNode: {{ $json.execution.lastNodeExecuted }}\nError: {{ $json.execution.error.message }}"
      },
      "name": "Ping Me",
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [450, 300]
    }
  ],
  "connections": {
    "Error Trigger": { "main": [[{ "node": "Ping Me", "type": "main", "index": 0 }]] }
  },
  "settings": {}
}
```

## 4. Weekly Content Repurposer (RSS → AI drafts)

```json
{
  "name": "Weekly Content Engine",
  "nodes": [
    {
      "parameters": { "rule": { "interval": [{ "field": "weeks", "triggerAtDay": [1], "triggerAtHour": 9 }] } },
      "name": "Monday 9am",
      "type": "n8n-nodes-base.scheduleTrigger",
      "typeVersion": 1.2,
      "position": [200, 300]
    },
    {
      "parameters": { "url": "https://yourblog.example/feed.xml", "options": {} },
      "name": "Blog RSS",
      "type": "n8n-nodes-base.rssFeedRead",
      "typeVersion": 1.1,
      "position": [400, 300]
    },
    {
      "parameters": {
        "promptType": "define",
        "text": "=Turn this blog post into: 1 LinkedIn post (hook + insight + CTA) and 1 X thread (5 tweets).\nTitle: {{ $json.title }}\nContent: {{ $json.contentSnippet }}"
      },
      "name": "Draft Posts",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [600, 300]
    },
    {
      "parameters": { "operation": "appendOrUpdateDocument", "documentId": "REPLACE_SHEET_ID", "sheetName": "Content Queue" },
      "name": "Queue for Review",
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.5,
      "position": [800, 300]
    }
  ],
  "connections": {
    "Monday 9am": { "main": [[{ "node": "Blog RSS", "type": "main", "index": 0 }]] },
    "Blog RSS": { "main": [[{ "node": "Draft Posts", "type": "main", "index": 0 }]] },
    "Draft Posts": { "main": [[{ "node": "Queue for Review", "type": "main", "index": 0 }]] }
  },
  "settings": {}
}
```

## Import Checklist (every time)

- [ ] All red nodes re-credentialed
- [ ] Test mode first: manual execution with sample data
- [ ] Webhook paths renamed to something private
- [ ] Timezone checked (`Settings` or `GENERIC_TIMEZONE`)
- [ ] Error workflow attached
- [ ] Export your customized version back into `templates/` with a `_v1` suffix
