from collections.abc import Iterable
from typing import Tuple
import sqlite3
from os.path import exists as file_exists
import model

class SqliteRepository(object):
    """
    Graph holding a consistent view of skills, people, and their
    relationships. Implemented with SQLite3.
    """

    __DB_INIT = [
        '''
        CREATE TABLE skills (
            skill_id INTEGER PRIMARY KEY,
            skill_name TEXT NOT NULL,
            skill_emoji TEXT NOT NULL
        );
        ''',
        '''
        CREATE TABLE people (
            person_id INTEGER PRIMARY KEY,
            person_name TEXT NOT NULL
        );
        ''',
        '''
        CREATE TABLE people_skills (
            person_id INTEGER NOT NULL,
            skill_id INTEGER  NOT NULL,
            UNIQUE (person_id, skill_id)
        );
        ''',
        'CREATE UNIQUE INDEX idx_skills_id ON skills(skill_id);',
        'CREATE UNIQUE INDEX idx_skills_names ON skills(skill_name);',
        'CREATE UNIQUE INDEX idx_people_id ON people(person_id);',
        'CREATE UNIQUE INDEX idx_people_skills ON people_skills(person_id, skill_id);',
    ]

    __CREATE_IF_NOT_EXIST_PERSON = 'INSERT OR IGNORE INTO people VALUES (?, ?);'
    __CREATE_IF_NOT_EXIST_SKILL = 'INSERT OR IGNORE INTO skills VALUES (?, ?);'
    __ADD_PERSON_SKILL = 'INSERT OR IGNORE INTO people_skills VALUES (?, ?);'
    __REMOVE_PERSON_SKILL = 'DELETE FROM people_skills WHERE person_id = ? AND skill_id = ?;'
    __SKILL_EXISTS = 'SELECT EXISTS(SELECT 1 FROM skills WHERE skill_id = ?);'
    __SELECT_ALL_SKILLS = "SELECT skill_id, skill_name, skill_emoji FROM skills;"
    __SELECT_ALL_PEOPLE = "SELECT person_id, person_name FROM people;"
    __SELECT_ALL_PEOPLE_SKILLS = "SELECT person_id, skill_id FROM people_skills;"
    __COUNT_SKILLS = "SELECT COUNT(*) FROM skills;"
    __COUNT_PEOPLE = "SELECT COUNT(*) FROM people;"
    __COUNT_PEOPLE_SKILLS = "SELECT COUNT(*) FROM people_skills;"

    def __init__(self, database_file):
        super(SqliteRepository, self).__init__()
        if not file_exists(database_file):
            print(f'🌐 Initializing database: {database_file}')
            new_db_uri = f'file:{database_file}?mode=rwc'
            new_db = sqlite3.connect(new_db_uri, uri=True)
            for statement in SqliteRepository.__DB_INIT:
                new_db.execute(statement)
            new_db.close()
        db_uri = f'file:{database_file}?mode=rw'
        self.db = sqlite3.connect(db_uri, uri=True)
        # add column for emoji if it doesn't exist
        try:
            self.db.execute("ALTER TABLE skills ADD COLUMN skill_emoji TEXT")
        except:
            pass

    def print_stats(self):
        print("--")
        print("Graph stats: ")
        print("  🙂 People:      {}".format(self.get_people_count()))
        print("  🔨 Skills:      {}".format(self.get_skills_count()))
        print("  ↔️  Connections: {}".format(self.get_people_skills_count()))
        print("--")

    def add_skill(self, skill_id: int, skill_name: str):
        print(f'🌐 Add skill: {skill_name} (id: {skill_id})')
        self.db.execute(SqliteRepository.__CREATE_IF_NOT_EXIST_SKILL, [skill_id, skill_name])
        self.db.commit()

    def add_person(self, person_id: int, person_name: str):
        print(f'🌐 Add person: {person_name} (id: {person_id})')
        self.db.execute(SqliteRepository.__CREATE_IF_NOT_EXIST_PERSON, [person_id, person_name])
        self.db.commit()

    def add_person_skill(self, person_id: int, skill_id: int):
        print(f'🌐 Link person: {person_id} to skill: {skill_id}')
        self.db.execute(SqliteRepository.__ADD_PERSON_SKILL, [person_id, skill_id])
        self.db.commit()

    def remove_person_skill(self, person_id: int, skill_id: int):
        print(f'🌐 Unlink person: {person_id} to skill: {skill_id}')
        self.db.execute(SqliteRepository.__REMOVE_PERSON_SKILL, [person_id, skill_id])
        self.db.commit()

    def skill_exists(self, skill_id: int):
        return self.db.execute(SqliteRepository.__SKILL_EXISTS, [skill_id]).fetchone()[0] == 1

    def get_people_count(self) -> int:
        return int(self.db.execute(SqliteRepository.__COUNT_PEOPLE).fetchone()[0])

    def get_skills_count(self) -> int:
        return int(self.db.execute(SqliteRepository.__COUNT_SKILLS).fetchone()[0])

    def get_people_skills_count(self) -> int:
        return int(self.db.execute(SqliteRepository.__COUNT_PEOPLE_SKILLS).fetchone()[0])

    def get_skills(self) -> Iterable[model.Skill]:
        return [
            # Construct a new Skill
            model.Skill(sid, sname, semoji)
            # For each row returned
            for sid, sname, semoji in self.db.execute(SqliteRepository.__SELECT_ALL_SKILLS).fetchall()
        ]

    def find_skill(self, skill_name):
        row = self.db.execute('SELECT skill_id FROM skills WHERE skill_name = ?', [skill_name]).fetchone()
        if row:
            return row[0]
        else:
            return None

    def get_people(self) -> Iterable[model.Person]:
        return [
            # Construct a new Person
            model.Person(pid, pname)
            # For each row returned
            for pid, pname in self.db.execute(SqliteRepository.__SELECT_ALL_PEOPLE).fetchall()
        ]

    def get_people_skills(self) -> Iterable[Tuple[int, int]]:
        return self.db.execute(SqliteRepository.__SELECT_ALL_PEOPLE_SKILLS).fetchall()

    def find_people_by_id(self, people_ids: Iterable[int]) -> Iterable[model.Person]:
        ids = ','.join([str(id) for id in people_ids])
        query = f"SELECT person_id, person_name FROM people WHERE person_id IN ({ids});"
        return [
            # Construct a new Person
            model.Person(pid, pname)
            # For each row returned
            for pid, pname in self.db.execute(query).fetchall()
        ]

    def find_skills_by_id(self, skills_ids: Iterable[int]) -> Iterable[model.Skill]:
        ids = ','.join([str(id) for id in skills_ids])
        query = f"SELECT skill_id, skill_name, skill_emoji FROM skills WHERE skill_id IN ({ids});"
        return [
            # Construct a new Skill
            model.Skill(sid, sname, semoji)
            # For each row returned
            for sid, sname, semoji in self.db.execute(query).fetchall()
        ]

    def find_skills_by_name(self, skill_name: str) -> Iterable[model.Skill]:
        wildcard_name = f'%{skill_name}%'
        return [
            # Construct a new Skill
            model.Skill(sid, sname, semoji)
            # For each row returned
            for sid, sname, semoji in self.db.execute('SELECT skill_id, skill_name, skill_emoji FROM skills WHERE skill_name LIKE ?', [wildcard_name]).fetchall()
        ]

    def find_people_skills_of_people(self, people_ids: Iterable[int]) -> Iterable[Tuple[int, int]]:
        ids = ','.join([str(id) for id in people_ids])
        query = f"SELECT person_id, skill_id FROM people_skills WHERE person_id IN ({ids});"
        return self.db.execute(query).fetchall()

    def find_people_skills_of_skills(self, skills_ids: Iterable[int]) -> Iterable[Tuple[int, int]]:
        ids = ','.join([str(id) for id in skills_ids])
        query = f"SELECT person_id, skill_id FROM people_skills WHERE skill_id IN ({ids});"
        return self.db.execute(query).fetchall()

    def get_graph_snapshot(self) -> model.Graph:
        g = model.Graph()
        # Capture edges first, to avoid dangling references
        people_skills = self.get_people_skills()
        for p in self.get_people():
            g.add_person(p)
        for s in self.get_skills():
            g.add_skill(s)
        for pid, sid in people_skills:
            g.link_person_to_skill(pid, sid)
        return g

    def get_people_subgraph_snapshot(self, people_ids: Iterable[int]) -> model.Graph:
        g = model.Graph()
        # Capture edges first, to avoid dangling references
        people_skills = self.find_people_skills_of_people(people_ids)
        skill_ids = set([sid for pid, sid in people_skills])
        for p in self.find_people_by_id(people_ids):
            g.add_person(p)
        for s in self.find_skills_by_id(skill_ids):
            g.add_skill(s)
        for pid, sid in people_skills:
            g.link_person_to_skill(pid, sid)
        return g

    def get_skills_subgraph_snapshot(self, skill_ids: Iterable[int]) -> model.Graph:
        g = model.Graph()
        # Capture edges first, to avoid dangling references
        people_skills = self.find_people_skills_of_skills(skill_ids)
        people_ids = set([pid for pid, sid in people_skills])
        for p in self.find_people_by_id(people_ids):
            g.add_person(p)
        for s in self.find_skills_by_id(skill_ids):
            g.add_skill(s)
        for pid, sid in people_skills:
            g.link_person_to_skill(pid, sid)
        return g
