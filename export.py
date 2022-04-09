import os
import sys
import json

import repository
import model
from render import *

input_files = sys.argv[1:]

print(f"Exporting {len(input_files)} databases...")

for input_file in input_files:
    json_output_file = input_file + "-export.json"
    js_output_file = input_file + "-export.js"

    print(f"Reading {input_file}")
    repo = repository.SqliteRepository(input_file)
    gs = repo.get_graph_snapshot()

    print(f"Exporting {json_output_file}")
    graph = {
        'people': [
            {
                'id': person.id,
                'name': person.name,
            } for person in gs.people.values()
        ],
        'skills': [
            {
                'id': skill.id,
                'name': skill.name,
            } for skill in gs.skills.values()
        ],
        'links': [
            {
                'person': link[0].id,
                'skill': link[1].id,
            } for link in gs.people_skills
        ],
    }
    with open(json_output_file, 'w') as f:
        json.dump(graph, f, indent=2)

    print(f"Exporting {js_output_file}")
    with open(js_output_file, 'w') as f:
        f.write('var people = [\n')
        for p in gs.people.values():
            f.write('    {id: "p-'+str(p.id)+'", name: "'+p.name+'"},\n')
        f.write(']\n')
        f.write('\n')
        f.write('var skills = [\n')
        for s in gs.skills.values():
            f.write('    {id: "s-'+str(s.id)+'", name: "'+s.name+'"},\n')
        f.write(']\n')
        f.write('\n')
        f.write('var people_skills = [\n')
        for ps in gs.people_skills:
            f.write('    {person: "p-'+str(ps[0].id)+'", skill: "s-'+str(ps[1].id)+'"},\n')
        f.write(']\n')
        f.write('\n')
