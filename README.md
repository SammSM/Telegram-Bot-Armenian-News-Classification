# Telegram-Bot-Armenian-News-Classification
A Telegram bot that predicts Armenian news category. This bot delivers quick and relevant results directly in Telegram.

This bot uses a machine learning model based on Random Forest to automatically predict the category of a given news article. Just send a short news text, and the bot will classify the category.

###!Provided articles should be in Armenian language.
Categories:
- Քաղաքական
- Հասարակական
- Կրթական
- Առոջապահական
---

## ⚙️ How It Works

- The input text is processed and transformed into numerical features (TfidfVectorizer is used).
- Random Forest Classifier model analyzes these features.
- The bot returns the most likely news category based on learned patterns from training data.

---

## 🛠️ Setup Guide

## 1. Clone the repository
Open your environment and clone the repository
```bash
https://github.com/SammSM/Telegram-Bot-Armenian-News-Classification.git
```
## 2. Change to Telegram-Bot-Armenian-News-Classification directory
```bash
cd Telegram-Bot-Armenian-News-Classification
```

## 4. Create a virtual environment and activate it

- ### Create a virtual environment
On Windows:
```bash
python -m venv venv
```
On macOS / Linux:
```bash
python3 -m venv venv
```
- ### Activate the virtual environment
On Windows:
```bash
venv\Scripts\activate
```
On macOS / Linux:
```bash
source venv/bin/activate
```

## 5. Install PIP package manager for Python
```bash
py -m pip install --upgrade pip
```
### Or
```bash
python -m pip install --upgrade pip
```

## 6. Install requirements
```bash
pip install -r requirements.txt
```

## 7. Get token from BotFather in Telegram.
- Enter /start in BotFather and follow the instruction
- Paste the generated token in news_bot.py

## 8. Run news_bot.py
```bash
py news_bot.py
```
Open the bot and enter /start
