Site:
https://odincoinofficial.github.io/ODIN_INTELLIGENCE_BOT/site/index.html
# ODIN COIN OSINT Telegram Bot

OSINT-бот для Telegram, реализованный на Python с использованием aiogram.

## Возможности

- Поиск по email, IP, username, домену, телефону
- Генерация PDF-отчёта
- Симуляция поиска в darknet
- Telegram ID, social профили, /report и /pdfreport

## Команды

- `/start` — Приветствие
- `/email someone@example.com` — Проверка email
- `/ip 1.2.3.4` — Информация об IP
- `/phone +1234567890` — Проверка телефона
- `/user username` — Проверка username
- `/domain example.com` — WHOIS
- `/tgid` — Telegram ID
- `/social username` — Поиск профилей
- `/darknet keyword` — Поиск в Даркнете (эмуляция)
- `/report target` — OSINT-отчёт
- `/pdfreport target` — PDF-отчёт

---

## Установка локально

```bash
git clone https://github.com/yourusername/osint-bot.git
cd osint-bot
pip install -r requirements.txt
cp .env.example .env
# Вставь свой токен в .env
python bot.py
```

---

## Развёртывание на Railway

1. Перейди на [https://railway.app](https://railway.app)
2. Создай проект из GitHub репозитория
3. В разделе **Variables** добавь:
   - `BOT_TOKEN=...`
4. Railway сам запустит `bot.py`

---

## Пример PDF

В результате команды `/pdfreport target@example.com` пользователь получит сгенерированный PDF с OSINT-данными.

---

## Требования

- Python 3.10+
- Библиотеки: aiogram, python-dotenv, requests, fpdf

---

## Безопасность

**Никогда не публикуй `.env` с токеном.** Используй `.env.example` как шаблон.
