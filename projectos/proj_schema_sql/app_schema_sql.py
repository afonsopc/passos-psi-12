import sqlite3
import pathlib

DATABASE = "database.sqlite"

def connect_db():
    return sqlite3.connect(DATABASE)

def run_schema():
    with connect_db() as conn:
        cursor = conn.cursor()

        with open(pathlib.Path(__file__).parent / "schema.sql") as f:
            cursor.executescript(f.read())

        conn.commit()

def insert_users():
    with connect_db() as conn:
        cursor = conn.cursor()

        with open(pathlib.Path(__file__).parent / "insert_users.sql") as f:
            cursor.executescript(f.read())

        conn.commit()

print(pathlib.Path(__file__).parent)

run_schema()
insert_users()