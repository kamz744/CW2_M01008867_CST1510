import sqlite3
import pandas as pd



def create_user_table():

    curr = conn.cursor()
    sql = """ CREATE TABLE IF NOT EXISTS users ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    username TEXT NOT NULL UNIQUE, 
    password_hash TEXT NOT NULL ) """


    curr.execute(sql)
    conn.commit()



def add_user(conn,name,hash_password):
    curr = conn.cursor() 
    sql= """insert into users (username,password_hash) Values(?,?)"""
    param=("alice","hashed_password_123")
    curr.execute(sql,param)
    conn.commit()

def migrate_users():
    with open("data/user.txt")as f:
        users=f.readline()
    
    for user in users:
        name,hash=user.strip().split(",")
        add_user(conn,name,hash)
                 
def get_all_users():
    curr=conn.cursor()
    sql="SELECT * FROM users"
    curr.execute(sql)
    users=curr.fetchall()

    conn.close()
    return users



def migrate_cyber_incidents():
    cyber=pd.read("data/cyber_incidents.csv")
    #print(cyber.head(5))
    conn=sqlite3.connect("Data/intelligence_platform.db")
    cyber.to_sql("cyber_incidents",conn,if_exists="append",index=false)
    print("migrated all cyber_incidents")

    def read_all_cyber_incidents_pandas():
        conn=sqlite3.connect("Data/intelligence_platform.db")
        query="select * from cyber_incidents"
        cyber_table=pd.read_sql(query,conn)
        print(cyber_table.head(5))  

def migrate_cyber_incidents(conn):
    data_cyber=pd.read_csv("DATA/cyber_incidents.csv")
    data_cyber.to_sql("cyber_incidents",conn)

def migrate_datasets_metadata(conn):   
    data_metadata=pd.read_csv("DATA/datasets_metadata.csv")
    data_metadata.to_sql("datasets_metadata",conn)
    


def migrate_datasets_metadata(conn):   
    data_metadata=pd.read_csv("DATA/it_tickets.csv")
    data_metadata.to_sql("it_tickets",conn)


conn=sqlite3.connect("DATA/intelligence_platform.db")  

def get_all_c
sql=SELECT * FROM cyber_incidents"
data=pd.read_sql(sql,conn")
conn.close()

print(data.head())


from app.meta