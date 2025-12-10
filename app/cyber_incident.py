import pandas as pd

def get_all_cyber_incidents(conn):
    sql = "SELECT * FROM cyber_incidents"
    data = pd.read_sql(sql, conn)
    return data
