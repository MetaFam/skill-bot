import re
import traceback
import discord

from . import helpers

class Controller(discord.Client):
    """Top level controller for Skill Bot"""
    def __init__(self, guild_name: str, channel_name: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.guild_name = guild_name
        self.channel_name = channel_name
        print(
            'Starting...\n'
            f'Guild (a.k.a. server): {self.guild_name}\n'
            f'Watching channel: {self.channel_name}\n'
        )

    async def on_ready(self):
        print(f'🐛 {self.user} has connected to Discord!')
        for g in self.guilds:
            print(
                f'{self.user} connected to: {g.name} (id: {g.id})'
            )
            if g.name == self.guild_name:
                return
        raise Exception(f'Guild not found: {self.guild_name}')

    async def on_message(self, message):
        if self.is_command(message):
            print(f'🐛 Command: {message.content}\n{message}')
            try:
                command = helpers.parse_command(message)
                await command.execute(self)
            except Exception as e:
                exception_message = repr(e)
                await message.channel.send(
                    f'Command error: {exception_message}'
                )
                print(f'⚠️ Error handling message: "{message.content}":\n' + traceback.format_exc())

    async def on_reaction_add(self, reaction, member):
        message = reaction.message
        # print(f'🐛 Reaction: {reaction} Member: {member} Message: {reaction.message}')
        # if self.is_skill_message(message) and self.is_skill_reaction(reaction, member):
        #     print(f'🐛 Skill reaction: {reaction}')


    def is_command(self, message):
        return (
            not message.author.bot and
            message.guild.name == self.guild_name and
            message.channel.name == self.channel_name and
            message.content.startswith('!sb')
        )

    def is_skill_message(self, message):
        return (
            message.author.id == self.user.id and
            message.guild.name == self.guild_name and
            message.channel.name == self.channel_name and
            message.content.startswith('A new skill was added')
        )

    def is_skill_reaction(self, reaction, member):
        print(f'me? {reaction.me}')
        print(f'bot? {member.bot}')
        print(f'eq? {int(reaction.emoji)} ?= {int("✅")}')
        return (
            not reaction.me and
            not member.bot and
            str(reaction) == '✅'
        )
