from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from start import App2 as Clt1

@Clt1.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Success Message 💥 2")
