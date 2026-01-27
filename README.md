# Telegram-Integrated Visitor Tracker for Flask

A lightweight, server-side monitoring module designed for Python web applications. This script enables real-time visitor notifications via Telegram Bot API, providing insights into visitor IP addresses, ISP, and approximate geographic locations.

## 🌟 Features
* **Real-time Alerts:** Instant Telegram notifications upon page access.
* **Geolocation Insights:** Automatically fetches city, country, and ISP data using IP-API.
* **Non-Blocking Logic:** Implemented with error handling to ensure the main web application remains functional even if the tracking API or Telegram is unreachable.
* **Formal Reporting:** Structured notification format for professional monitoring.

## 🛠️ Tech Stack
* **Language:** Python
* **Framework:** Flask / Django (Logic is portable to any Python-based backend)
* **Libraries:** `requests`

## 🚀 Installation & Setup

### 1. Telegram Bot Configuration
To use this module, you need a Telegram Bot:
1. **Create a Bot:** Chat with [@BotFather](https://t.me/botfather) on Telegram, use the `/newbot` command, and save your **API Token**.
2. **Get Your Chat ID:** Chat with [@userinfobot](https://t.me/userinfobot) to retrieve your unique **User ID**.

### 2. Integration
Paste the provided snippet into your main application file (e.g., `app.py`). Ensure you have the `requests` library installed:
```bash
pip install requests
```

## ⚠️ Important Disclaimers

1. Accuracy & Geolocation Privacy
   
This tool identifies locations based on the ISP's network routing—representing the regional "Point of Presence" rather than exact GPS coordinates—which means a visitor in Indramayu might be detected in Sumedang depending on how their provider routes traffic at the network information level.

2. Compatibility & Requirements
   
This is a Python-specific module. It is designed to work with:
Flask (as demonstrated in app_snippet.py)
Django
Any Python backend environment.
Note: This will not function on static HTML sites or PHP/Node.js without translating the logic into those respective languages.


3. Educational Purposes Only
   
This project is developed for educational and portfolio purposes to demonstrate API integration and backend logic.
Users are responsible for complying with local privacy laws (such as GDPR or CCPA) regarding the collection of IP data.
Use this tool ethically and responsibly.


## 🛡️ Security Best Practice

[!IMPORTANT] Do not hardcode your actual Token and Chat ID when pushing to public repositories.
Always use Environment Variables or placeholders as demonstrated in this repository to prevent unauthorized access to your Bot.
