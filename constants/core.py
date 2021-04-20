# Hacky way to customize strings across multiple servers/channels/use-cases
# Not pretty but works alright, and clean enough.

class Strings:
    COMMAND_PREFIX = '!sb'
    DESCRIPTION = 'SkillBot helps you discover **skills** among people in your community 💕'
    SKILL_ICON = '⭐️'
    REACTION="✅"
    PEOPLE = 'people'
    PEOPLE_UPPERCASE = 'People'
    ENTITIES_LONG = 'skills'
    ENTITIES_LONG_UPPERCASE = 'Skills'
    ENTITY_SHORT = "skill"
    HELLO_TITLE = 'Hello World!'
    INFO_MESSAGE = DESCRIPTION + '''
        This bot is an experimental multiplayer community **game** to facilitate discovery of skills among community members.

        Source: <https://github.com/MetaFam/skill-bot>
    '''
    PEOPLE = 'people'
    WORD_CLOUD_SIZE = 'number of people'
    ERROR_CONTACT_PERSON = '@mprime#9455'
    REACTION_REASON = 'have this skill'
    NEW_COMMAND_EXAMPLES = ["fishing", "dancing"]
    NEW_SKILL_REGEX = '^[\w][\w_]+$'
    DRAW_SKILLS_COMMAND_NAME = 'skills'
    DRAW_SKILLS_COMMAND_EXAMPLES = ["hunt farm", "ui ux design"]
