import re
import traceback
import discord

from . import helpers

class Controller(discord.Client):
    """Top level controller for Skill Bot"""
    def __init__(self, guild_name: str, channel_name: str, skill_graph, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.guild_name = guild_name
        self.channel_name = channel_name
        self.channel_id = 745693123505553461 # TODO
        self.guild_id = 745693123505553458 # TODO
        self.skill_graph = skill_graph
        print(
            'Starting...\n'
            f'Guild (a.k.a. server): {self.guild_name}\n'
            f'Watching channel: {self.channel_name}\n'
        )
        self.skill_graph.print_stats()

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

    async def on_raw_reaction_add(self, payload):
        if not payload.member.bot and self.is_relevant_reaction(payload):
            print("🐛 + Reaction: " + str(payload))
            self.skill_graph.add_person(payload.member.id, payload.member.name)
            self.skill_graph.add_person_skill(payload.member.id, payload.message_id)

    async def on_raw_reaction_remove(self, payload):
        if self.is_relevant_reaction(payload):
            print("🐛 - Reaction: " + str(payload))
            self.skill_graph.remove_person_skill(payload.user_id, payload.message_id)

    def is_command(self, message):
        return (
            not message.author.bot and
            message.guild.name == self.guild_name and
            message.channel.name == self.channel_name and
            message.content.startswith('!sb')
        )

    def is_skill_message_reaction(self, message, reaction, member):
        return (
            message.author.id == self.user.id and
            message.guild.name == self.guild_name and
            message.channel.name == self.channel_name and
            message.content.startswith('A new skill was added') and
            not member.bot and
            reaction.emoji == "✅"
        )

    def is_relevant_reaction(self, payload):
        print("🐛 reaction payload: " + str(payload))
        return (
            payload.guild_id == self.guild_id and
            payload.channel_id == self.channel_id and
            payload.emoji.name == "✅" and
            self.skill_graph.skill_exists(payload.message_id)
        )
