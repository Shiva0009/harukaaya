import logging, os, sys, time
import telegram.ext as tg
from telethon.sessions import MemorySession
from telethon import TelegramClient


StartTime = time.time()


# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOGGER = logging.getLogger(__name__)


# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "You must have a python version of at least 3.6! Multiple features depend on this. Bot quitting."
    )
    quit(1)

ENV = bool(os.environ.get("ENV", False))

if ENV:
    TOKEN = os.environ.get("TOKEN", "5901539309:AAHi49v-3IEQRJ98-Obx58zuuXpD68GLUOQ")

    try:
        OWNER_ID = os.environ.get("OWNER_ID", "5620092357")
    except ValueError:
        raise Exception("Your OWNER_ID env variable is not a valid integer.")
    try:
        INSPECTOR = {int(x) for x in os.environ.get("INSPECTOR", "").split()}
        DEV_USERS = {int(x) for x in os.environ.get("DEV_USERS", "").split()}
    except ValueError:
        raise Exception("Your inspector(sudo) or dev users list does not contain valid integers.")

    try:
        REQUESTER = {int(x) for x in os.environ.get("REQUESTER", "").split()}
    except ValueError:
        raise Exception("Your requester list does not contain valid integers.")
    try:
        API_ID = int(os.environ.get("API_ID", "27926792"))
    except ValueError:
        raise Exception("Your API_ID env variable is not a valid integer.")

    try:
        API_HASH = os.environ.get("API_HASH", "71baac4bfd54337b396c525c9fb1c437")
    except ValueError:
        raise Exception("Please Add Hash Api key to start the bot")

    DB_URI = os.environ.get("postgres://qszfsijv:y6sYqkEb8Z9lFGBmriG7AYjbSbgAJBVk@peanut.db.elephantsql.com/qszfsijv")
    KORA_API_TOKEN = os.environ.get("KORA_API_TOKEN")
    PHOTO = os.environ.get("PHOTO")
    WORKERS = int(os.environ.get("WORKERS", 8))
    ALLOW_EXCL = os.environ.get('ALLOW_EXCL', False)
    ALLOW_CHATS = os.environ.get("ALLOW_CHATS", True)

    OWNER_USERNAME = os.environ.get("demure_shiv", None)
    SUPPORT_CHAT = os.environ.get("-1001883990501", None)
    EVENT_LOGS = os.environ.get("EVENT_LOGS", None)
    JOIN_LOGGER = os.environ.get("JOIN_LOGGER", None)

    WEBHOOK = bool(os.environ.get("WEBHOOK", False))
    CERT_PATH = os.environ.get("CERT_PATH")
    URL = os.environ.get("URL", "")  # Does not contain token
    PORT = int(os.environ.get("PORT", 5000))

    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "translation").split()

    DEL_CMDS = bool(os.environ.get("DEL_CMDS", True))
    INFOPIC = bool(os.environ.get("INFOPIC", False))




else:
    from Yone.config import Development as Config

    try:
        OWNER_ID = int(Config.OWNER_ID)
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")
# telegram bot requered things from telegram org 
    API_ID = Config.API_ID
    API_HASH = Config.API_HASH
    TOKEN = Config.TOKEN
    DB_URI = Config.SQLALCHEMY_DATABASE_URI

    SUPPORT_CHAT = Config.SUPPORT_CHAT

# WEBHOOK REQUERED THINGS
    WORKERS = Config.WORKERS
    ALLOW_EXCL = Config.ALLOW_EXCL
    WEBHOOK = Config.WEBHOOK
    CERT_PATH = Config.CERT_PATH
    PORT = Config.PORT
    URL = Config.URL


updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)
telethn = TelegramClient(MemorySession(), API_ID, API_HASH)
dispatcher = updater.dispatcher



