"""
Telegram Price Tracker Bot
==========================

This script implements a simple Telegram bot that monitors the price of a single
product page and notifies a chat when the price drops.  It uses the aiogram
framework for Telegram and the aiohttp/BeautifulSoup stack for fetching and
parsing the page.  Configuration is done through environment variables;
see the accompanying README.md for details.

Note: For production deployments you should consider running the bot via a
webhook rather than long polling.  When using webhooks, the Telegram Bot API
delivers updates to your server; the aiogram documentation explains that you
cannot use long polling and webhooks at the same time and that you need an
async web framework to serve the webhook【471498544294698†L576-L599】.
"""

import asyncio
import logging
import os
from typing import Optional

import aiohttp
from aiogram import Bot, Dispatcher, types
from bs4 import BeautifulSoup

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Read configuration from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
PRODUCT_URL = os.getenv("PRODUCT_URL")
PRICE_SELECTOR = os.getenv("PRICE_SELECTOR", "span.price")
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", "3600"))  # seconds

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is not set")
if not CHAT_ID:
    raise RuntimeError("CHAT_ID environment variable is not set")
if not PRODUCT_URL:
    raise RuntimeError("PRODUCT_URL environment variable is not set")


async def fetch_price(session: aiohttp.ClientSession, url: str, selector: str) -> Optional[float]:
    """Fetch the product page and extract the numeric price.

    Args:
