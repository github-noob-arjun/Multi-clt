from pyrogram import Client, idle, filters 
import os

BOT_TOKEN = ""
API_ID =
API_HASH = ""

Sbot = Client("Sbot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

@Sbot.on_message(filters.text)
async def start(client, message):
    await message.reply_text("Success Message 💥")
