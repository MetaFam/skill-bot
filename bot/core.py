import re
import traceback
import discord

from . import commands
from . import messages

class Controller(discord.Client):
    """Top level controller for Skill Bot"""
    def __init__(self, guild_id: int, channel_id: int, repository, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.channel_id = channel_id
        self.guild_id = guild_id
        self.repository = repository
        print(
            'Starting...\n'
            f'Guild (a.k.a. server): {self.guild_id}\n'
            f'Watching channel: {self.channel_id}\n'
        )
        self.repository.print_stats()

    async def on_ready(self):
        print(f'🐛 {self.user} has connected to Discord!')
        for g in self.guilds:
            print(
                f'{self.user} connected to: {g.name} (id: {g.id})'
            )
            if g.id == self.guild_id:
                await g.get_channel(self.channel_id).send(embed=messages.HELLO)
                return
        raise Exception(f'Guild not found: {self.guild_id}')

    async def on_message(self, message):
        if self.is_command(message):
            print(f'🐛 Command: {message.content}')
            try:
                command = commands.parse_command(message)
                await command.execute(self)
            except Exception as e:
                print(f'⚠️ Error handling message: "{message.content}":\n' + traceback.format_exc())
                await message.channel.send(
                    embed=messages.command_error_message(message.content, e)
                )

    async def on_raw_reaction_add(self, payload):
        if not payload.member.bot and self.is_relevant_reaction(payload):
            print("🐛 + Reaction")
            self.repository.add_person(payload.member.id, payload.member.name)
            self.repository.add_person_skill(payload.member.id, payload.message_id)

    async def on_raw_reaction_remove(self, payload):
        if self.is_relevant_reaction(payload):
            print("🐛 - Reaction")
            self.repository.remove_person_skill(payload.user_id, payload.message_id)

    def is_command(self, message):
        return (
            not message.author.bot and
            message.guild.id == self.guild_id and
            message.channel.id == self.channel_id and
            message.content.startswith('!sb')
        )

    def is_relevant_reaction(self, payload):
        # print("🐛 reaction payload: " + str(payload))
        return (
            payload.guild_id == self.guild_id and
            payload.channel_id == self.channel_id and
            payload.emoji.name == "✅" and
            self.repository.skill_exists(payload.message_id)
        )
    
    def create_skill(self, skill_id: int, skill_name: str):
        self.repository.add_skill(skill_id, skill_name)
