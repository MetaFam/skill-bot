# bot.py
import os

from dotenv import load_dotenv

import skillbot
import skillgraph

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = int(os.getenv('GUILD_ID'))
CHANNEL = int(os.getenv('MONITOR_CHANNEL_ID'))

graph = skillgraph.SkillGraph()
bot = skillbot.Controller(GUILD, CHANNEL, graph)

# Begin test data
# graph.add_skill(111, "Hunting")
# graph.add_skill(222, "Fishing")
# graph.add_skill(333, "Farming")
#
# graph.add_person(1, "Joe")
# graph.add_person(2, "Sammy")
#
# graph.add_person_skill(1, 111)
# graph.add_person_skill(2, 111)
# graph.add_person_skill(1, 222)
# graph.add_person_skill(2, 333)
# End test data


bot.run(TOKEN)
