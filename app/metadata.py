import pandas as pd
import sqlite3

conn=sqlite3.connect("your.db",check_same_thread=False)

def migrate_dataset_metadata(conn):
    data_metadata  =pd.read_csv("DATA/datasets_metadata.csv") 
    data_metadata.to_sql("datasets_metadata",conn)

def get_all_metadata(conn):
    sql = "SELECT * FROM metadata"
    data = pd.read_sql(sql, conn)
    df= pd.read_sql(sql, conn)
    return data
            


 
   



