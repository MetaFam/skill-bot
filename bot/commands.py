import re
from discord import File

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
    _description = "Create a new skill"
    _example_arguments = ["fishing", "dancing"]
    _skill_re = re.compile('^[\w][\w_]+$')

    def __init__(self, message, args):
        super(AddSkillCommand, self).__init__(message)
        print(f'🐛 Args: {args}')
        if not args:
            raise Exception("Missing skill name :shrug:")
        skill_name = re.sub(r'\W+', '_', args)
        print(f'🐛 skill_name: {skill_name}')
        if not AddSkillCommand._skill_re.match(skill_name):
            raise Exception("Invalid skill name :shrug:")
        self.skill_name = skill_name.lower()

    async def execute(self, client):
        await client.create_skill(self.skill_name)

class ListSkillsCommand(AbstractCommand):
    """A summary message with all skills"""

    _name = "list"
    _description = "List all skills"
    _example_arguments = None

    def __init__(self, message, args):
        super(ListSkillsCommand, self).__init__(message)

    async def execute(self, client):
        await client.send_skill_recap_message(self.message.channel)

class DrawFullGraphCommand(AbstractCommand):
    """Creates an image of the whole graph"""

    _name = "fullgraph"
    _description = "Draw the full graph"
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
    _description = "Creates a word-cloud of interests"
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

    _name = "subgraph"
    _description = "Draw graph with just a subset of people"
    _example_arguments = ["@Adam @Bob @Charlie"]

    def __init__(self, message, args):
        super(DrawPeopleSubgraphCommand, self).__init__(message)
        if not args:
            raise Exception("Missing people names :shrug:")
        mentions = re.findall('<@!(\d+)>', args)
        print(f'🐛 mentions: {mentions}')
        if not mentions:
            raise Exception("Missing people names :shrug:")
        self.people_ids = [int(m) for m in mentions]

    async def execute(self, client):
        from render import ImageFileRenderer, SubGraphDotRenderer
        dot_graph = SubGraphDotRenderer(client.get_graph_snapshot(self.people_ids)).render()
        png_file = ImageFileRenderer(dot_graph).render()

        m = await self.message.channel.send(
            embed=messages.subgraph_message(self.people_ids),
            file=File(png_file)
        )
