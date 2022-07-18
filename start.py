from pyrogram import Client, idle, filters, MessageHandler
import os
from new.mkn import MKN
from sample2.mkn2 import Sbot
from sample3.arjun import Arjun



my_apps = {
    "Sbot": Client("Sbot"),
    "MKN": Client("MKN"),
    "Arjun": Client("Arjun"),
    # and so on
}

def test(a, m):
    m.reply("Response")

for _, app in my_apps.items():
    # Add a MessageHandler to each Client and start it
    app.add_handler(MessageHandler(test, Filters.command("test")))
    app.start()

Client.idle()


for _, app in my_apps.items():
    app.stop()
