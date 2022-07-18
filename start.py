from pyrogram import Client, idle, filters 
import os
from new.mkn import MKN
from sample2.mkn2 import Sbot

BOT_TOKEN = "5501750004:AAGXvnWJWR5SRAm5geuv1qikpUVsI2oPK4o"
API_ID = 4738674
API_HASH = "f2be74eaa9b1cb32498f45d04e4dbb54"

bot = Client("bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

@Sbot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Success Message 💥 3")


Sbot.run()

idle()

MKN.run()
bot.run()


#Sbot.stop()
#MKN.stop()
