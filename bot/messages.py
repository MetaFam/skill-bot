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

        Source: <https://github.com/MetaFam/skill-bot>
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

def list_message(guild_id: int, channel_id: int, skills: Iterable, num_pages: int, current_page: int):
    embed = discord.Embed(
        title = f'Skills and interests (part {current_page} / {num_pages})',
        colour = COLOR,
        description = f'''
            Click on the **show** link to jump to the skill
        '''
    )
    for skill in skills:
        name_link=f'⭐️ {skill.name}'
        description=f'''
            {len(skill.people)} people
            [show](https://discord.com/channels/{guild_id}/{channel_id}/{skill.id})
        '''
        embed.add_field(name=name_link, value=description)
    return embed

def paginated_list_messages(guild_id: int, channel_id: int, skills: Iterable, page_size: int = 25):
    paginated_skills = [skills[i:i + page_size] for i in range(0, len(skills), page_size)]
    num_pages = len(paginated_skills)
    return [list_message(guild_id, channel_id, paginated_skills[index], num_pages, index+1) for index in range(len(paginated_skills))]


def people_subgraph_message(people_ids: Iterable[int]):
    mentions = ", ".join(f'<@!{pid}>' for pid in people_ids)
    embed = discord.Embed(
        title = "☝️\nHere's your map!",
        colour = COLOR,
        description = f'''
            It includes only a subset of people: {mentions}
        '''
    )
    return embed

def skills_subgraph_message(skills_terms: Iterable[str]):
    terms_string = ", ".join(f'"{term}"' for term in skills_terms)
    embed = discord.Embed(
        title = "☝️\nHere's your map!",
        colour = COLOR,
        description = f'''
            It includes only skills matching: {terms_string}
        '''
    )
    return embed

def stats_message(people_count: int, skills_count: int, people_skills_count: int):
    embed = discord.Embed(
        title = "📊\nStatistics",
        colour = COLOR,
        description = f'''
            👤 People: {people_count}
            ⭐️ Skills & Interests: {skills_count}
            ↔️ Connections: {people_skills_count}
        '''
    )
    return embed
