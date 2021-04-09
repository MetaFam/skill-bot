
def print_graph(g):
    print(f"People: {len(g.people)}")
    for pid, p in g.people.items():
        print(f" * {p.name} ({p.id})")
        for s in p.skills:
            print(f"   - {s.name} ({s.id})")

    print(f"Skills: {len(g.skills)}")
    for sid, s in g.skills.items():
        print(f" * {s.name} ({s.id})")
        for p in s.people:
            print(f"   - {p.name} ({p.id})")

    print(f"People skills: {len(g.people_skills)}")
    for person, skill in g.people_skills:
        print(f"{person.name} <-> {skill.name}")

#############################
# Model tests
#############################

import model

p1 = model.Person(1, "Alice")
p2 = model.Person(2, "Bob")
p3 = model.Person(3, "Charles")

s1 = model.Skill(11, "Dancing")
s2 = model.Skill(22, "Fishing")

g = model.Graph()

g.add_person(p1)
g.add_person(p2)
g.add_person(p3)

g.add_skill(s1)
g.add_skill(s2)

g.link_person_to_skill(1, 11)
g.link_person_to_skill(1, 22)
g.link_person_to_skill(2, 11)
g.link_person_to_skill(3, 22)

assert g.people[p1.id] == p1
assert g.people[p2.id] == p2
assert g.people[p3.id] == p3
assert g.skills[s1.id] == s1
assert g.skills[s2.id] == s2

assert p1 in s1.people
assert p1 in s2.people
assert p2 in s1.people
assert p3 in s2.people

assert s1 in p1.skills
assert s2 in p1.skills
assert s1 in p2.skills
assert s2 in p3.skills

assert len(g.people_skills) == 4

for s in [s1, s2]:
    for p in s.people:
        assert (p, s) in g.people_skills

for p in [p1, p2, p3]:
    for s in p.skills:
        assert (p, s) in g.people_skills

print_graph(g)

#############################
# Repository tests
#############################

import os
import repository

TEST_DB_FILE = 'test-db.sqlite'

if os.path.exists(TEST_DB_FILE):
  os.remove(TEST_DB_FILE)

# Create and initialize new DB
tmp_repo = repository.SqliteRepository(TEST_DB_FILE)

# Open exsisting DB
repo = repository.SqliteRepository(TEST_DB_FILE)

# Test all tables are empty
assert repo.get_skills_count() == 0
assert repo.get_people_count() == 0
assert repo.get_people_skills_count() == 0
assert repo.get_skills()[:] == []
assert repo.get_people()[:] == []
assert repo.get_people_skills()[:] == []

# Add 3 skills
repo.add_skill(111, "Hunting")
repo.add_skill(222, "Fishing")
repo.add_skill(333, "Farming")

# Test skills
assert repo.get_skills_count() == 3
assert repo.skill_exists(111)
assert repo.skill_exists(222)
assert repo.skill_exists(333)
assert not repo.skill_exists(444)
assert repo.find_skill("Hunting") == 111
assert repo.find_skill("Fishing") == 222
assert repo.find_skill("Farming") == 333
assert repo.find_skill("Dancing") == None

skills = repo.get_skills()
assert len(skills) == 3
for s in skills:
    if s.id == 111:
        assert s.name == "Hunting"
    elif s.id == 222:
        assert s.name == "Fishing"
    elif s.id == 333:
        assert s.name == "Farming"
    else:
        assert False

# Test overwrite skill name (no effect, and no duplicates)
repo.add_skill(222, "Phishing")
assert repo.get_skills_count() == 3
skills = repo.get_skills()
assert len(skills) == 3
for s in skills:
    if s.id == 111:
        assert s.name == "Hunting"
    elif s.id == 222:
        assert s.name == "Fishing"
    elif s.id == 333:
        assert s.name == "Farming"
    else:
        assert False

# Add 2 people
repo.add_person(1, "Joe")
repo.add_person(2, "Sammy")

