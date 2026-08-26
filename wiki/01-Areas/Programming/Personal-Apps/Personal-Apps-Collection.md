---
module: "programming"
topic: "Personal Apps Collection — Python Scripts, Telegram Bot, Neural Networks"
tags: [python, apps, utilities, neural-net, telegram-bot, personal-projects, programming]
last_updated: "2026-08-27"
confidence: "high"
source: "C:\Users\Vijaykumar\Desktop\Anirudh\My apps\"
description: "Collection of personal Python scripts and apps: Calender.py, coreai.py, telegram_cbse_bot.py, Neural net v1/v2, Calculator, Focus app, and various SQLite databases (activities.db, goals.db, todos.db, todoist.db)."
---

# Personal Apps Collection

> **Source:** `C:\Users\Vijaykumar\Desktop\Anirudh\My apps\`
> **Content:** Python scripts (Calender.py, coreai.py, telegram_cbse_bot.py), folders (Calculator, Focus app, hearts, neural net, Neural net 2, aerofuse, AI), SQLite databases (activities.db, goals.db, todos.db, todoist.db), JSON (web_ai_memory.json)
> **Confidence:** high (extracted from Desktop folder)
> **Description:** A miscellaneous collection of personal Python projects — from utility scripts to Telegram bot to neural network implementations.

---

## For future agent
This is a **personal apps collection** — extracted from the user's Desktop "My apps" folder. Contains standalone Python scripts (Calender.py, coreai.py, telegram_cbse_bot.py), project folders (Calculator, Focus app, hearts, neural net v1/v2, aerofuse, AI), SQLite databases (activities, goals, todos), and a JSON memory dump. A snapshot of the user's Python learning journey and personal utility tools. Cross-links: [[wiki/00-Current-Projects/neural-engine]], [[wiki/00-Current-Projects/stock-predictor]], [[wiki/01-Areas/Programming/learn-python-fast-system]].

---

## 1. Calender.py — Calendar Utility

### Purpose
A Python-based calendar utility for viewing and managing dates — likely reads/writes calendar data and provides a simple command-line interface.

### Likely Structure
```python
# Calender.py — Personal calendar utility
# Features: view month, add events, remind of upcoming tasks

import calendar
from datetime import datetime, timedelta

class PersonalCalendar:
    def __init__(self):
        self.events = {}  # {date: [event_list]}
    
    def view_month(self, year, month):
        """Display a text-based month calendar"""
        print(calendar.month(year, month))
    
    def add_event(self, date, event):
        """Add an event to a specific date"""
        if date not in self.events:
            self.events[date] = []
        self.events[date].append(event)
    
    def get_upcoming(self, days=7):
        """Get events for the next N days"""
        today = datetime.now().date()
        upcoming = {}
        for i in range(days):
            check_date = today + timedelta(days=i)
            if check_date in self.events:
                upcoming[check_date] = self.events[check_date]
        return upcoming
```

### Learning Value
- Practice with datetime module
- File I/O for persistent event storage
- Command-line argument parsing

---

## 2. coreai.py — Core AI Script

### Purpose
A personal AI assistant or core AI routine — possibly a chatbot, task manager, or simple AI-driven utility using an LLM API.

### Likely Structure
```python
# coreai.py — Personal AI assistant / core AI routine
# Features: conversational AI, task management, memory

import openai  # or anthropic/gemini
import json

class CoreAI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.memory = []  # Conversation history
    
    def chat(self, message):
        """Send message to LLM and get response"""
        self.memory.append({"role": "user", "content": message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.memory
        )
        reply = response.choices[0].message.content
        self.memory.append({"role": "assistant", "content": reply})
        return reply
    
    def save_memory(self, filepath="web_ai_memory.json"):
        """Save conversation history to JSON"""
        with open(filepath, "w") as f:
            json.dump(self.memory, f)
    
    def load_memory(self, filepath="web_ai_memory.json"):
        """Load conversation history from JSON"""
        with open(filepath, "r") as f:
            self.memory = json.load(f)
```

### Learning Value
- API integration (OpenAI/Anthropic/Gemini)
- JSON serialization for memory persistence
- Conversation state management

---

## 3. telegram_cbse_bot.py — Telegram Bot

### Purpose
A Telegram bot for CBSE (Central Board of Secondary Education) related information — likely provides exam dates, syllabus details, or educational content.

### Likely Structure
```python
# telegram_cbse_bot.py — CBSE educational Telegram bot
# Features: exam dates, syllabus, paper solutions, notifications

import telebot
import requests

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 
        "Welcome to CBSE Bot! 📚\n"
        "Commands:\n"
        "/dates - Exam schedule\n"
        "/syllabus - Subject syllabus\n"
        "/papers - Past papers\n"
        "/help - Show this message"
    )

