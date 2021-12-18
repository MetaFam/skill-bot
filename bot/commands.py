import re
from discord import File

from constants import Strings as k
from . import messages

class AbstractCommand(object):
    """Base class for commands"""

    def __init__(self, message):
        super(AbstractCommand, self).__init__()
        self.message = message

    async def execute(self, client):
        raise Exception(f'Execute not implemented for {self}')

class HelpCommand(AbstractCommand):
    """Responds with a message with bot usage info and commands"""

    _name = "help"
    _description = "Display bot usage and help"
    _example_arguments = None

    def __init__(self, message, args):
        super(HelpCommand, self).__init__(message)

    async def execute(self, client):
        await self.message.channel.send(
            embed=messages.help_message(client.get_commands())
        )

class InfoCommand(AbstractCommand):
    """Responds with a message with bot information"""

    _name = "info"
    _description = "Display bot info"
    _example_arguments = None

    def __init__(self, message, args):
        super(InfoCommand, self).__init__(message)

    async def execute(self, client):
        await self.message.channel.send(embed=messages.INFO)


class AddSkillCommand(AbstractCommand):
    """Creates a new skill in the graph"""

    _name = "new"
    _description = f'Creates new {k.ENTITY_SHORT}'
    _example_arguments = k.NEW_COMMAND_EXAMPLES
    _skill_re = re.compile(k.NEW_SKILL_REGEX)

    def __init__(self, message, args):
        super(AddSkillCommand, self).__init__(message)
        print(f'🐛 Args: {args}')
        if not args:
            raise Exception("Missing skill name :shrug:")
        skill_name = re.sub(r'\W+', '_', args)
        print(f'🐛 skill_name: {skill_name}')
        if not AddSkillCommand._skill_re.match(skill_name):
            raise Exception(f'Invalid {k.ENTITY_SHORT} name :shrug:')
        self.skill_name = skill_name.lower()

    async def execute(self, client):
        await client.create_skill(self.skill_name)

class ListSkillsCommand(AbstractCommand):
    """A summary message with all skills"""

    _name = "list"
    _description = f'List all {k.ENTITIES_LONG}'
    _example_arguments = None

    def __init__(self, message, args):
        super(ListSkillsCommand, self).__init__(message)

    async def execute(self, client):
        await client.send_skill_recap_message(self.message.channel)

class StatsCommand(AbstractCommand):
    """A summary message with entities count"""

    _name = "stats"
    _description = "Display statistics"
    _example_arguments = None

    def __init__(self, message, args):
        super(StatsCommand, self).__init__(message)

    async def execute(self, client):
        await client.send_stats_message(self.message.channel)

class DrawFullGraphCommand(AbstractCommand):
    """Creates an image of the whole graph"""

    _name = "fullgraph"
    _description = f'Draws the full graph of {k.PEOPLE} and {k.ENTITIES_LONG}'
    _example_arguments = None

    def __init__(self, message, args):
        super(DrawFullGraphCommand, self).__init__(message)

    async def execute(self, client):
        from render import ImageFileRenderer, FullGraphDotRenderer
        dot_graph = FullGraphDotRenderer(client.get_graph_snapshot()).render()
        png_file = ImageFileRenderer(dot_graph).render()

        m = await self.message.channel.send(
            embed=messages.FULL_GRAPH,
            file=File(png_file)
        )

class DrawWordCloudCommand(AbstractCommand):
    """Creates an word cloud image for all interests"""

    _name = "wordcloud"
    _description = f'Creates a word-cloud of {k.ENTITIES_LONG}'
    _example_arguments = None

    def __init__(self, message, args):
        super(DrawWordCloudCommand, self).__init__(message)

    async def execute(self, client):
        from render import ImageFileRenderer, WordCloudDotRenderer
        dot_graph = WordCloudDotRenderer(client.get_graph_snapshot()).render()
        png_file = ImageFileRenderer(dot_graph).render()

        m = await self.message.channel.send(
            embed=messages.WORD_CLOUD_GRAPH,
            file=File(png_file)
        )

class DrawPeopleSubgraphCommand(AbstractCommand):
    """Creates an image of the graph with a subset of people explicitly requested"""

    _name = k.PEOPLE
    _description = f'Draw graph with just a subset of {k.PEOPLE}'
    _example_arguments = ["@Adam @Bob @Charlie"]

    def __init__(self, message, args):
        super(DrawPeopleSubgraphCommand, self).__init__(message)
        if not args:
            raise Exception(f"{k.COMMAND_PREFIX} {k.PEOPLE} had no {k.PEOPLE} supplied!")
        mentions = re.findall('<@(?:!)?(\d+)>', args)
        print(f'🐛 mentions: {mentions}')
        if not mentions:
            ex_msg = f"{k.DRAW_PEOPLE_ERROR_MESSAGE} _Example_ `{k.COMMAND_PREFIX} {k.PEOPLE} {self._example_arguments[0]}`"
            raise Exception(ex_msg)
        self.people_ids = [int(m) for m in mentions]

    async def execute(self, client):
        from render import ImageFileRenderer, SubGraphDotRenderer
        dot_graph = SubGraphDotRenderer(client.get_people_subgraph_snapshot(self.people_ids)).render()
        png_file = ImageFileRenderer(dot_graph).render()

        m = await self.message.channel.send(
            embed=messages.people_subgraph_message(self.people_ids),
            file=File(png_file)
        )

class DrawSkillsSubgraphCommand(AbstractCommand):
    """Creates an image of the graph with a subset of skills explicitly requested"""

    _name = k.DRAW_SKILLS_COMMAND_NAME
    _description = f'Draw graph with just a subset of {k.ENTITIES_LONG}'
    _example_arguments = k.DRAW_SKILLS_COMMAND_EXAMPLES

    def __init__(self, message, args):
        super(DrawSkillsSubgraphCommand, self).__init__(message)
        if not args:
            raise Exception(f'No {k.ENTITY_SHORT} supplied!')
        terms = [re.sub(r'\W+', '_', term) for term in args.split()]
        print(f'🐛 terms: {terms}')
        if not terms:
            raise Exception(f'{k.DRAW_SKILLS_ERROR_MESSAGE}. {k.ENTITY_SHORT} supplied ({repr(terms)}) not recognized!')
        self.terms = terms

    async def execute(self, client):
        skill_ids = client.search_skills(self.terms)
        from render import ImageFileRenderer, SubGraphDotRenderer
        dot_graph = SubGraphDotRenderer(client.get_skills_subgraph_snapshot(skill_ids)).render()
        png_file = ImageFileRenderer(dot_graph).render()

        m = await self.message.channel.send(
            embed=messages.skills_subgraph_message(self.terms),
            file=File(png_file)
        )
