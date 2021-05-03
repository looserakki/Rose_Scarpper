from Rsc import TOKEN, tbot
import Rsc.events

try:
    tbot.start(bot_token=TOKEN)
except Exception:
    print("Bot Token Invalid")
    exit(1)

tbot.run_until_disconnected()

