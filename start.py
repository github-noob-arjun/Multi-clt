from pyrogram import Client, idle, filters, compose
import os
from new.mkn import MKN
from sample2.mkn2 import Sbot
from sample3.arjun import Arjun


async def main():
    apps = [
        Client("Arjun"),
        Client("Sbot"),
        Client("MKN")
    ]

    ...

    await compose(apps)


asyncio.run(main())



