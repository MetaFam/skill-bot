import re

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
    _example = None

    def __init__(self, message, args):
        super(HelpCommand, self).__init__(message)

    async def execute(self, client):
         await self.message.channel.send(
            "Skillbot help:\n"
            "```\n"
            "...\n"
            "```\n"
        )

class InfoCommand(AbstractCommand):
    """Responds with a message with bot information"""

    _name = "info"
    _description = "Display bot info"
    _example = None

    def __init__(self, message, args):
        super(InfoCommand, self).__init__(message)

    async def execute(self, client):
         await self.message.channel.send(
            "Skillbot info:\n"
            "```\n"
            "...\n"
            "```\n"
        )

class AddSkillCommand(AbstractCommand):
    """Creates a new skill in the graph"""

    _name = "new"
    _description = "Create a new skill"
    _example = None
    _skill_re = re.compile('^[\w][\w_]+$')

    def __init__(self, message, args):
        super(AddSkillCommand, self).__init__(message)
        print(f'🐛 Args: {args}')
        skill_name = re.sub(r'\W+', '_', args)
        print(f'🐛 skill_name: {skill_name}')
        if not AddSkillCommand._skill_re.match(skill_name):
            raise Exception("Invalid skill name :shrug:")
        self.skill_name = skill_name

    async def execute(self, client):
         m = await self.message.channel.send(
            'A new skill was added to the graph:\n'
            '-----\n'
            f'  ⭐️ **{self.skill_name}** ⭐️\n'
            '-----\n'
            '*If you have this skill, react with ✅ to this message*'
         )
         await m.add_reaction("✅")

_commands_map = {
    HelpCommand._name: HelpCommand,
    InfoCommand._name: InfoCommand,
    AddSkillCommand._name: AddSkillCommand,
}
_command_re = re.compile('^!sb ([a-z]+)( .*)?$')

def parse_command(message):
    match = _command_re.match(message.content)
    if not match:
        raise Exception("Unrecognized command, Try `!sb help`.")

    command_name = match.group(1)
    command_args = match.group(2)
    if command_args:
        command_args = command_args.strip()
    if command_args == "":
        command_args = None
    command_class = _commands_map.get(command_name)

    if not command_class:
        raise Exception("Unrecognized command, Try `!sb help`.")

    return command_class(message, command_args)
