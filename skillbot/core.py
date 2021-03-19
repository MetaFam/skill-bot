
import random

from . import helpers

class Controller(object):
    """
    Controller, high level logic for bot that monitors a channel, updates
    the graph and more
    """

    def __init__(self):
        super(Controller, self).__init__()

    def handle_client_ready(self, client):
        pass

    async def handle_new_skill_command(self, message, skill_name):
        m = await message.channel.send(
            f'---\n'
            f'🌟 **{skill_name}** 🌟\n'
            f'(if you have this skill, react with: 🧙)‍\n'
            f'---\n'
        )
        await m.add_reaction('🧙‍♂️')
