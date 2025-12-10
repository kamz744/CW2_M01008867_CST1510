import sqlite3

# Create a single shared database connection
conn = sqlite3.connect("DATA/intelligence_platform.db", check_same_thread=False)

def get_db_connection():
    return conn


