# Skill Discovery (Discord bot)

This little project is a "hack" developed as part of [MetaFest](https://metafest.metagame.wtf) 2021.

### Objective

Create a graphical representation of people skills and interests.

### Why?

To facilitate social bonding and skills exchange:

 * Find someone that has skill S, which you are looking for
 * Find what skills/interests you have in common with person P
 * Get a general feel of the interests within a community
 * ...

## Project structure

#### ⚠️ HACK ALERT ⚠️
The source code of this project is **hack-level** quality.

It was stringed together in less than a week.
Please calibrate your expectations accordingly.

For example:

 * ❌ Most of the code is not covered by tests
 * ❌ Code is a hodgepodge of classes, static functions, globals, etc (thanks, Python!)
 * ❌ Some calls are not thread-safe (database, graph rendering, ...)
 * ❌ The data model is as simple as it gets
 * ❌ The rendering is pretty rudimentary
 * etc.

That said, it's in pretty good shape *for a hack*.
Future improvements (if anyone is willing) should be possible incrementally.

### Code overview

...

## Deployment

The bot requires 3 environment variables to run properly.
They can be set on the shell, or in a `.env` file.

`DISCORD_TOKEN`: Token obtained by creating a new discord application.
For examples, see [this guide](https://realpython.com/how-to-make-a-discord-bot-python/) or similar.

`GUILD_ID`: The unique numeric id of the Discord server (a.k.a guild).

`MONITOR_CHANNEL_ID`: The unique numeric ID of the Discord channel to monitor.

The easiest way to learn your server and channel IDs is to open Discord in a browser.
The URL will look like this:

> https://discord.com/channels/<guild id\>/<channel id\>/

### Dependencies

**Python 3** and it's dependencies listed in `requirements.txt`.

The `dot` program installed (on Linux and macOS, this is part of the `graphviz` package).

You can learn more about this format on [Wikipedia](https://en.wikipedia.org/wiki/Graphviz) or on the [official website](https://www.graphviz.org/).

### Permissions

To work properly, the bot needs the following permission in the target channel:

 * Read channel messages
 * Write messages to channel
 * React to messages in channel

## License

This project is released under `MIT` license. See the `LICENSE` file for details.
