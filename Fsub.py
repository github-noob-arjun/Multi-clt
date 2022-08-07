from pyrogram.errors import UserNotParticipant
from pyrogram import enums

async def not_subscribed(_, client, message):
   if not client.force_channel:
      return False
   try:             
      user = await client.get_chat_member(client.force_channel, message.from_user.id)
   except UserNotParticipant:
      pass
   else:
      if user.status != enums.ChatMemberStatus.RESTRICTED:         
         return False 
   return True
