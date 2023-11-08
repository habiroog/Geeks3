import sqlite3
from pathlib import Path
from pprint import pprint


def init_db():
    global db, cursor
    db = sqlite3.connect(Path(__file__).parent.parent / 'db.sqlite3')
    cursor = db.cursor()

def create_table():
    cursor.execute('''
        DROP TABLE IF EXISTS students
        ''')

    cursor.execute('''
        DROP TABLE IF EXISTS categories
        ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        categoryId INTEGER PRIMARY KEY AUTOINCREMENT,
        faculties TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        productsid INTEGER PRIMARY KEY,
        name TEXT,
        year_of_birth DATE,
        faculties TEXT,
        image TEXT,
        categoryId INTEGER,
        FOREIGN KEY (categoryId) REFERENCES categories (categoryId)
    )
    ''')
    db.commit()

def populate_tables():
    cursor.execute('''
    INSERT INTO categories (faculties)
    VALUES ('Лингвистики'),
            ('Филологии'),
            ('Программировании')
    ''')
    cursor.execute('''
        INSERT INTO students (name, year_of_birth, faculties, image, categoryId)
        VALUES ('Sarah', 1999, 'Linguistic', 'image/Sarah.jpg', 1),
               ('Michael', 1997, 'Philology', 'image/Michael.jpg', 2),
               ('Bradley', 2000, 'Programming', 'image/Bradley.jpg', 3),
               ('Brenda', 2003, 'Philology', 'image/Brenda.jpg', 2 ),
               ('Karl', 1998, 'Linguistic', 'image/Karl.jpg', 1 ),
               ('Jennifer', 2001, 'Linguistic', 'image/Jennifer.jpg', 1 ),
               ('Paul', 2003, 'Programming', 'image/Paul.jpg', 3 )
               
    ''')
    db.commit()


def get_all():
    cursor.execute('''SELECT * FROM students''')
    return cursor.fetchall()

def get_by_category(category_id: int):
    cursor.execute(
        f'SELECT * FROM students WHERE categoryId = {category_id}'
    )
    return cursor.fetchall()


if __name__ == '__main__':
    init_db()
    create_table()
    populate_tables()
    # pprint(get_all())
    pprint(get_by_category(2))
