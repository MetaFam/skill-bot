import re
import traceback
import discord

from . import messages

class Controller(discord.Client):
    """Top level controller for Skill Bot"""
    def __init__(self, guild_id: int, channel_id: int, repository, commands):
        super().__init__()
        self.channel_id = channel_id
        self.guild_id = guild_id
        self.repository = repository
        self.commands_map = {}
        for c in commands:
            self.commands_map[c._name] = c
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
                command = self.parse_command(message)
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

    async def create_skill(self, skill_name: str):
        sid = self.repository.find_skill(skill_name)
        if sid:
            print("🐛 Duplicate skill: " + skill_name)
            await self.get_channel(self.channel_id).send(
                embed=messages.duplicate_skill_message(skill_name, sid, self.guild_id, self.channel_id)
            )
        else:
            m = await self.get_channel(self.channel_id).send(
                embed=messages.new_skill_message(skill_name)
            )
            self.repository.add_skill(m.id, skill_name)
            await m.add_reaction("✅")


    _command_re = re.compile('^!sb ([a-z]+)( .*)?$')

    def parse_command(self, message):
        match = Controller._command_re.match(message.content)
        if not match:
            raise Exception("Unrecognized command, Try `!sb help`.")

        command_name = match.group(1)
        command_args = match.group(2)
        if command_args:
            command_args = command_args.strip()
        command_class = self.commands_map.get(command_name)

        if not command_class:
            raise Exception("Unrecognized command, Try `!sb help`.")

        return command_class(message, command_args)

    def get_commands(self):
        return self.commands_map.values()

    def get_graph_snapshot(self):
        return self.repository.get_graph_snapshot()

    async def send_skill_recap_message(self, channel):
        await channel.send(
            embed=messages.list_message(self.guild_id, self.channel_id, self.get_graph_snapshot().skills.values())
        )
