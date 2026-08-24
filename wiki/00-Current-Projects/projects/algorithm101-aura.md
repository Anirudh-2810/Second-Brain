---
course_code: "PROJECT"
course_name: "Portfolio Projects"
unit: "Algorithm101"
tags: [project, github, fastapi, react, mongodb, youtube-api, prediction, portfolio]
last_updated: "2026-08-23"
confidence: stated
relations:
  applies_concepts_from: "[[momentum-jegadeesh-titman]]"
  relates_to: "[[stock-agent/overview|Stock-Agent Overview]]"
---

## For future agent
This note catalogs the owner's GitHub repo **Algorithm101 (AURA — Neural Trend Engine)**, extracted from its README/PRD/source on 2026-08-23. Use it for questions about the music-trend prediction dashboard's stack and scoring approach; note the README itself is a placeholder ("Here are your Instructions") — the PRD is the real doc.

# AURA — Neural Trend Engine (`Algorithm101`)

**Repo:** https://github.com/Anirudh-2810/Algorithm101 · JavaScript/Python · updated Mar 2026

Full-stack **music trend intelligence** app: fetches live YouTube trending data across 3 time windows, classifies genres, forecasts trajectories, predicts which songs go viral next week. Built via Emergent bootstrap (Node prototype → React+FastAPI port).

## Stack
- **Frontend:** React 19 + Tailwind + Recharts + Lucide; 7 viz components (RnnBars, GenreChart, HypeChart, PredictionGrid, TrendForecast, TopShorts, ScanHistory); DM Mono/Syne dark glass-morphism theme
- **Backend:** FastAPI + httpx async + Motor (async MongoDB); endpoints `/api/analyze-trend`, `/api/scan-history`, `/api/health`
- **Data:** YouTube Data API v3 (4 parallel fetch windows); MongoDB scan history

## Signal machinery (the interesting part)
- Genre classification: multi-signal regex over title + channel + description + tags
- **Engagement scoring + velocity scoring**
- 3-window forecasting (now vs 1mo vs 3mo)
- Viral prediction via composite score
- "RNN hidden state" animated visualization

## Status (as of Jan 2026 per PRD)
All core requirements checked, tests passing 100%. Backlog: auto-refresh, click-through to video, scan comparison, genre filters, user accounts.

## Why it matters (my read)
This is secretly a quant project wearing a music costume — velocity/composite scoring and short-horizon trend forecasting are the same DNA as momentum strategies in [[momentum-jegadeesh-titman]] and the signal layer of [[stock-agent/overview|the stock-agent]]. Reusable patterns for the stock-agent: parallel API windows, async persistence of scans, composite-score ranking UI.
