from . import helpers

class SkillGraph(object):
    """
    Top level graph holding a consistent view of skills, people, and their
    relationships.
    """

    def __init__(self):
        super(SkillGraph, self).__init__()
        self.people = set()
        self.skills = set()
        self.people_skills = set()

    def print_stats(self):
        print("--")
        print("Graph stats: ")
        print("  🙂 People:        {}".format(len(self.people)))
        print("  🔨 Skills:        {}".format(len(self.skills)))
        print("  ↔️  People Skills: {}".format(len(self.skills)))
        print("--")

    def add_checking_for_duplicates(self, name, collection):
        if name in collection:
            raise Exception("Duplicate entry: " + name)
        collection.add(name)

    def add_person(self, person_name):
        self.add_checking_for_duplicates(person_name, self.people)

    def add_skill(self, skill_name):
        self.add_checking_for_duplicates(skill_name, self.skills)

    def add_person_skill(self, person_name, skill_name):
        if not person_name in self.people:
            raise Exception("Unknown person: " + person_name)

        if not skill_name in self.skills:
            raise Exception("Unknown skill: " + skill_name)

        self.add_checking_for_duplicates(tuple((person_name, skill_name)), self.people_skills)

    def get_people_names(self):
        return self.people

    def get_skill_names(self):
        return self.skills

    def get_people_skills(self):
        return self.people_skills
