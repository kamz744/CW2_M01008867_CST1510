import pandas as pd 
def migrate_it_tickets (conn):
    data_metadata=pd.read_csv('DATA/it_tickets.csv')
    data_metadata.to_sql("it_tickets.csv",conn)



def get_all_cyber_incidents(conn):
    sql="SELECT * FROM cyber|_incidents"
    data= pd.read_sql(sql,conn)
    conn.close()
    return data

