import discord
import os
from dotenv import load_dotenv
from pathlib import Path
from json import load
from random import randint

from moderation_functions import kick, ban, mute, unmute
from chatbot import get_response

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)
with open("config.json", "r") as f:
    config = load(f)


class MyClient(discord.Client):
    async def on_ready(self):
        self.bot_log_channel = self.get_channel(config["bot-log-channel-id"])
        self.owner = await self.fetch_user(config["owner-id"])
        await self.bot_log_channel.send(f"Hi {self.owner.mention}, I'm online!")

    async def on_message(self, message):
        if message.author == self.user:
            return

        msg_from_server_owner = message.author.id == self.owner.id
        if msg_from_server_owner:
            if "shutdown" in message.content.lower() and self.user.mention in message.content:
                self.shutdown_code = randint(1000, 9999)
                await message.channel.send(f"Are you sure you want to shut me down? type {self.shutdown_code} and ping me to confirm.")
                return
            if hasattr(self, 'shutdown_code') and str(self.shutdown_code) in message.content and self.user.mention in message.content:
                await message.channel.send("Shutting down...")
                await self.close()
                return
            match message.content.lower().split()[0]:
                case "kick":
                    await kick(message)
                    return
                case "ban":
                    await ban(message)
                    return
                case "mute":
                    await mute(message)
                    return
                case "unmute":
                    await unmute(message)
                    return
        
        if self.user.mention in message.content or message.reference is not None and message.reference.resolved.author == self.user:
            prev_msg_ref = message.reference
            async with message.channel.typing():
                await message.reply(get_response(
                    "" if prev_msg_ref is None else
                    f"Previous message by {prev_msg_ref.resolved.author.name.replace(self.user.name, 'you')}: {prev_msg_ref.resolved.content}",
                    message.clean_content   .replace(self.user.mention, "Server Bot")
                ))
    
    async def on_member_join(self, member):
        channel = self.get_channel(config["welcome-channel-id"])
        await channel.send(f"Welcome to the server, {member.mention}")


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = MyClient(intents=intents)
client.run(os.getenv("DISCORD_TOKEN"), reconnect=True)
