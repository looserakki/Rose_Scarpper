from telethon import TelegramClient
import os, logging, sys, io
from logging import basicConfig, INFO, getLogger
from telethon.sessions import StringSession

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
LOGGER = logging.getLogger(__name__)

STRING_1 = os.environ.get("SS_1", None)
STRING_2 = os.environ.get("SS_2", None)
STRING_3 = os.environ.get("SS_3", None)
STRING_4 = os.environ.get("SS_4", None)
STRING_5 = os.environ.get("SS_5", None)
STRING_6 = os.environ.get("SS_6", None)
STRING_7 = os.environ.get("SS_7", None)
STRING_8 = os.environ.get("SS_8", None)
STRING_9 = os.environ.get("SS_9", None)
STRING_10 = os.environ.get("SS_10", None)

TOKEN = os.environ.get("TOKEN", None)

KEY_1 = os.environ.get("KEY_1", None)
KEY_2 = os.environ.get("KEY_2", None)
KEY_3 = os.environ.get("KEY_3", None)
KEY_4 = os.environ.get("KEY_4", None)
KEY_5 = os.environ.get("KEY_5", None)
KEY_6 = os.environ.get("KEY_6", None)
KEY_7 = os.environ.get("KEY_7", None)
KEY_8 = os.environ.get("KEY_8", None)
KEY_9 = os.environ.get("KEY_9", None)
KEY_10 = os.environ.get("KEY_10", None)

HASH_1 = os.environ.get("HASH_1", None)
HASH_2 = os.environ.get("HASH_2", None)
HASH_3 = os.environ.get("HASH_3", None)
HASH_4 = os.environ.get("HASH_4", None)
HASH_5 = os.environ.get("HASH_5", None)
HASH_6 = os.environ.get("HASH_6", None)
HASH_7 = os.environ.get("HASH_7", None)
HASH_8 = os.environ.get("HASH_8", None)
HASH_9 = os.environ.get("HASH_9", None)
HASH_10 = os.environ.get("HASH_10", None)

DB_URI = os.environ.get("DATABASE_URL", None)
DIR = "./"

if STRING_1:
 abot = TelegramClient(StringSession(STRING_1), KEY_1, HASH_1)
if STRING_2:
 bbot = TelegramClient(StringSession(STRING_2), KEY_2, HASH_2)
if STRING_3:
 cbot = TelegramClient(StringSession(STRING_1), KEY_1, HASH_2)
if STRING_4:
 dbot = TelegramClient(StringSession(STRING_1), KEY_1, HASH_2)
if STRING_4:
 ebot = TelegramClient(StringSession(STRING_1), KEY_1, HASH_2)
if STRING_5:
 fbot = TelegramClient(StringSession(STRING_1), KEY_1, HASH_2)
if STRING_6:
 gbot = TelegramClient(StringSession(STRING_1), KEY_1, HASH_2)
if STRING_7:
 hbot = TelegramClient(StringSession(STRING_1), KEY_1, HASH_2)
if STRING_8:
 ibot = TelegramClient(StringSession(STRING_1), KEY_1, HASH_2)
if STRING_9:
 jbot = TelegramClient(StringSession(STRING_1), KEY_1, HASH_2)
if STRING_10:
 kbot = TelegramClient(StringSession(STRING_1), KEY_1, HASH_2)

try:
        abot.start()
except:
        print("Invalid STRING SESSION 1!")
try:
        bbot.start()
except:
        print("Invalid STRING SESSION 2!")
try:
        cbot.start()
except:
        print("Invalid STRING SESSION!3")
try:
        dbot.start()
except:
        print("Invalid STRING SESSION 4!")
try:
        ebot.start()
except:
        print("Invalid STRING SESSION 5!")
try:
        fbot.start()
except:
        print("Invalid STRING SESSION 6!")
try:
        gbot.start()
except:
        print("Invalid STRING SESSION 7!")
try:
        hbot.start()
except:
        print("Invalid STRING SESSION 8!")
try:
        ibot.start()
except:
        print("Invalid STRING SESSION 9!")
try:
        jbot.start()
except:
        print("Invalid STRING SESSION 10!")

