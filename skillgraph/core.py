from . import helpers

class SkillGraph(object):
    """
    Graph holding a consistent view of skills, people, and their
    relationships.
    """

    def __init__(self):
        super(SkillGraph, self).__init__()
        self.people = {}
        self.skills = {}
        self.people_skills = []

    def print_stats(self):
        print("--")
        print("Graph stats: ")
        print("  🙂 People:      {}".format(len(self.people)))
        print("  🔨 Skills:      {}".format(len(self.skills)))
        print("  ↔️  Connections: {}".format(len(self.people_skills)))
        print("--")

    def add_skill(self, skill_id: int, skill_name: str):
        print(f'🌐 Add skill: {skill_name} (id: {skill_id})')
        self.skills[skill_id] = skill_name

    def add_person(self, person_id: int, person_name: str):
        print(f'🌐 Add person: {person_name} (id: {person_id})')
        self.people[person_id] = person_name

    def add_person_skill(self, skill_id: int, person_id: int):
        print(f'🌐 Link person: {person_id} to skill: {skill_id}')
        self.people_skills.append((skill_id, person_id))
