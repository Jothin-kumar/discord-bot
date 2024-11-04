from datetime import timedelta
from discord import errors


async def kick(msg):
    for user in msg.mentions:
        try:
            await user.kick(reason=msg.content)
            await msg.reply(f"Kicked {user.mention}")
        except errors.Forbidden:
            await msg.reply(f"**I can't kick {user.mention}**\n\nKindly make sure that I have the necessary permissions and that the user isn't superior to me")

async def ban(msg):
    for user in msg.mentions:
        try:
            await user.ban(reason=msg.content)
            await msg.reply(f"Banned {user.mention}")
        except errors.Forbidden:
            await msg.reply(f"**I can't ban {user.mention}**\n\nKindly make sure that I have the necessary permissions and that the user isn't superior to me")

async def mute(msg):
    weeks = 0
    days = 0
    hrs = 0
    mins = 0
    secs = 0
    for word in "".join([l for l in msg.content if l.isalnum() or l == " "]).split()[::-1]:
        try:
            match word[-1]:
                case "w":
                    weeks = int(word[:-1])
                case "d":
                    days = int(word[:-1])
                case "h":
                    hrs = int(word[:-1])
                case "m":
                    mins = int(word[:-1])
                case "s":
                    secs = int(word[:-1])
        except ValueError:
            pass
    if not any([weeks, days, hrs, mins, secs]):
        mins = 1
    td = timedelta(weeks=weeks, days=days, hours=hrs, minutes=mins, seconds=secs)
    if td.total_seconds() > 60*60*24*7*4:
        await msg.reply("I can't mute an user for more than 4 weeks")
        return
    for user in msg.mentions:
        try:
            await user.timeout(td, reason=msg.content)
            await msg.reply(f"Muted {user.mention} for {f'{weeks} weeks ' if weeks else ''}{f'{days} days ' if days else ''}{f'{hrs} hours ' if hrs else ''}{f'{mins} minutes ' if mins else ''}{f'{secs} seconds' if secs else ''}")
        except errors.Forbidden:
            await msg.reply(f"**I can't mute {user.mention}**\n\nKindly make sure that I have the necessary permissions and that the user isn't superior to me")

async def unmute(msg):
    for user in msg.mentions:
        try:
            await user.timeout(None, reason=msg.content)
            await msg.reply(f"Unmuted {user.mention}")
        except errors.Forbidden:
            await msg.reply(f"**I can't unmute {user.mention}**\n\nKindly make sure that I have the necessary permissions and that the user isn't superior to me")