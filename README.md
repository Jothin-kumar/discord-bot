# Discord server bot

Built for using in [Jothin Kumar's Discord server](https://joth.in/dc). Open source and free for anyone to use.

Currently, the bot is in development and only has moderation commands and welcomes new users. GitHub integration and other features will be added soon.

## Configuration

- `.env` should be present in the root directory with the following content:

```env
DISCORD_TOKEN=<bot token here>
```

- `config.json` should be present in the root directory with the following content:

```json
{
    "owner-username": "<your username>",
    "welcome-channel-id": <channel id>
}
```

## Basic commands

### shutdown

ping the bot and include the word `shutdown` in the message to shut down the bot.

## Moderation commands

### muting / unmuting members (Uses discord's timeout functionality)

`mute @member1 @member2 etc... (optional reason anywhere in the message) 60s`

**All members** mentioned in any message starting with "mute" will be **muted**.

The default duration is `1 minute`. To change this, add seconds in numeric value followed by a `s` anywhere in the message (If this occurs more than once, first occurence is considered).

- Valid: `30s`
- Invalid: `30 s`

Similarly, m for minutes, h for hours, d for days and w for weeks can be used.

Due to discord limitations, the maximum duration is `4 weeks`.

To unmute a member, use the `unmute` command.

If an already muted member is muted again, the previous timeout is cancelled and the new one is set.

### Banning members

`ban @member1 @member2 etc... (optional reason anywhere in the message)`

**All members** mentioned in any message starting with "ban" will be **banned**.

### Kicking members

`kick @member1 @member2 etc... (optional reason anywhere in the message)`

**All members** mentioned in any message starting with "kick" will be **kicked**.
