from telethon import TelegramClient
from telethon.sessions import StringSession
import os, sys

S_1 = os.environ.get("STRING_1")
S_2 = os.environ.get("STRING_2")
S_3 = os.environ.get("STRING_3")
S_4 = os.environ.get("STRING_4")
S_5 = os.environ.get("STRING_5")

K_1 = os.environ.get("KEY_1")
K_2 = os.environ.get("KEY_2")
K_3 = os.environ.get("KEY_3")
K_4 = os.environ.get("KEY_4")
K_5 = os.environ.get("KEY_5")

H_1 = os.environ.get("HASH_1")
H_2 = os.environ.get("HASH_2")
H_3 = os.environ.get("HASH_3")
H_4 = os.environ.get("HASH_4")
H_5 = os.environ.get("HASH_5")
OWNER_ID = os.environ.get("OWNER_ID")

TOKEN = os.environ.get("TOKEN")
tbot = TelegramClient(None, K_1, H_1)

ubot = TelegramClient(StringSession(S_1), K_1, H_1)

try:
  ubot.start()
except Exception as e:
  print(e)
  sys.exit()

