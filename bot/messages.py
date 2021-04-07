from collections.abc import Iterable

import discord

COLOR = discord.Colour.magenta()
DESCRIPTION = "SkillBot helps you discover common **interests** and **skills** among people in your community."
REACTION="✅"

HELLO = discord.Embed(
    title = "Hello World!",
    colour = COLOR,
    description = DESCRIPTION + '''

        Try `!sb help` to learn more.
    '''
)

HELP = discord.Embed(
    title = "❓\nHelp!",
    colour = COLOR,
    description = '''
        `...`
    '''
)

INFO = discord.Embed(
    title = "ℹ️\nInfo!",
    colour = COLOR,
    description = DESCRIPTION + '''
        This bot is an experiment (more precisely, a hack for MetaFest 2021).

        Suggestions? Bugs? Wanna help?
        Ping @mprime on Metagame.
    '''
)

FULL_GRAPH = discord.Embed(
    title = "☝️\nHere's your map!",
    colour = COLOR,
    description = "It includes *all* skills, interests and people"
)

WORD_CLOUD_GRAPH = discord.Embed(
    title = "☝️\nHere's your words cloud!",
    colour = COLOR,
    description = "More common interests are bigger in size"
)

def command_error_message(command, e):
    return discord.Embed(
        title = "🤦‍♂️\nOoops!",
        colour = COLOR,
        description = f'''
            Something went wrong with command: `{command}`

            {repr(e)}

            **If you think this is a bug**, give a shout to @mprime
        '''
    )

def new_skill_message(skill_name):
    return discord.Embed(
        title = f'⭐️ {skill_name} ⭐️',
        colour = COLOR,
        description = f'''
            New skill/interest created.

            **React with {REACTION} to this message if you have this skill or interest**
        '''
    )

def duplicate_skill_message(skill_name: str, skill_id: int, guild_id: int, channel_id: int):
    return discord.Embed(
        title = f'Duplicate {skill_name}',
        colour = COLOR,
        description = f'''
            The skill you tried to create already exists!

            You should react with {REACTION} to the original message:
            https://discord.com/channels/{guild_id}/{channel_id}/{skill_id}
        '''
    )

def help_message(commands):
    embed = discord.Embed(
        title = "❓\nHelp!",
        colour = COLOR,
        description = f'''
            To create a new skill or interest that does not exist yet, see the command below.
            People can then mark themselves able (for a skill) or interested (for an interest) by reacting with {REACTION} to the bot message.
        '''
    )
    for c in commands:
        command_string = f"`!sb {c._name}`"
        description = c._description
        if c._example_arguments:
            for ex in c._example_arguments:
                description += f'\n*Example*: `!sb {c._name} {ex}`'
        embed.add_field(name=command_string, value=description)
    return embed

def list_message(guild_id: int, channel_id: int, skills: Iterable):
    embed = discord.Embed(
        title = f'Skills and interests recap',
        colour = COLOR,
        description = f'''
            {len(skills)} skills:
        '''
    )
    for skill in skills:
        name_link=f'⭐️ {skill.name}'
        description=f'''
            [show](https://discord.com/channels/{guild_id}/{channel_id}/{skill.id})
            Linked to {1} people
        '''
        embed.add_field(name=name_link, value=description)
    return embed
