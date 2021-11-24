class Person(object):
    """Represents a person with name and some skills"""

    def __init__(self, id: int, name: str):
        super(Person, self).__init__()
        self.id = id
        self.name = name
        self.skills = set()

    def add_skill(self, skill):
        self.skills.add(skill)

class Skill(object):
    """Represents a skill (or interest), has a name and references people with this skill"""

    def __init__(self, id: int, name: str, emoji: str):
        super(Skill, self).__init__()
        self.id = id
        self.name = name
        self.emoji = emoji
        self.people = set()

    def add_person(self, person):
        self.people.add(person)

class Graph(object):
    """
    Representation of the graph with cross-referencing objects and some indexing
    """

    def __init__(self):
        super(Graph, self).__init__()
        self.people = {}
        self.skills = {}
        self.people_skills = set()

    def link_person_to_skill(self, person_id: int, skill_id: int):
        person = self.people[person_id]
        skill = self.skills[skill_id]
        person.add_skill(skill)
        skill.add_person(person)
        self.people_skills.add((person, skill))

    def add_person(self, person: Person):
        self.people[person.id] = person

    def add_skill(self, skill: Skill):
        self.skills[skill.id] = skill
