# Telegram Price Tracker Bot

This repository contains a simple Telegram bot that monitors the price of a product on an e‑commerce site and notifies you when the price drops.  The bot is written in Python using the [`aiogram`](https://docs.aiogram.dev) framework for Telegram bots and the [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/) library for HTML parsing.  It periodically downloads the product page, extracts the current price and compares it to the last known price.  If the price decreases, the bot sends a message to the configured chat.

## Цель

— **Автоматизация отслеживания цены**.  Бот облегчает контроль стоимости товара на сайте (например, Ozon или Wildberries) и мгновенно уведомляет о снижении.  Это экономит время и позволяет купить товар по лучшей цене.

## Стек технологий

* **Python 3** – основной язык разработки.
* **aiogram 3** – асинхронный фреймворк для работы с Telegram Bot API.
* **aiohttp** – асинхронный HTTP‑клиент для скачивания страниц.
* **BeautifulSoup 4** – парсер HTML для извлечения цены.
* **SQLite** – небольшая база данных для хранения последней известной цены (можно заменить на файл).

## Установка

1. Клонируйте репозиторий и перейдите в папку проекта:

   ```bash
   git clone https://github.com/your‑username/telegram-price-tracker.git
   cd telegram-price-tracker
   ```

2. Создайте виртуальное окружение и установите зависимости:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Создайте бота через [@BotFather](https://t.me/BotFather) и получите токен.  Узнайте свой `chat_id`, которому бот будет отправлять уведомления (например, с помощью бота [@userinfobot](https://t.me/userinfobot)).

4. Настройте переменные окружения (можно создать файл `.env`):
   - `BOT_TOKEN` – токен вашего бота
   - `CHAT_ID` – ID чата для отправки уведомлений
   - `PRODUCT_URL` – ссылка на страницу товара
   - `PRICE_SELECTOR` – CSS‑селектор элемента с ценой (например, `span.price`)
   - `CHECK_INTERVAL` – интервал проверки в секундах (по умолчанию час)

5. Запустите бота:

   ```bash
   python main.py
   ```

## Пример запуска

В примере ниже бот настроен на отслеживание цены из примера `data/sample_product.html`.  При первом запуске он сохраняет текущую цену, затем при обнаружении снижения отправляет уведомление:

```bash
export BOT_TOKEN="<ваш токен>"
export CHAT_ID="<ваш chat_id>"
export PRODUCT_URL="file://$PWD/data/sample_product.html"
export PRICE_SELECTOR="span.price"
python main.py
```## Для разворачивания бота на сервере часто используют вебхуки.  Документация aiogram подчёркивает, что при использовании вебхука нельзя одновременно использовать long polling.  Вместо этого необходимо настроить асинхронный веб‑сервер (например, `aiohttp`) и вызвать метод `setWebhook` для привязки URL【471498544294698†L576-L599】.  В нашем примере бот использует long polling для локального запуска, однако для продакшн‑окружения следует рассмотреть переход на вебхуки.
