import discord
import os
from dotenv import load_dotenv
from pathlib import Path
from moderation_functions import kick, ban, mute, unmute

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        msg_from_server_owner = message.author.name == "jothinkumar"
        if msg_from_server_owner:
            match message.content.lower().split()[0]:
                case "kick":
                    await kick(message)
                case "ban":
                    await ban(message)
                case "mute":
                    await mute(message)
                case "unmute":
                    await unmute(message)
    
    async def on_member_join(self, member):
        channel = self.get_channel(1196700464549462088)
        await channel.send(f"Welcome to the server, {member.mention}")


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = MyClient(intents=intents)
client.run(os.getenv("DISCORD_TOKEN"), reconnect=True)
