from pyrogram import Client, idle, filters
import os
from new.mkn import MKN
from sample2.mkn2 import Sbot
from sample3.arjun import Arjun

Arjun.run()

Sbot.start()
MKN.start()

idle()
 
Sbot.stop()
MKN.stop()
