---
course_code: "BUILDS"
course_name: "Builds Domain Index (Your Active Projects)"
unit: "Domain Hub"
tags: [builds, projects, portfolio, index, domain-hub]
last_updated: "2026-08-26"
confidence: high
description: "BUILDS domain hub - YOUR active builds: stock-agent trading platform, retrieval-agent RAG brain, GitHub portfolio projects. Scan THIS folder for questions about your own systems."
---

## For future agent
**DOMAIN SCOPE**: Questions about the user's OWN built systems (stock-agent architecture/bugs/roadmap, the retrieval-agent business brain, GitHub portfolio repos) → scan `wiki/00-Current-Projects/**`. These are LIVING documents — update them as the builds evolve.

# Builds Domain — Your Active Systems

## Sub-modules

| Module | Pages | Status |
|--------|-------|--------|
| [[stock-agent/overview|stock-agent/]] | 8 | Alpaca paper-trading platform (FastAPI+React+ML): deep review w/ 18 verified bugs, architecture, improvement roadmap P0–P3, interview-prep guide |
| [[retrieval-agent/overview|retrieval-agent/]] | 5 | The RAG "business brain": n8n + Supabase Edge Function + pgvector. Full n8n-setup/edge-function/schema docs |
| [[projects/index|projects/]] | 4 | GitHub portfolio: StockOffline inventory system, AURA trend engine, handsens101 gesture control |
| [[neural-engine|neural-engine]] | 1 | From-scratch NumPy neural network library (SGD/Adam/AdamW/RMSprop, dropout, L2, early stopping, save/load) |
| [[stock-predictor|stock-predictor]] | 1 | S&P 500 direction forecasting pipeline (yfinance → 20+ indicators → NeuralEngine → trading sim) |
| [[aerofuse|aerofuse]] | 1 | ROS2 odometry diagnostic dashboard: dual-path trajectory, covariance heatmap, live Q/R tuning |
| [[web-access-ai|web-access-ai]] | 1 | Streamlit chatbot: live DuckDuckGo search, tools (calc/code/weather), PDF reading, memory |
| [[quote-pomodoro|quote-pomodoro]] | 1 | Tkinter Pomodoro timer: dark theme, quotes, beeps, notifications, presets |
| [[react-calculator|react-calculator]] | 1 | React + Tailwind calculator: keyboard support, history, Lucide icons, gradient UI |
| [[budget-tracker|budget-tracker]] | 1 | Excel/VBA Budget vs Actual vs Variance + Executive Dashboard (Mac/Win compatible) |

## Quick Answers

- "What's wrong with stock-agent?" → [[deep-review-report]], [[improvement-roadmap]]
- "How does my RAG brain work?" → retrieval-agent/overview + edge-function
- "What do I show recruiters?" → [[projects/index]] + stock-agent interview-prep-guide

## NOT Here

How to BUILD projects generally → [[build-project-playbook]] (business) · Reference architectures studied → `wiki/01-Areas/Programming/case-studies/`

## Cross-Domain Bridges

stock-agent ML internals ↔ ai-data · quant strategies ↔ business/quant-finance · interview stories ↔ [[interview-counter-guide]] · Roadmaps hub: [[01-Areas/Roadmaps/INDEX]]

**Update discipline**: after every build session, update these pages BEFORE committing code ([[build-project-playbook]] README contract).