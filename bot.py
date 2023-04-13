from pyrogram import Client
from config import *
from route import web_server
from aiohttp import web
bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=100,
    plugins={"root": "main"},
    sleep_threshold=10,
  )
bot.start()
       
