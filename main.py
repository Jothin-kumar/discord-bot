import discord
import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import timedelta

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        msg = message.content
        msg_from_server_owner = message.author.name == "jothinkumar"
        mentions = message.mentions
        if self.user in mentions:
            await message.reply(f"Hello {message.author.mention}, I'm live.")
        if msg_from_server_owner:
            if msg.startswith("kick"):
                for user in mentions:
                    await user.kick(reason=message.content)
                    await message.reply(f"Kicked {user.mention}")
            elif msg.startswith("ban"):
                for user in mentions:
                    await user.ban(reason=message.content)
                    await message.reply(f"Banned {user.mention}")
            elif msg.startswith("mute"):
                secs = 60
                for word in msg.split()[::-1]:
                    if word.endswith("s"):
                        try:
                            secs = int(word[:-1])
                        except ValueError:
                            pass
                for user in mentions:
                    await user.timeout(timedelta(seconds=secs), reason=message.content)
                    await message.reply(f"Muted {user.mention} for {secs} seconds")
    
    async def on_member_join(self, member):
        channel = self.get_channel(1196700464549462088)
        await channel.send(f"Welcome to the server, {member.mention}")


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = MyClient(intents=intents)
client.run(os.getenv("DISCORD_TOKEN"), reconnect=True)
