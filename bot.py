# bot.py
import os

from dotenv import load_dotenv

import discord
from discord.ext import commands

import skillbot as sb

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = int(os.getenv('GUILD_ID'))
CHANNEL = int(os.getenv('CHANNEL_ID'))

bot = commands.Bot(command_prefix='!')
controller = sb.Controller()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    for g in bot.guilds:
        print(
            f'{bot.user} connected to: {g.name} (id: {g.id})'
        )
        if g.id == GUILD:
            return controller.handle_client_ready(bot)
    raise Exception("Guild not found: {GUILD}")

@bot.command(name='ns', help='Creates a new skill')
async def new_skill(ctx, skill_name: str):
    # print(ctx)
    message = ctx.message
    if message.channel.id == CHANNEL:
        await controller.handle_new_skill_command(message, skill_name)
    # await ctx.send("bar")

@bot.event
async def on_command_error(ctx, error):
    print(f'error: {error}')
    await ctx.send(f'❌ Error: {error}')


# @bot.event
# async def on_message(message):
#     if message.author != bot.user and message.channel.id == CHANNEL:
#         await controller.handle_channel_message(message)


bot.run(TOKEN)
