# bot.py
import os

from dotenv import load_dotenv

import skillbot

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_NAME')
CHANNEL = os.getenv('MONITOR_CHANNEL_NAME')

skillbot.Controller(GUILD, CHANNEL).run(TOKEN)
