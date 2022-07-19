from pyrogram import Client, idle, filters
import os
import asyncio
from DCBot.Main import DCBot as App1
from new2.sample2 import App2
from new3.sample3 import App3

App1.start()
App2.start()
App3.start()

idle()

App1.stop()
App2.stop()
App3.stop()
