import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**bgm Bot**, \n",
                    buttons=(
                      [Button.url('Owner BGM', 'https://t.me/aliyefhsos'),
                      [Button.url('Instagram', 'https://t.me/aliyefh_sos'),
                      [Button.url('WhatsApp', 'https://t.me/@aliyefh_sos')]
                    ),
                    link_preview=False
                   )
print("BOT ONLINE")
client.run_until_disconnected()
