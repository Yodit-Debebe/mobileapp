import sqlite3
from fastapi import FastAPI

app = FastAPI()

def get_db():
    conn = sqlite3.connect("journals.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    yield conn
    conn.close()