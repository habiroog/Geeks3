import sqlite3
from pathlib import Path

def initdb():
    global db, cursor
    db = sqlite3.connect('db.users')
    cursor = db.cursor()

def createtable():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            categoryId INTEGER PRIMARY KEY AUTOINCREMENT,
            userId TEXT,
            username TEXT
        )
        ''')
    db.commit()


if __name__ == '__main__':
    initdb()
    createtable()

