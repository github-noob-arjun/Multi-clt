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

my_apps.items.start()

Client.idle()

my_apps.items.stop()
