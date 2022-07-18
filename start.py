from pyrogram import Client, idle, filters
import os
from new.mkn import MKN
from sample2.mkn2 import Sbot
from sample3.arjun import Arjun



my_apps = [
    Client("Sbot"),
    Client("MKN"),
    Client("Arjun"),
    # and so on
]

for app in my_apps:

my_apps.run()
   app.start()

Client.idle()
 
for app in my_apps:
    app.stop()
