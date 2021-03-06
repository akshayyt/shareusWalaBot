# (c) @RoyalKrrishna

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.

π€ My Name: <a href='https://t.me/SuperfastSearchbot'> Super fast Search bot</a>

π Language : <a href='https://www.python.org'> Python V3</a>

π Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

π‘ Server: <a href='https://heroku.com'>Heroku</a>

π¨βπ» Created By: <a href='https://t.me/Akshay_Chand'>Akshay Chand</a></b>
"""

    ABOUT_HELP_TEXT = """<b>π¨βπ» Developer : <a href='https://t.me/Akshay_Chand'>Akshay Chand</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hey! {}π,

Super fast Search bot Here.π€</a>

I Can Search π What You Wantβ

<a>Made With β€ By @Akshay_Chand</a></b>
"""


    START_MSG = """
<b>Hey! {}π,

Super fast Search bot.π€</a>

I Can Search π What You Wantβ

<a>Made With β€ By @Akshay_Chand</a></b>
"""