# Test people
assert repo.get_people_count() == 2
people = repo.get_people()
assert len(people) == 2
assert [p for p in people if p.id == 1][0].name == "Joe"
assert [p for p in people if p.id == 2][0].name == "Sammy"

# Test overwrite person name (no effect, and no duplicates)
repo.add_person(1, "Joe Reloaded")
assert repo.get_people_count() == 2
people = repo.get_people()
assert len(people) == 2
assert [p for p in people if p.id == 1][0].name == "Joe"
assert [p for p in people if p.id == 2][0].name == "Sammy"

# Add 4 people-skills relationships
repo.add_person_skill(1, 111)
repo.add_person_skill(2, 111)
repo.add_person_skill(1, 222)
repo.add_person_skill(2, 333)

# Test people skills
assert repo.get_people_skills_count() == 4
people_skills = repo.get_people_skills()
assert len(people_skills) == 4
assert (1, 111) in people_skills
assert (2, 111) in people_skills
assert (1, 222) in people_skills
assert (2, 333) in people_skills

# Remove one person skill
repo.remove_person_skill(1, 222)

# Test people skills
assert repo.get_people_skills_count() == 3
people_skills = repo.get_people_skills()
assert len(people_skills) == 3
assert (1, 111) in people_skills
assert (2, 111) in people_skills
assert not (1, 222) in people_skills
assert (2, 333) in people_skills

# Remove non-existent person skill
repo.remove_person_skill(1, 222)

# Test people skills
people_skills = repo.get_people_skills()
assert len(people_skills) == 3
assert (1, 111) in people_skills
assert (2, 111) in people_skills
assert (2, 333) in people_skills

# Add duplicate people-skills relationships
repo.add_person_skill(1, 111)
repo.add_person_skill(1, 111)
repo.add_person_skill(1, 111)

# Test people skills
people_skills = repo.get_people_skills()
assert len(people_skills) == 3
assert (1, 111) in people_skills
assert (2, 111) in people_skills
assert (2, 333) in people_skills

#############################
# Repository + model test
#############################

g = repo.get_graph_snapshot()

assert len(g.people) == 2
assert len(g.skills) == 3
assert len(g.people_skills) == 3

print_graph(g)

#############################
# Model rendering test
#############################
alice = model.Person(1, "Alice")
bob = model.Person(2, "Bob")
charles = model.Person(3, "Charles")
diana = model.Person(4, "Diana")

cooking = model.Skill(11, "Cooking")
gardening = model.Skill(22, "Gardening")
fishing = model.Skill(33, "Fishing")
hunting = model.Skill(44, "Hunting")
woodworking = model.Skill(55, "Woodworking")

g = model.Graph()

g.add_person(alice)
g.add_person(bob)
g.add_person(charles)
g.add_person(diana)

g.add_skill(cooking)
g.add_skill(gardening)
g.add_skill(fishing)
g.add_skill(hunting)
g.add_skill(woodworking)

g.link_person_to_skill(alice.id, cooking.id)
g.link_person_to_skill(alice.id, fishing.id)
g.link_person_to_skill(alice.id, hunting.id)
g.link_person_to_skill(bob.id, woodworking.id)
g.link_person_to_skill(charles.id, cooking.id)
g.link_person_to_skill(charles.id, fishing.id)
g.link_person_to_skill(diana.id, cooking.id)
g.link_person_to_skill(diana.id, gardening.id)

import os
from render import *

dot_full_graph = FullGraphDotRenderer(g).render()
png_file = ImageFileRenderer(dot_full_graph).render(path_prefix="test-full.dot")
assert png_file == "test-full.dot.jpg"
assert os.path.exists(png_file)

dot_word_cloud_graph = WordCloudDotRenderer(g).render()
png_file = ImageFileRenderer(dot_word_cloud_graph).render(path_prefix="test-word-cloud.dot")
assert png_file == "test-word-cloud.dot.jpg"
assert os.path.exists(png_file)
