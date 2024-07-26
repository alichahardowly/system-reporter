import psycopg2
import time
from Backend import pc_details
#connection to data base function
def connect_to_db(Database,User,Password,Host,Port):
    try:
        connection = psycopg2.connect(database=Database,
            user=User,
            password=Password,
            host=Host,
            port=Port)
        return connection
    except:
        print("connection to database failed...")
        return None
#create table
def create_table(tablename):
    try:
        connection=connect_to_db("pcRamDetails","postgres","1234","127.0.0.1","5432")
        if connection:
        
            cur = connection.cursor()
        
            cur.execute("""
                CREATE TABLE IF NOT EXISTS {tablename}(
                id SERIAL PRIMARY KEY,
                timestamp VARCHAR (50) NOT NULL,
                total VARCHAR (50) NOT NULL,
                free VARCHAR (50) NOT NULL,
                used VARCHAR (50) NOT NULL
            );
            """)
            connection.commit()
            connection.close()
            print ("create database succeeded...")
        else:
            print("not connecct to database")
    except:
        connection.rollback()
#Inserting information into the database
def insert_to_database(timestamp,total,free,used):
    try:
        connection=connect_to_db("pcRamDetails","postgres","1234","127.0.0.1","5432")
        if connection:
            cur = connection.cursor()
            insert_comm = """INSERT INTO pc_ram_details12345 (timestamp,total,free,used) VALUES (%s,%s,%s,%s);"""
            cur.execute(insert_comm,(timestamp,total,free,used))
            connection.commit()
        else:
            print("not connecct to database")
    except:
        connection.rollback()
#get information
def information():
    timestamp=str(int(time.time()))
    total=pc_details().total
    free=pc_details().free
    used=pc_details().used
    insert_to_database(timestamp,total,free,used)  
if __name__ == "__main__":
    #while loop
    while True:
        information()
        print("Inserting to database succeeded...")
        time.sleep(60) 