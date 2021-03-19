
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

    async def handle_channel_message(self, message):
        print(f'Message: {message}')

        brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            (
                'Cool. Cool cool cool cool cool cool cool, '
                'no doubt no doubt no doubt no doubt.'
            ),
        ]

        if message.content == '99!':
            response = random.choice(brooklyn_99_quotes)
            await message.channel.send(response)
        elif message.content == 'eee':
            raise discord.DiscordException
