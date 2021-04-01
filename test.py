
import os
import skillgraph

TEST_DB_FILE = 'test-db.sqlite'

if os.path.exists(TEST_DB_FILE):
  os.remove(TEST_DB_FILE)

# Create and initialize new DB
tmp_graph = skillgraph.SqliteSkillGraph(TEST_DB_FILE)

# Open exsisting DB
graph = skillgraph.SqliteSkillGraph(TEST_DB_FILE)

# Test all tables are empty
assert graph.get_skills()[:] == []
assert graph.get_people()[:] == []
assert graph.get_people_skills()[:] == []

# Add 3 skills
graph.add_skill(111, "Hunting")
graph.add_skill(222, "Fishing")
graph.add_skill(333, "Farming")

# Test skills
assert graph.skill_exists(111)
assert graph.skill_exists(222)
assert graph.skill_exists(333)
assert not graph.skill_exists(444)

skills = graph.get_skills()
assert len(skills) == 3
assert (111, "Hunting") in skills
assert (222, "Fishing") in skills
assert (333, "Farming") in skills

# Test overwrite skill name (no effect, and no duplicates)
graph.add_skill(222, "Phishing")
skills = graph.get_skills()
assert len(skills) == 3
assert (111, "Hunting") in skills
assert (222, "Fishing") in skills
assert (333, "Farming") in skills


# Add 2 people
graph.add_person(1, "Joe")
graph.add_person(2, "Sammy")

# Test people
people = graph.get_people()
assert len(people) == 2
assert (1, "Joe") in people
assert (2, "Sammy") in people

# Test overwrite person name (no effect, and no duplicates)
graph.add_person(1, "Joe Reloaded")
people = graph.get_people()
assert len(people) == 2
assert (1, "Joe") in people
assert (2, "Sammy") in people

# Add 4 people-skills relationships
graph.add_person_skill(1, 111)
graph.add_person_skill(2, 111)
graph.add_person_skill(1, 222)
graph.add_person_skill(2, 333)

# Test people skills
people_skills = graph.get_people_skills()
assert len(people_skills) == 4
assert (1, 111) in people_skills
assert (2, 111) in people_skills
assert (1, 222) in people_skills
assert (2, 333) in people_skills

# Remove one person skill
graph.remove_person_skill(1, 222)

# Test people skills
people_skills = graph.get_people_skills()
assert len(people_skills) == 3
assert (1, 111) in people_skills
assert (2, 111) in people_skills
assert not (1, 222) in people_skills
assert (2, 333) in people_skills

# Remove non-existent person skill
graph.remove_person_skill(1, 222)

# Test people skills
people_skills = graph.get_people_skills()
assert len(people_skills) == 3
assert (1, 111) in people_skills
assert (2, 111) in people_skills
assert (2, 333) in people_skills

# Add duplicate people-skills relationships
graph.add_person_skill(1, 111)
graph.add_person_skill(1, 111)
graph.add_person_skill(1, 111)

# Test people skills
people_skills = graph.get_people_skills()
assert len(people_skills) == 3
assert (1, 111) in people_skills
assert (2, 111) in people_skills
assert (2, 333) in people_skills
