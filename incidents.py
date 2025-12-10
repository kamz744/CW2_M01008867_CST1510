def migrate_cyber_incidents():
    cyber= data_cyber=pd.read_csv("DATA/cyber_incidents.csv")    
    print(cyber.head)
    conn=sqlite3.connect("DATA/intelligence_platform.db") 
    cyber.to_sql("cyber_incidents",conn,if_exists="append",index=False
    print("all data migrated for cyber_incidents") 

def read_all_cyber_incidents_pandas():
    conn=sqlite3.connec("DATA/intelligence_platform.db")
    querry="SELECT" * FROM cyber_incidents"
    cyber_table=pd.read_sql(querry,conn)
    print(cyber_table.head(5))




    #------- get data---------




    #------migrate data -------


def migrate_cyber_incidents(conn):
    data_cyber = pd.read_csv("DATA/cyber_incidents.csv")
    data_cyber.to_sql("cyber_incidnets", conn)

def get_all_cyber_incidents(conn):
    sql="SELECT"* FROM cyber_incidents"
    data=pd.read_sql(sql,conn)
    conn.close()
    return data


conn=sqlite3.connec("DATA/intelligence_platform.db")
print(get_all_cyber_incidents(conn))
