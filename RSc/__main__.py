from RSc import TOKEN, tbot
import RSc.events

try:
    tbot.start(bot_token=TOKEN)
except Exception:
    print("Bot Token Invalid")
    exit(1)

async def start_log():
    await tbot.send_message(-1001163286284, "**Scrapper Started!**")


tbot.loop.run_until_complete(start_log())

tbot.run_until_disconnected()

