import sqlite3
from os.path import exists as file_exists

class SqliteRepository(object):
    """
    Graph holding a consistent view of skills, people, and their
    relationships. Implemented with SQLite3.
    """

    __DB_INIT = [
        '''
        CREATE TABLE skills (
            skill_id INTEGER PRIMARY KEY,
            skill_name TEXT NOT NULL
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
        'CREATE UNIQUE INDEX idx_people_id ON people(person_id);',
        'CREATE UNIQUE INDEX idx_people_skills ON people_skills(person_id, skill_id);',
    ]

    __CREATE_IF_NOT_EXIST_PERSON = 'INSERT OR IGNORE INTO people VALUES (?, ?);'
    __CREATE_IF_NOT_EXIST_SKILL = 'INSERT OR IGNORE INTO skills VALUES (?, ?);'
    __ADD_PERSON_SKILL = 'INSERT OR IGNORE INTO people_skills VALUES (?, ?);'
    __REMOVE_PERSON_SKILL = 'DELETE FROM people_skills WHERE person_id = ? AND skill_id = ?;'
    __SKILL_EXISTS = 'SELECT EXISTS(SELECT 1 FROM skills WHERE skill_id = ?);'
    __SELECT_ALL_SKILLS = "SELECT skill_id, skill_name FROM skills;"
    __SELECT_ALL_PEOPLE = "SELECT person_id, person_name FROM people;"
    __SELECT_ALL_PEOPLE_SKILLS = "SELECT person_id, skill_id FROM people_skills;"

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

    def print_stats(self):
        print("--")
        print("Graph stats: ")
        print("  🙂 People:      {}".format(len(self.get_people())))
        print("  🔨 Skills:      {}".format(len(self.get_skills())))
        print("  ↔️  Connections: {}".format(len(self.get_people_skills())))
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

    def get_skills(self):
        return self.db.execute(SqliteRepository.__SELECT_ALL_SKILLS).fetchall()

    def get_people(self):
        return self.db.execute(SqliteRepository.__SELECT_ALL_PEOPLE).fetchall()

    def get_people_skills(self):
        return self.db.execute(SqliteRepository.__SELECT_ALL_PEOPLE_SKILLS).fetchall()
