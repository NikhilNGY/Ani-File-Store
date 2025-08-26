# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import re
import os
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default=False):
    if value is None:
        return default
    v = str(value).strip().lower()
    if v in ("true", "yes", "1", "enable", "enabled", "y", "on"):
        return True
    if v in ("false", "no", "0", "disable", "disabled", "n", "off"):
        return False
    return default

# ---------- Bot Information ----------
API_ID = int(environ.get("API_ID", "2468192"))
API_HASH = environ.get("API_HASH", "4906b3f8f198ec0e24edb2c197677678")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Pictures for /start (space-separated list). Safe if empty.
_default_pics = (
    "https://telegra.ph/file/84e99f37a84ea85be1bd5.jpg "
    "https://telegra.ph/file/ea10bde858558928aea10.jpg "
    "https://telegra.ph/file/13cc320175d6fc4ccbace.jpg "
    "https://telegra.ph/file/9107275ff1d9b71db6bec.jpg "
    "https://telegra.ph/file/4466d37d43f5703516f74.jpg"
)
PICS = [p for p in environ.get("PICS", _default_pics).split() if p] or _default_pics.split()

ADMINS = [
    int(a) if id_pattern.search(a) else a
    for a in environ.get("ADMINS", "2068233407").split()
]

BOT_USERNAME = environ.get("BOT_USERNAME", "File_StoreRobot")  # without @
PORT = int(environ.get("PORT", "8080"))

# ---------- Clone Info ----------
CLONE_MODE = is_enabled(environ.get("CLONE_MODE"), False)

# If Clone Mode is True, fill these:
CLONE_DB_URI = environ.get(
    "CLONE_DB_URI",
    "",
)
CDB_NAME = environ.get("CDB_NAME", "Filter1")

# ---------- Database Information ----------
DB_URI = environ.get(
    "DB_URI",
    "",
)
DB_NAME = environ.get("DB_NAME", "Filter1")

# ---------- Auto Delete ----------
AUTO_DELETE_MODE = is_enabled(environ.get("AUTO_DELETE_MODE"), True)
AUTO_DELETE = int(environ.get("AUTO_DELETE", "30"))          # minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "1800"))  # seconds

# ---------- Channel / Logs ----------
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1001693006436"))

# ---------- File Caption ----------
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# ---------- Public File Store ----------
PUBLIC_FILE_STORE = is_enabled(environ.get("PUBLIC_FILE_STORE", "True"), True)

# ---------- Verification ----------
VERIFY_MODE = is_enabled(environ.get("VERIFY_MODE", "False"), False)
SHORTLINK_URL = environ.get("SHORTLINK_URL", "")  # without https://
SHORTLINK_API = environ.get("SHORTLINK_API", "")
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "")

# ---------- Website Mode (for genlink.py) ----------
WEBSITE_URL_MODE = is_enabled(environ.get("WEBSITE_URL_MODE"), True)
WEBSITE_URL = environ.get("WEBSITE_URL", "")  # If enabled, set full base URL

# ---------- File Stream Config ----------
STREAM_MODE = is_enabled(environ.get("STREAM_MODE"), False)
MULTI_CLIENT = is_enabled(environ.get("MULTI_CLIENT"), False)

SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes

ON_HEROKU = "DYNO" in environ
URL = environ.get("URL", "")-------------------------------------------------------------
