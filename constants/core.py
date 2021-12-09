# Hacky way to customize strings across multiple servers/channels/use-cases
# Not pretty but works alright, and clean enough.

class Strings:

    RG_WARRIOR_EMOJI_CODE = '<:warrior:720324879421014086>'
    RG_ALCHEMIST_EMOJI_CODE = '<:alchemist:750768541929832478>'
    RG_ARCHER_EMOJI_CODE = '<:archer:720324879215362109>'
    RG_MONK_EMOJI_CODE = '<:monk:756585425828839556>'
    RG_TAVERN_EMOJI_CODE = '<:tavern:750768608208224258>'

    JAPANESE_CASTLE_EMOJI_CODE = "\U0001F3EF"
    TRIANGLE_RULER_EMOJI_CODE = "\U0001F4D0"
    COLLISION_EMOJI_CODE = "\U0001F4A5"
    SCROLL_EMOJI_CODE = "\U0001F4DC"
    MECHANICAL_ARM_EMOJI_CODE = "\U0001F9BE"

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
    ERROR_CONTACT_PERSON = '@mprime#9455, @flip#3394, @govinda#3746'
    REACTION_REASON = 'have this skill'
    NEW_COMMAND_EXAMPLES = ["fishing", "dancing"]
    NEW_SKILL_REGEX = '^[\w][\w_]+$'
    EMOJI_REGEX = r'[^!\w\s,]'
    DRAW_SKILLS_COMMAND_NAME = 'skills'
    DRAW_SKILLS_COMMAND_EXAMPLES = ["hunt farm", "ui ux design"]
    DRAW_SKILLS_ERROR_MESSAGE = 'Could not find the people. Make sure the people have an \'@\' before their handle!'

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
    Strings.INFO_MESSAGE = Strings.DESCRIPTION + f'''
        This bot is an experimental multiplayer **game** to facilitate discovery of common interests among players.

        Suggestions? Bugs? Wanna help?
        Ping {Strings.ERROR_CONTACT_PERSON}.

        Source: <https://github.com/MetaFam/skill-bot>
    '''
    Strings.PEOPLE = 'players'
    Strings.WORD_CLOUD_SIZE = 'number of players'
    Strings.REACTION_REASON = 'have this skill/interest/hobby'
    Strings.NEW_COMMAND_EXAMPLES = ["NFTs", "Python", "debating"]
    Strings.NEW_SKILL_REGEX = '^[\w][\w_]+$'
    Strings.DRAW_SKILLS_COMMAND_NAME = 'skills'
    Strings.DRAW_SKILLS_COMMAND_EXAMPLES = ["nft web3", "cooking"]
    Strings.DRAW_PEOPLE_ERROR_MESSAGE = f'Could not find the {Strings.PEOPLE}. Make sure the {Strings.PEOPLE} have an \'@\' before their handle!'

# Light RaidGuild customization
def apply_raidguild_customization():
    print(f'Applying customization: ⚔️ RaidGuild')
    Strings.COMMAND_PREFIX = '!qm'
    Strings.DESCRIPTION = f'''
        After countless raids and demons slain, the Guild has appointed me as the Quartermaster.
        
        My is to job help you find fellow Guild members based on their skills and abilities.
        {Strings.RG_WARRIOR_EMOJI_CODE} {Strings.RG_ALCHEMIST_EMOJI_CODE} {Strings.RG_ARCHER_EMOJI_CODE} {Strings.RG_MONK_EMOJI_CODE} {Strings.RG_TAVERN_EMOJI_CODE}
    '''
    Strings.SKILL_ICON = '⚔️'
    Strings.REACTION="🙋"
    Strings.ACCEPTED_REACTIONS = ["✅", "🙋"]
    Strings.PEOPLE = 'raiders'
    Strings.PEOPLE_UPPERCASE = 'Raiders'
    Strings.ENTITIES_LONG = 'skills and abilities'
    Strings.ENTITIES_LONG_UPPERCASE = "Skills and Abilities"
    Strings.ENTITY_SHORT = 'skills/abilities'
    Strings.HELLO_TITLE = f'{Strings.RG_WARRIOR_EMOJI_CODE}** Good day adventurer! Welcome to the Skill Hall!** {Strings.JAPANESE_CASTLE_EMOJI_CODE}'
    Strings.INFO_MESSAGE = Strings.DESCRIPTION + f'''

        I am known by the name Quartermaster and I am here to help you find Guild members based on their skills to help you recruit and form parties.
        {Strings.RG_WARRIOR_EMOJI_CODE} {Strings.RG_ALCHEMIST_EMOJI_CODE} {Strings.RG_ARCHER_EMOJI_CODE} {Strings.RG_MONK_EMOJI_CODE} {Strings.RG_TAVERN_EMOJI_CODE}

        Suggestions? Bugs? Wanna help?
        Ping {Strings.ERROR_CONTACT_PERSON}

        Source: <https://github.com/MetaFam/skill-bot>
    '''
    Strings.WORD_CLOUD_SIZE = 'number of raiders'
    Strings.REACTION_REASON = 'have this skill or ability'
    Strings.NEW_COMMAND_EXAMPLES = ["typescript", "solidity ♦", f"design {Strings.TRIANGLE_RULER_EMOJI_CODE}"]
    Strings.NEW_SKILL_REGEX = '^[\w][\w_]+$'
    Strings.DRAW_SKILLS_COMMAND_NAME = 'skills'
    Strings.DRAW_SKILLS_COMMAND_EXAMPLES = ["React", "IPFS", "solidity smart-contracts"]
    Strings.DRAW_SKILLS_ERROR_MESSAGE = f'Could not find the {Strings.ENTITY_SHORT}.'
    Strings.DRAW_PEOPLE_ERROR_MESSAGE = f'Could not find the {Strings.PEOPLE}. Make sure the {Strings.PEOPLE} have an \'@\' before their handle!'
