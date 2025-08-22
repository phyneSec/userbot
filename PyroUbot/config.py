import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "8111609385").split()))

API_ID = int(os.getenv("API_ID", "25854684"))

API_HASH = os.getenv("API_HASH", "7774a01f20d4edc63c90b19e1967cc79")

BOT_TOKEN = os.getenv("BOT_TOKEN", "ISI_BOT_TOKEN_TELE_MU_DISINI")

OWNER_ID = int(os.getenv("OWNER_ID", "ISI_ID_MU_DISINI"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-4767188817").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "Monggodb kamu")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", " -4767188817"))
