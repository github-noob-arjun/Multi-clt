from pyrogram import Client, idle, filters
import os
from new.mkn import MKN
from sample2.mkn2 import Sbot
from sample3.arjun import Arjun


a = Client("Sbot"),
b = Client("MKN"),
c = Client("Arjun"),

a.start()
b.start()
c.start()

idle()
 
a.stop()
b.stop()
c.stop()
