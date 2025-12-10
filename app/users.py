import bcrypt
import pandas as pd





def add_user(conn, name, hash):
    curr = conn.cursor()
    sql = 'INSERT into users (user_name, hash_paswsword) VALUES (?,?)'
    parameters = (name, hash)
    curr.execute(sql, parameters)
    conn.commit()

def get_user(conn, name):
    curr = conn.cursor()
    sql = 'SELECT * FROM users WHERE user_name = ?'
    parameters = (name,)
    curr.execute(sql, parameters)
    return curr.fetchone()