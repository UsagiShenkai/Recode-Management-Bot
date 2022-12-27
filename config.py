import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID", "9735747")
    API_HASH = getenv("API_HASH", "391c71286a84db5065e2d218d9cdfd38")
    TOKEN = getenv("TOKEN", "5888843904:AAEYxHtQNjCx8x-nglIorkueYaG-_DNOKe0")
    OWNER_ID = getenv("OWNER_ID", "5489233583")
    ASSISTANT_ID = getenv("ASSISTANT_ID", "5951656665")
    STRING_SESSION = getenv("STRING_SESSION", "1BVtsOIYBu7JcP8VDGIl-F8ShIEUCaqtbl1k8Qb-doEl3r5sjbk3BiIt4ZJq1EFGCZVA28p6Z4r1WmeIxLdl50Dl5_3DabXTH3RJGwBpvo7n1Z0337UeXFUJss_GGfphZdgbr37GZSXkNwpB_U6IeNFOFAxekUDYubNiUFuhgmkdXgSNAh_cbhIi2nVeL2RNXfd1VBBmJmhbJEj2Rcyf6Tf4UtdiyLjr4xKJOKhKyc5GV7XonHTIvkd9I00_olvbcdm7uS53FnuqlZQzojoRdyEQqz6GiDQG0FvTtnPDBklWedhH7R4qZnJoopUbRwEvCJcnIikvFARcDCMBTW-CogDkPYio0CIg=") #telethon
    OWNER_USERNAME = getenv("OWNER_USERNAME", "Hirakox")
    DB_URI = getenv("DATABASE_URL", "postgres://qcocgtqm:xwAT1Iw4TmGsJMwSOJIgv7klpF11qVNH@mahmud.db.elephantsql.com/qcocgtqm")
    DB_URI = DB_URI.replace("postgres", "postgresql")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "-1001742432410")
    GBAN_LOGS = getenv("GBAN_LOGS", "-1001742432410")
    SYS_ADMIN = getenv("SYS_ADMIN", "5951656665")
    DEV_USERS = getenv("DEV_USERS", "5951656665")
    LOAD = getenv("LOAD")
    WEBHOOK = False
    SPB_MODE = True
    DROP_UPDATES = False
    DEBUG = False
    URL = None
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    BAN_STICKER = getenv("BAN_STICKER", "")
    ALLOW_EXCL = True
    CUSTOM_CMD = False
    CHANNEL = getenv("CHANNEL", "TheUpdatesChannel")
    SUPPORT = getenv("SUPPORT", "TheSupportChat")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    CASH_API_KEY = getenv("CASH_API_KEY", "https://www.alphavantage.co/support/#api-key")
    TIME_API_KEY = getenv("TIME_API_KEY", "https://timezonedb.com/api")
    WALL_API = getenv("WALL_API", "https://wall.alphacoders.com/api.php")
    spamwatch_api = getenv("spamwatch_api", "https://t.me/SpamWatchBot")
    SPAMMERS = getenv("SPAMMERS", "")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "https://www.last.fm/api/account/create")
    CF_API_KEY = getenv("CF_API_KEY", "coffehouse.intellivoid.net")
    BOT_API_URL = getenv("BOT_API_URL", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("BOT_API_FILE_URL", "https://api.telegram.org/file/bot")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5951656665").split()))
    ZAID_USER = list(map(int, getenv("DEV_USERS", "5951656665").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))
