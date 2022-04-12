from logging import getLogger
from sample_config import Config
from pyrogram import Client

LOGS = getLogger("PMBot")
BOT = Client("pmbot", api_id=Config.APP_ID, api_hash=Config.API_HASH, bot_token=Config.TG_BOT_TOKEN, plugins=dict(root="Plugins"))
