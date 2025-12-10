import sqlite3

conn=sqlite3.connect("DATA/intelligent_platform,db")

def create_user_table(conn):
    curr=conn.cursor()


sql = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL
);
"""

