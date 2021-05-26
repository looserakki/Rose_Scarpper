from RSc import ubot, OWNER_ID
from telethon import events
from functions.messages import ImportChatInviteRequest

@tbot.on(events.NewMessage(pattern="^/start$"))
async def event(event):
 await event.reply("RSc Scrapper is online With 1/15 Clients Active.")

@tbot.on(events.NewMessage(pattern="^/scrape ?(.*)"))
async def sc(event):
 if not event.sender_id == OWNER_ID:
    return
 if not event.pattern_match.group(1):
    return await event.reply("Please enter the chat username to start scrapping members.")
 chat_username = event.pattern_match.group(1)
 try:
   chat = await tbot.get_entity(chat_username)
   username = chat.username
 except:
   return await event.reply("❌Invalid chat provided.")
 await ubot(ImportChatInviteRequest(hash=username))
 
