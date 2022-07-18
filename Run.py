from pyrogram import Client, idle, filters
import os
import asyncio
from Bot.App1 import App1
from Bot.App2 import App2
from Bot.App3 import App3

my_apps = [
    Client("App1"),
    Client("App2"),
    Client("App3"),
    # and so on
]


for app in my_apps:
    # Add a MessageHandler to each Client and start it
    # app.add_handler(MessageHandler(test, Filters.command("test")))
    app.start()


Client.idle()

for app in my_apps:
    app.stop()

