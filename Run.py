from pyrogram import Client, idle, filters
import os
import asyncio
from start import App1, App2, App3

#my_apps = {
#    "App1": Client("App1"),
 #   "App2": Client("App2"),
#    "App3": Client("App3"),
#    # and so on
#}


#for _, app in my_apps.items():
#    # Add a MessageHandler to each Client and start it
    # app.add_handler(MessageHandler(test, Filters.command("test")))
#    app.start()


#Client.idle()

#for _, app in my_apps.items():
#    app.stop()

App1.start()
App2.start()
App3.start()

idle()

App1.stop()
App2.stop()
App3.stop()
