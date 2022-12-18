from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
STRING = getenv("STRING_SESSION", "BQBD1fTjePi95vr0b0UhM2LYVlhOmFLETWqX3k9IKNKyewE12ptohui2NZxTozHHAVowsfBnzkW_p7NP67lYhG3ujyyLjchiyfEj5c4dKURctQkJThgibR_Lrc52CX5cIpK-sLDdsnwtO0Ppb8GpIoaMLEvf1kbuEBxqAFochWbcD3uR6UlPvp8DQgHSQ9W_Z_8_6nGwxGkNUv-7faKj0VrnVFRYA8sNnGGOJZPyIzx13_JqQvUb1lWn67PvT7HTteqAMqXuLgBSAewCJLuKF2crYqeCojJLv0JBU2n3MJCoRd6KWjp8mwboCqt0IG2H3fjNXZuNlvfx-OANszqOWEohAAAAAU0hUXYA")
BOT_TOKEN = getenv("BOT_TOKEN" ,"5947463448:AAGoOQ8GRiSH_NHDgrAcs4L-fvMcd0A-aVk")
API_ID = int(getenv("API_ID", "14739013"))
API_HASH = getenv("API_HASH","0d4ffaf95ba8e5dac2c6df849d86213d")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "999999"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://logesh:logesh@cluster0.z75dh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1955509952").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "1955509952").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001759657140"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME","Logi")
if str(getenv("SUPPORT_CHANNEL")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))
