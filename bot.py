#-------------------------------------- https://github.com/m4mallu/PMChatbot ------------------------------------------#
import os
from Plugins import LOGS, BOT

from pyrogram import Client

if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config

# Logging 
basicConfig(
    format="> %(asctime)s | %(name)s [%(levelname)s] <> %(message)s",
    level=INFO,
    datefmt="%d/%m/%Y, %H:%M:%S",
    handlers=[FileHandler("PMBot.log"), StreamHandler()],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("pyrogram.dispatcher").setLevel(logging.INFO)
LOGS.info("Starting Deployment...")
LOGS.info("This Bot Is Powered By @TheeDeCode || @OfficialDeCode,For Any Query Contact Us")

BOT.start()
idle()

BOT.stop()
LOGS.info("Bot Stopped, Something Went Wrong..")
