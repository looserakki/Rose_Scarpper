from RSc import tbot, ubot, vbot, wbot, xbot, ybot, OWNER_ID, xbot
import random, asyncio
from telethon.tl.functions.channels import InviteToChannelRequest as invite
from telethon.errors import UserKickedError, UserBannedInChannelError, UserBlockedError, ChatWriteForbiddenError, ChatAdminRequiredError, UserNotMutualContactError, FloodError, UserPrivacyRestrictedError, FloodWaitError, PeerFloodError
from telethon import events, Button

clients = [ubot, vbot, wbot, xbot, ybot]

@tbot.on(events.NewMessage(pattern="^[.?!/]add ?(.*)"))
async def add(event):
 if not event.sender_id == 1763477650:
    return
 from RSc.modules.Scrape import members
 if event.pattern_match.group(1):
   limit = event.pattern_match.group(1)
 else:
   limit = 50
 if len(members) == 0 or len(members) < int(limit):
   return await event.reply("Not enough members in scrapped list.")
 final = 0
 for user in members:
   if final >= int(limit):
     break
   try:
     x = random.choice(clients)
     await x(invite(event.chat_id, [user]))
     final += 1
     members.remove(user)
     await asyncio.sleep(2)
   except UserPrivacyRestrictedError:
     members.remove(user)
     pass
   except UserNotMutualContactError:
     members.remove(user)
     pass
   except UserKickedError:
     members.remove(user)
     pass
   except UserBannedInChannelError:
     members.remove(user)
     pass
   except UserBlockedError:
     members.remove(user)
     pass
   except ChatWriteForbiddenError:
     return await event.reply("One of the clients is muted unmute them and restart proceedure.")
   except ChatAdminRequiredError:
     return await event.reply("Enable add members permission.")
   except FloodError as e:
    try:
     x = random.choice(clients)
     await x(invite(event.chat_id, [user]))
     final += 1
     members.remove(user)
     await asyncio.sleep(2)
    except:
      pass
   except PeerFloodError:
    try:
     x = random.choice(clients)
     await x(invite(event.chat_id, [user]))
     final += 1
     members.remove(user)
     await asyncio.sleep(2)
    except:
      pass
   except FloodWaitError:
     x = random.choice(clients)
     await x(invite(event.chat_id, [user]))
     final += 1
     members.remove(user)
     await asyncio.sleep(2)
   except:
     try:
       x = random.choice(clients)
       await x(invite(event.chat_id, [user]))
       final += 1
       members.remove(user)
       await asyncio.sleep(2)
     except:
      pass
 await event.respond(f"Added {final} Members.")
   
@tbot.on(events.NewMessage(pattern="^/tadd ?(.*)"))
async def adder(event):
 if not event.sender_id == 1763477650:
    return
 from RSc.modules.Scrape import members
 if event.pattern_match.group(1):
   limit = int(event.pattern_match.group(1))
 else:
   limit = 69
 final = 0
 for user in members:
   if final == limit:
     break
   client = random.choice(clients)
   try:
     await client(invite("eviesupport", [user]))
     members.remove(user)
     final += 1
   except:
     pass
