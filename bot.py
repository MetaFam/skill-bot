# bot.py
import os

from dotenv import load_dotenv

import bot
import repository

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = int(os.getenv('GUILD_ID'))
CHANNEL = int(os.getenv('MONITOR_CHANNEL_ID'))
DB_FILE = f'{GUILD}-{CHANNEL}.sqlite'

repo = repository.SqliteRepository(DB_FILE)

bot.Controller(GUILD, CHANNEL, repo).run(TOKEN)
