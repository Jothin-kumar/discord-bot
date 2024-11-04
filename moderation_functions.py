from datetime import timedelta


async def kick(msg):
    for user in msg.mentions:
        await user.kick(reason=msg.content)
        await msg.reply(f"Kicked {user.mention}")

async def ban(msg):
    for user in msg.mentions:
        await user.ban(reason=msg.content)
        await msg.reply(f"Banned {user.mention}")

async def mute(msg):
    days = 0
    hrs = 0
    mins = 1
    secs = 0
    for word in "".join([l for l in msg.content if l.isalphanum() or l == " "]).split()[::-1]:
        try:
            match word[-1]:
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
    for user in msg.mentions:
        await user.timeout(
            timedelta(days=days, hours=hrs, minutes=mins, seconds=secs),
            reason=msg.content
        )
        await msg.reply(f"Muted {user.mention} for {f'{days} days ' if days else ''}{f'{hrs} hours ' if hrs else ''}{f'{mins} minutes ' if mins else ''}{f'{secs} seconds' if secs else ''}")

async def unmute(msg):
    for user in msg.mentions:
        await user.timeout(None, reason=msg.content)
        await msg.reply(f"Unmuted {user.mention}")