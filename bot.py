# bot.py
import os

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = int(os.getenv('GUILD_ID'))
CHANNEL = int(os.getenv('MONITOR_CHANNEL_ID'))
DB_FILE = f'{GUILD}-{CHANNEL}.sqlite'
CUSTOMIZATION = os.getenv('CUSTOMIZATION')

import constants
if CUSTOMIZATION == "metagame":
    constants.apply_metagame_customization()
elif CUSTOMIZATION == "raidguild":
    constants.apply_raidguild_customization()


import bot
import repository

repo = repository.SqliteRepository(DB_FILE)

commands = [
    bot.HelpCommand,
    bot.InfoCommand,
    bot.ListSkillsCommand,
    bot.StatsCommand,
    bot.AddSkillCommand,
    bot.DrawFullGraphCommand,
    bot.DrawWordCloudCommand,
    bot.DrawPeopleSubgraphCommand,
    bot.DrawSkillsSubgraphCommand,
]

bot.Controller(GUILD, CHANNEL, repo, commands).run(TOKEN)
