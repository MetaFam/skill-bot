import os
import sys

import repository
import model
from render import *

input_files = sys.argv[1:]

print(f"Exporting {len(input_files)} databases...")

for input_file in input_files:
    output_file = input_file + "-export.json"
    print(f"Processing {input_file} => {output_file}")
    repo = repository.SqliteRepository(input_file)
    gs = repo.get_graph_snapshot()
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
    with open(output_file, 'w') as f:
        json.dump(graph, f, indent=2)
