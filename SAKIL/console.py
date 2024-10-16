import os
import time
import logging

from os import getenv
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler


logging.basicConfig(
    format="[%(asctime)s]:[%(levelname)s]:[%(name)s]:: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "logs.txt", maxBytes=(1024 * 1024 * 5), backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)


if os.path.exists("Internal"):
   load_dotenv("Internal")


API_ID = int(getenv("API_ID", "22617523"))
API_HASH = getenv("API_HASH", "30e617ac3ad93cf39b49f4a9172c00aa")
BOT_TOKEN = getenv("BOT_TOKEN", "7916642904:AAHtvJzGVzgTcJ_9Ks4LQ5C4f_2XMA70ILQ")
STRING_SESSION = getenv("STRING_SESSION", "BQHHpwsAkYECKGCUqK4pVTOBxaKueTShS9MIxtLes1LFxOlSE8RX2SX9D69VzoAj-QiZRurn1NvSblRCE5NCEb-a6AFnRBvoPfOo8uNeQ6DCXqKE-uJgNQb_yopXXw2dLQ8JLxHaTGKyDHnXyXAIh-uoyANPMNkRnfFh-Rw1wrXsjVfiK-9qa8u9UqmHXBpEi3esHOXkwzjHZJqHfx24Z_gZaqLQaTnD77zX0giIyS6rEJy7QI4Kd5wv1-lw43Ic7tP8D74PU0DtaxtWyGXdCfdqyehrvl52ZCclsm2DXv_UlxTsySrzusJtFSz4VtBJgmK-7INg6EBgKDkz8lvGFRqJBvNuQgAAAAFnEjCPAA")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://mr:mrs@sakil.fhmjb.mongodb.net/?retryWrites=true&w=majority&appName=sakil")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002429373405"))
OWNER_ID = int(getenv("OWNER_ID", "6024212623"))
OWNER_USERNAME = getenv("OWNER_USERNAME", "@YO_UR_OFFICIAL_CRUSH")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6024212623").split()))
ALIVE_PIC = getenv("ALIVE_PIC", "https://envs.sh/TLU.jpg")


# OPTIONAL VARIABLES
SESSION_STRING = getenv("SESSION_STRING", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". !").split())



# OTHERS VARIABLES

# PM GUARD VARS
PM_GUARD = bool(getenv("PM_GUARD", True))
PM_GUARD_TEXT = getenv("PM_GUARD_TEXT", "**🥀 ʜᴇʏ, ɪ ᴀᴍ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ & ꜱᴜᴘᴇʀꜰᴀꜱᴛ ʜɪɢʜ Qᴜᴀʟɪᴛʏ ᴜꜱᴇʀʙᴏᴛ ᴀꜱꜱɪꜱᴛᴀɴᴛ ᴡɪᴛʜ ᴀɴ ᴜᴘɢʀᴀᴅᴇᴅ ᴠᴇʀꜱɪᴏɴ ꜱᴇᴄᴜʀɪᴛʏ ꜱʏꜱᴛᴇᴍ.\n\n🌿 ɪ ᴄᴀɴ'ᴛ ʟᴇᴛ ʏᴏᴜ ᴍᴇꜱꜱᴀɢᴇ ᴍʏ ᴏᴡɴᴇʀ'ꜱ ᴅᴍ ᴡɪᴛʜᴏᴜᴛ ᴍʏ ᴏᴡɴᴇʀ'ꜱ ᴘᴇʀᴍɪꜱꜱɪᴏɴ.\n\n❤️ ᴍʏ ᴏᴡɴᴇʀ ɪꜱ ᴏꜰꜰʟɪɴᴇ ɴᴏᴡ, ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ ᴜɴᴛɪʟ ᴍʏ ᴏᴡɴᴇʀ ᴀʟʟᴏᴡꜱ ʏᴏᴜ.\n\n🍂 ᴘʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ꜱᴘᴀᴍ ʜᴇʀᴇ, ʙᴇᴄᴀᴜꜱᴇ ꜱᴘᴀᴍᴍɪɴɢ ᴡɪʟʟ ꜰᴏʀᴄᴇ ᴍᴇ ᴛᴏ ʙʟᴏᴄᴋ ʏᴏᴜ ꜰʀᴏᴍ ᴍʏ ᴏᴡɴᴇʀ ɪᴅ 👍🏻**")
PM_GUARD_LIMIT = int(getenv("PM_GUARD_LIMIT", 5))


# USERBOT DEFAULT IMAGE
USERBOT_PICTURE = getenv("USERBOT_PICTURE", "https://envs.sh/TLU.jpg")



# Don't Edit This Codes From This Line

LOGGER = logging.getLogger("main")
runtime = time.time()

FLOODXD = {}
OLD_MSG = {}
PM_LIMIT = {}
PLUGINS = {}
SUDOERS = []


COMMAND_HANDLERS = []
for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)
COMMAND_HANDLERS.append('')

