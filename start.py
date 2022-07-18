from pyrogram import Client, idle, filters 
import os

BOT_TOKEN = "5465507667:AAFggC4o13JV-J-zC8yuZf3sUZa-1y5AJgk"
API_ID = 4738674
API_HASH = "f2be74eaa9b1cb32498f45d04e4dbb54"

bot = Client("Sbot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

@bot.on_message(filters.text)
async def start(client, message):
    await message.reply_text("Success Message 💥")
