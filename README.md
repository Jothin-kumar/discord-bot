[`Join my Discord server`](https://joth.in/dc)

# muting members (Uses discord's timeout functionality)

`mute @member1 @member2 etc... (optional reason anywhere in the message) 60s`

**All members** mentioned in any message starting with "mute" will be **muted**.

The default duration is `60 seconds`. To change this, add seconds in numeric value followed by a `s` anywhere in the message (If this occurs more than once, first occurence is considered).
 - Valid: `30s`
 - Invalid: `30 s`

To unmute, just set the duration to `0s`.

**If an already muted member is muted again, the previous timeout is cancelled**

# Banning members

`ban @member1 @member2 etc... (optional reason anywhere in the message)`

**All members** mentioned in any message starting with "ban" will be **banned**.

# Kicking members

`kick @member1 @member2 etc... (optional reason anywhere in the message)`

**All members** mentioned in any message starting with "kick" will be **kicked**.

# Welcoming users

Welcome messages are sent in `#hello-world`.
