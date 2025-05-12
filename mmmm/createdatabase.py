# create_database.py
import sqlite3

# initialize tables if they don't exist
with sqlite3.connect("journals.db") as db:
    c = db.cursor()
    c.execute("""
      CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        email TEXT UNIQUE,
        username TEXT,
        password TEXT,
        created_at TEXT
      )
    """)
    c.execute("""
      CREATE TABLE IF NOT EXISTS journals (
        id INTEGER PRIMARY KEY,
        owner_id INTEGER,
        title TEXT,
        content TEXT,
        created_at TEXT
      )
    """)
    c.execute("""
      CREATE TABLE IF NOT EXISTS journal_shares (
        id INTEGER PRIMARY KEY,
        journal_id INTEGER,
        user_id INTEGER,
        permission TEXT
      )
    """)
    db.commit()
