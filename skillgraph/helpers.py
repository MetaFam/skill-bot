import csv
import hashlib

def load_from_csv_directory(graph, csv_directory):
    print("⏳ Loading CSV data from directory: {}".format(csv_directory))

    people_file = csv_directory.rstrip("/") + "/people.csv"
    skills_file = csv_directory.rstrip("/") + "/skills.csv"
    people_skills_file = csv_directory.rstrip("/") + "/people_skills.csv"

    with open (people_file, 'r') as f:
        for line in f:
            graph.add_person(line.strip())

    with open (skills_file, 'r') as f:
        for line in f:
            graph.add_skill(line.strip())

    with open (people_skills_file, 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            if len(row) == 0:
                pass
            if len(row) != 2:
                raise Exception("Invalid line: " + str(row))
            graph.add_person_skill(row[0].strip(), row[1].strip())

    print("✅ Graph CSV data loaded!")

    graph.print_stats()

def node_hash(name):
    return "n" + hashlib.md5(name.encode()).hexdigest()

def export_as_dotfile(graph, dot_file_path):
    print("⏳ Exporting graph to DOT format in: {}".format(dot_file_path))

    with open (dot_file_path, 'w') as file:
        file.write('graph graphname {\n')
        file.write('  layout=neato\n')

        for name in graph.get_people_names():
            nid = node_hash(name)
            file.write("  {} [shape=box,label=\"{}\"]\n".format(nid, name))

        for skill in graph.get_skill_names():
            sid = node_hash(skill)
            ssize = 20
            file.write("  {} [shape=ellipse,label=\"{}\",fontsize={}]\n".format(sid, skill, ssize))

        for name, topic in graph.get_people_skills():
            nid = node_hash(name)
            tid = node_hash(topic)
            file.write("  {} -- {}\n".format(nid, tid))

        file.write('}\n')

    print("✅ Graph exported to DOT!")
