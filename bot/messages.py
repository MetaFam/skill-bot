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
        `...`
    '''
)

FULL_GRAPH = discord.Embed(
    title = "☝️\nHere's your map!",
    colour = COLOR,
    description = "It includes *all* skills, interests and people"
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
        title = f'⭐️\n{skill_name}',
        colour = COLOR,
        description = f'''
            New skill/interest created.

            **React with {REACTION} to this message if you have this skill or interest**
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
                description += f'\n*Example*: `!sb {c._name}` {ex}'
        embed.add_field(name=command_string, value=description)
    return embed
