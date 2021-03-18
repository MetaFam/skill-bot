# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = int(os.getenv('GUILD_ID'))
CHANNEL = int(os.getenv('CHANNEL_ID'))

client = discord.Client()
guild = None

def print_message(message):
    if message == None:
        return

    print(f'Message: {message}')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for g in client.guilds:
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{g.name}(id: {g.id})'
        )
        if g.id == GUILD:
            print("Found Guild: " + g.name)
            guild = g

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel.id != CHANNEL:
        return
    print_message(message)

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

client.run(TOKEN)
