from RSc import tbot, ubot, vbot, wbot, xbot, ybot, OWNER_ID
import random, asyncio
from telethon.tl.functions.channels import InviteToChannelRequest as invite
from telethon.errors import UserKickedError, UserBannedInChannelError, UserBlockedError, ChatWriteForbiddenError, ChatAdminRequiredError, UserNotMutualContactError, UserPrivacyRestrictedError
from telethon import events, Button

@tbot.on(events.NewMessage(pattern="^[.?!/]add ?(.*)"))
async def add(event):
 if not event.sender_id == 1763477650:
    return
 from RSc.modules.Scraper import members
 if event.pattern_match.group(1):
   limit = event.pattern_match.group(1)
 else:
   limit = 50
 if len(members) == 0 or len(members) < limit:
   return await event.reply("Not enough members in scrapped list.")
 clients = [ubot, vbot, wbot, xbot, ybot]
 final_no
 for user in members:
   if final >= limit:
      break
   client = random.choice(clients)
   try:
     client(invite(event.chat_id, user))
     final += 1
     await asyncio.sleep(1)
     members.remove(user)
   except UserPrivacyRestrictedError:
     pass
   except UserNotMutualContactError:
     pass
   except UserKickedError:
     pass
   except UserBannedInChannelError:
     pass
   except UserBlockedError:
     pass
   except ChatWriteForbiddenError:
     return await event.reply("One of the clients is mutes unmute them and restart proceedure.")
   except ChatAdminRequiredError:
     return await event.reply("Enable add members permission.")
   except FloodError as e:
     await asyncio.sleep(e.seconds)
 await event.respond(f"Added {final} Members.")
   
