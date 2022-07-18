from pyrogram import Client, idle, filters 
import os
from new.mkn import MKN
from sample2.mkn2 import Sbot

Sbot.start()
MKN.start()

idle()

Sbot.stop()
MKN.stop()
