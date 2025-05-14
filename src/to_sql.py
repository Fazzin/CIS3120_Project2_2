'''
This function converts a dataframe to a sql database by creating a database.
It iterates through the parameter, dictionaries, to convert every dataframe into a table in the database.
The function prints the table name, and how many rows were saved to the database name.
'''
import sqlite3

def to_sql(rosters, db_file="Sports_Database.db"):
    db_conn = sqlite3.connect('Sports_Database.db') #Creates database 
    for table, df in rosters.items(): #Iterates through the dictionary by table (team category) and df
        #Converts dataframe into a SQL database. The table are used as names.
        df.to_sql(table, db_conn, if_exists="replace", index=False) #If data exists, the data is replaced with the new one. Also removes index.
        print(f'{table}: {len(df)} rows saved to {db_file}')
    db_conn.close() 
