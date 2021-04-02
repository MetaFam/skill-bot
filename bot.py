# bot.py
import os

from dotenv import load_dotenv

import bot
import skillgraph

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = int(os.getenv('GUILD_ID'))
CHANNEL = int(os.getenv('MONITOR_CHANNEL_ID'))
DB_FILE = f'{GUILD}-{CHANNEL}.sqlite'

graph = skillgraph.SqliteSkillGraph(DB_FILE)

bot.Controller(GUILD, CHANNEL, graph).run(TOKEN)
