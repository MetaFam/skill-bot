import discord

# Hacky way to customize strings across multiple servers/channels/use-cases
# Not pretty but works alright, and clean enough.
class Cosmetics:
    # Note that custom fonts are not guaranteed to be installed on the system
    RENDER_CLOUD_FONT = "Source Serif Pro"
    RENDER_ELLIPSE_COLOR = "#B66AD6"
    RENDER_RECTANGLE_COLOR = "#FF3864"

    DISCORD_MESSAGE_COLOR = discord.Colour.magenta()

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

    NEW_SKILL_REGEX = '^[\w][\w_]+$'
    EMOJI_REGEX = r'[^!\w\s,]'

    COMMAND_PREFIX = '!sb'
    SKILL_ICON = '⭐️'
    REACTION="✅"
    ACCEPTED_REACTIONS = [REACTION]
    
    DESCRIPTION = 'SkillBot helps you discover **skills** among people in your community 💕'
    PEOPLE = 'people'
    PEOPLE_UPPERCASE = 'People'
    ENTITIES_LONG = 'skills'
    ENTITIES_LONG_UPPERCASE = 'Skills'
    ENTITY_SHORT = "skill"
    HELLO_TITLE = 'Hello World!'
    PEOPLE = 'people'
    WORD_CLOUD_SIZE = 'number of people'
    ERROR_CONTACT_PERSON = '@mprime#9455, @flip#3394, @govinda#3746'
    REACTION_REASON = 'have this skill'
    NEW_COMMAND_EXAMPLES = ["fishing", "dancing"]
    DRAW_SKILLS_COMMAND_NAME = 'skills'
    DRAW_SKILLS_COMMAND_EXAMPLES = ["hunt farm", "ui ux design"]

    STATS_MESSAGE_TITLE = "📊\nStatistics"
    MAP_MESSAGE_TITLE = "☝️\nHere's your map!"
    HELP_MESSAGE_TITLE = "❓\nHelp!"
    LIST_MESSAGE_TITLE = "List of skills:"
    INFO_MESSAGE_TITLE = "ℹ️\nInfo!"
    WORD_CLOUD_MESSAGE_TITLE = "☝️\nHere's your words cloud!"

    INFO_MESSAGE_DESCRIPTION = DESCRIPTION + '''
        This bot is an experimental multiplayer community **game** to facilitate discovery of skills among community members.

        Source: <https://github.com/MetaFam/skill-bot>
    '''
    LIST_MESSAGE_DESCRIPTION = "Click on the **show** link to jump to the skill"

    COMMAND_ERROR_MESSAGE = "🤦‍♂️\nOoops!"
    DUPLICATE_SKILL_ERROR_MESSAGE = "Entry already exists!"
    DRAW_PEOPLE_ERROR_MESSAGE = 'Could not find the people. Make sure the people have an \'@\' before their handle!'

# Calling this method is needed to define formatted strings
def apply_generic_string_formatting():
    Strings.DUPLICATE_SKILL_ERROR_MESSAGE = f'''
        The {Strings.ENTITY_SHORT} already exists!
        You should react with {Strings.REACTION} to the original message:
        https://discord.com/channels/{{}}/{{}}/{{}}
    '''
    Strings.LIST_MESSAGE_TITLE = f'List of {Strings.ENTITIES_LONG} (page {{}} / {{}})'
    Strings.LIST_MESSAGE_DESCRIPTION = f"Click on the **show** link to jump to the {Strings.ENTITY_SHORT}"

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
    Strings.INFO_MESSAGE_DESCRIPTION = Strings.DESCRIPTION + f'''
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
    Strings.INFO_MESSAGE_DESCRIPTION = f'''
        After countless raids and demons slain, the Guild has appointed me as the Quartermaster.
        
        My is to job help you find fellow Guild members based on their skills and abilities.
        {Strings.RG_WARRIOR_EMOJI_CODE} {Strings.RG_ALCHEMIST_EMOJI_CODE} {Strings.RG_ARCHER_EMOJI_CODE} {Strings.RG_MONK_EMOJI_CODE} {Strings.RG_TAVERN_EMOJI_CODE}

        Suggestions? Bugs? Wanna help?
        Ping {Strings.ERROR_CONTACT_PERSON}

        Source: <https://github.com/MetaFam/skill-bot>
    '''
    Strings.WORD_CLOUD_SIZE = 'number of raiders'
    Strings.REACTION_REASON = 'have this skill or ability'
    Strings.NEW_COMMAND_EXAMPLES = ["typescript", "solidity ♦", f"design {Strings.TRIANGLE_RULER_EMOJI_CODE}"]
    Strings.NEW_SKILL_REGEX = '^[\w][\w_]+$'

    Strings.STATS_MESSAGE_TITLE = f"{Strings.MECHANICAL_ARM_EMOJI_CODE} \nSee how mighty our Guild is! Death to Moloch!"
    Strings.MAP_MESSAGE_TITLE = "⚔\nBehold the skills of our guild!"
    Strings.HELP_MESSAGE_TITLE = f"{Strings.SCROLL_EMOJI_CODE} \n How may I assist you, adventurer?"
    Strings.LIST_MESSAGE_TITLE = f'Arsenal of {Strings.ENTITIES_LONG} (page {{}} / {{}})'
    Strings.INFO_MESSAGE_TITLE = f"{Strings.SCROLL_EMOJI_CODE} \n Stay a while and listen..."
    Strings.WORD_CLOUD_MESSAGE_TITLE = f"Word size is proportional to number of raiders..."

    Strings.LIST_MESSAGE_DESCRIPTION = f"Click upon the **show** link to jump to the {Strings.ENTITY_SHORT}, adventurer!"

    Strings.DRAW_SKILLS_COMMAND_NAME = 'skills'
    Strings.DRAW_SKILLS_COMMAND_EXAMPLES = ["React", "IPFS", "solidity smart-contracts"]

    Strings.DUPLICATE_SKILL_ERROR_MESSAGE = f'''
        We already have these {Strings.ENTITY_SHORT} in our arsenal!

        Might I suggest reacting with {Strings.REACTION} to the original message:
        https://discord.com/channels/{{}}/{{}}/{{}}
    '''
    Strings.DRAW_SKILLS_ERROR_MESSAGE = f'Could not find the {Strings.ENTITY_SHORT}.'
    Strings.DRAW_PEOPLE_ERROR_MESSAGE = f'Could not find the {Strings.PEOPLE}. Make sure the {Strings.PEOPLE} have an \'@\' before their handle!'
    Strings.COMMAND_ERROR_MESSAGE = f"{Strings.COLLISION_EMOJI_CODE} \nYou seem to be mistaken..."

    Cosmetics.COLOR = discord.Colour.magenta()