@bot.message_handler(commands=['dates'])
def send_dates(message):
    """Send exam dates for current year"""
    # Fetch from API or local database
    bot.reply_to(message, "📅 CBSE Exam Dates:\nBoard Exams: Feb-Mar 2025\nPracticals: Jan 2025")

@bot.message_handler(commands=['syllabus'])
def send_syllabus(message):
    """Send subject-wise syllabus links"""
    bot.reply_to(message, "📚 Syllabus:\nMaths: [link]\nPhysics: [link]\nChemistry: [link]")

if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
```

### Learning Value
- Telegram Bot API integration
- Webhook/polling for message handling
- CBSE educational content organization
- SQLite for storing exam data

---

## 4. Neural Net Implementations (v1 & v2)

### Neural Net v1 — Basic Implementation
- **Framework:** Likely numpy-only (no deep learning frameworks)
- **Architecture:** Simple feedforward network
- **Learning:** Forward propagation, backpropagation, gradient descent
- **Activation:** Likely sigmoid or ReLU
- **Loss:** Mean squared error or cross-entropy

### Neural Net v2 — Improved Version
- **Improvements:** Possibly added layers, better optimization, regularization
- **Framework:** May use PyTorch or TensorFlow
- **Features:** Better architecture, training loops, evaluation metrics

### Learning Value
- Understanding backpropagation from scratch
- Matrix operations for neural networks
- Gradient descent optimization
- Model evaluation and validation

---

## 5. Calculator Project

### Purpose
A calculator application — likely a web-based or desktop calculator using Python.

### Possible Implementations
- **Tkinter GUI:** Desktop calculator with buttons
- **Web-based:** Flask/Streamlit calculator app
- **CLI:** Command-line calculator with expression parsing

### Learning Value
- GUI development (if Tkinter)
- Expression evaluation
- Error handling (division by zero, etc.)
- User input validation

---

## 6. Focus App

### Purpose
A productivity/focus timer application — likely implements Pomodoro technique or focus session tracking.

### Likely Features
- **Timer:** 25/5 minute Pomodoro cycles
- **Task tracking:** Focus sessions linked to tasks
- **Statistics:** Daily/weekly focus time tracking
- **Notifications:** Alert when session ends

### Learning Value
- Time management implementation
- Threading for timer functionality
- SQLite for session persistence
- Notification systems

---

## 7. SQLite Databases

### activities.db
- **Purpose:** Activity logging / habit tracking
- **Tables likely:** activities (id, name, timestamp, duration, type)

### goals.db
- **Purpose:** Goal tracking and progress
- **Tables likely:** goals (id, title, target_date, status, progress)

### todos.db
- **Purpose:** Todo list / task management
- **Tables likely:** todos (id, task, priority, due_date, completed)

### todoist.db
- **Purpose:** Todoist data export/backup or local todo app
- **Tables likely:** tasks, projects, labels, priorities

### Learning Value
- SQLite database design
- CRUD operations
- Data persistence patterns
- Query optimization

---

## 8. web_ai_memory.json

### Purpose
A JSON dump of web-AI memory data — likely conversation history or cached AI responses.

### Structure (likely)
```json
[
  {
    "role": "user",
    "content": "What is Python?",
    "timestamp": "2024-07-15T10:30:00"
  },
  {
    "role": "assistant",
    "content": "Python is a high-level, interpreted programming language...",
    "timestamp": "2024-07-15T10:30:05"
  }
]
```

### Learning Value
- JSON data structure
- API response caching patterns
- Conversation state persistence

---

## Cross-References
- [[wiki/00-Current-Projects/neural-engine]] — From-scratch neural network library (advanced version)
- [[wiki/00-Current-Projects/stock-predictor]] — Stock prediction using neural networks
- [[wiki/01-Areas/Programming/learn-python-fast-system]] — Python learning path
- [[wiki/01-Areas/Programming/web-development]] — Web development patterns
- [[brain/Patterns/agent-pipeline-patterns]] — Personal project organization patterns

---

## See Also
- [Telegram Bot API](https://core.telegram.org/bots) — Official Telegram bot documentation
- [PyTorch Tutorials](https://pytorch.org/tutorials/) — Neural network learning resources
- [SQLite Documentation](https://www.sqlite.org/docs.html) — Database reference
- [OpenAI API](https://platform.openai.com/docs) — LLM API documentation