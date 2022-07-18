from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from start import App3 as Clt3

@Clt3.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Success Message 💥 3")
