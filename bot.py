# bot.py
import os

from dotenv import load_dotenv

import skillbot
import skillgraph

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_NAME')
CHANNEL = os.getenv('MONITOR_CHANNEL_NAME')

graph = skillgraph.SkillGraph()
bot = skillbot.Controller(GUILD, CHANNEL, graph)

bot.run(TOKEN)
