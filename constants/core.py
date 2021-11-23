# Hacky way to customize strings across multiple servers/channels/use-cases
# Not pretty but works alright, and clean enough.

class Strings:
    COMMAND_PREFIX = '!sb'
    DESCRIPTION = 'SkillBot helps you discover **skills** among people in your community 💕'
    SKILL_ICON = '⭐️'
    REACTION="✅"
    ACCEPTED_REACTIONS = [REACTION]
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

# Light metagame customization.
# Expand to interests and hobbies in addition to skills
# Add more octopi
def apply_metagame_customization():
    print(f'Applying customization: 🐙 Metagame')
    Strings.COMMAND_PREFIX = '!sb'
    Strings.DESCRIPTION = 'SkillBot helps you discover common **interests**, **skills**, **hobbies** among players 🐙'
    Strings.SKILL_ICON = '🐙'
    Strings.REACTION="✅"
    Strings.ACCEPTED_REACTIONS = ["✅"]
    Strings.PEOPLE = 'players'
    Strings.PEOPLE_UPPERCASE = 'Players'
    Strings.ENTITIES_LONG = 'skills, interests, hobbies'
    Strings.ENTITIES_LONG_UPPERCASE = 'Skills, Interests, Hobbies'
    Strings.ENTITY_SHORT = "skill/interest/hobbies"
    Strings.HELLO_TITLE = '🐙 Hello MetaGame! 🐙'
    Strings.INFO_MESSAGE = Strings.DESCRIPTION + '''
        This bot is an experimental multiplayer **game** to facilitate discovery of common interests among players.

        Suggestions? Bugs? Wanna help?
        Ping @mprime.

        Source: <https://github.com/MetaFam/skill-bot>
    '''
    Strings.PEOPLE = 'players'
    Strings.WORD_CLOUD_SIZE = 'number of players'
    Strings.ERROR_CONTACT_PERSON = '@mprime'
    Strings.REACTION_REASON = 'have this skill/interest/hobby'
    Strings.NEW_COMMAND_EXAMPLES = ["NFTs", "Python", "debating"]
    Strings.NEW_SKILL_REGEX = '^[\w][\w_]+$'
    Strings.DRAW_SKILLS_COMMAND_NAME = 'skills'
    Strings.DRAW_SKILLS_COMMAND_EXAMPLES = ["nft web3", "cooking"]

# Light RaidGuild customization
def apply_raidguild_customization():
    print(f'Applying customization: ⚔️ RaidGuild')
    Strings.DESCRIPTION = 'SkillBot (*RaidGuild edition*) helps you find members based on their skills and abilities'
    Strings.SKILL_ICON = '⚔️'
    Strings.REACTION="🙋"
    Strings.ACCEPTED_REACTIONS = ["✅", "🙋"]
    Strings.PEOPLE = 'raiders'
    Strings.PEOPLE_UPPERCASE = 'Raiders'
    Strings.ENTITIES_LONG = 'skills and abilities'
    Strings.ENTITIES_LONG_UPPERCASE = "Skills and Abilities"
    Strings.ENTITY_SHORT = 'skills/abilities'
    Strings.HELLO_TITLE = '⚔️ Greetings RaidGuild. I am Warrick. Your Quartermaster ⚔️'
    Strings.INFO_MESSAGE = Strings.DESCRIPTION + '''

        Quartermaster helps you find and recruit members based on their skills and abilities

        Suggestions? Bugs? Wanna help?
        Ping @mprime#9455

        Source: <https://github.com/MetaFam/skill-bot>
    '''
    Strings.WORD_CLOUD_SIZE = 'number of people'
    Strings.REACTION_REASON = 'have this skill or ability'
    Strings.NEW_COMMAND_EXAMPLES = ["typescript", "solidity", "design"]
    Strings.NEW_SKILL_REGEX = '^[\w][\w_]+$'
    Strings.DRAW_SKILLS_COMMAND_NAME = 'skills'
    Strings.DRAW_SKILLS_COMMAND_EXAMPLES = ["React", "IPFS", "solidity smart-contracts"]
