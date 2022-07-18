from pyrogram import Client, idle, filters 
import os
from new.mkn import MKN
from sample2.mkn2 import Sbot
from sample3.arjun import Arjun

Sbot.start()
MKN.start()
Arjun.start()

idle()

MKN.stop()
Sbot.stop()
Arjun.stop()
