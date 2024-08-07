import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 29350132
API_HASH = "e854995be05edb5bf21f5b84bdc0212f"
BOT_TOKEN = "7324085779:AAE_b-iI2nnpAmSFTBq2JHERBlQOMWlOAKU"
MONGO_DB_URI = "mongodb+srv://devilkingp0404:devilkingp0404@cluster0.iw04afs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 16000))
LOG_GROUP_ID = -1002222142844
OWNER_ID = 7245959664

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/timepassmarkus04/Marwin2002",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/MNS_botss")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/MNS_botss")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQG_2PQAStIETpzT9i1ELcS8hFwMXd99-qtMxgdeNafIh82fMT_MMMoaLGKvaI7vPn4NVaEX8CVUl1a3LhatZ7-EMNEFAVPHP7Rk-wVwZ2rd0wnyc39Eq0ufUf4Bew3Cl7KprUcsBePYwZGAbldfnVq_puWkyI8Pga37I1vK8I46ZgENwlFxvu9IXnsdOBQC3TI33Mw1U00BDZe04WDrRVZjhctUBocqbOEbWQj5ZsLUSQEL8EuY2-_nJQC6BL-136B4XiLE1BVKRZfAJfOQJnSJzFRNKOOySDjptAjr2zPwckqjP1pROUDyGtJaVXQiC7zJQTHJcsQXounNO4zDpAdWVflVEgAAAAG85SnWAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/b5c5289821a2445fb5042.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/b5c5289821a2445fb5042.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org//file/3dfcffd0c218ead96b102.png"
STATS_IMG_URL = "https://graph.org//file/99a8a9c13bb01f9ac7d98.png"
TELEGRAM_AUDIO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
TELEGRAM_VIDEO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
