# bot.py
import os

import discord
from dotenv import load_dotenv

import skillbot as sb

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = int(os.getenv('GUILD_ID'))
CHANNEL = int(os.getenv('CHANNEL_ID'))

client = discord.Client()
controller = sb.Controller()

def print_message(message):
    if message == None:
        return

    print(f'Message: {message}')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for g in client.guilds:
        print(
            f'{client.user} connected to: {g.name} (id: {g.id})'
        )
        if g.id == GUILD:
            return controller.handle_client_ready(client)
    raise Exception("Guild not found: {GUILD}")

@client.event
async def on_message(message):
    if message.author != client.user and message.channel.id == CHANNEL:
        await controller.handle_channel_message(message)

client.run(TOKEN)
