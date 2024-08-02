import psycopg2
import time
from backend import pc_details
#connection to data base function
class database_for_details:
    def __init__(self,database,user,password,host,port) -> None:
        self.database=database
        self.user=user
        self.password=password
        self.host=host
        self.port=port
    def connection(self):
        try:
            connection = psycopg2.connect(database=self.database,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port)
            return connection

        except:
            print("connection to database failed...")
            return None  
    #create table
    def create_table(self):
        try:
            connection=self.connection()
            cur = connection.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS pc_ram_detail(
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
        except:
            print('error in create table')
            connection.rollback()  
    #Inserting information into the database
    def insert_to_database(self,timestamp,total,free,used):
        try:
            connection=self.connection()
            cur = connection.cursor()
            insert_comm = """INSERT INTO pc_ram_detail (timestamp,total,free,used) VALUES (%s,%s,%s,%s);"""
            cur.execute(insert_comm,(timestamp,total,free,used))
            connection.commit()
        except:
            print("error in insert to database")
            connection.rollback() 
    #read information
    def list_of_information(result):
        c=[]
        for record in result:
            cat_dict={}
            cat_dict['timstamp']=record[1]
            cat_dict['total']=record[2]
            cat_dict['free']=record[3]
            cat_dict['used']=record[4]
            c.append(cat_dict)
        return c[::-1]
    def get_data_from_database(self,n):
        try:
            connection=self.connection()
            cur = connection.cursor()
            command = """
                SELECT * FROM pc_ram_detail ORDER BY timestamp DESC LIMIT %s;
                """
            cur.execute(command,(n,))
        
            result = cur.fetchall()
            data_list=self.list_of_information(result)
            connection.close()
            
            print ("get data succeeded...")
            return data_list
        except:
            connection.rollback()
            print("Selecting from database failed...")
        
x=database_for_details("pcRamDetails","postgres","1234","127.0.0.1","5432")
x.create_table()
def information():
    p=pc_details()
    timestamp=str(int(time.time()))
    total=p[0]
    free=p[1]
    used=p[2]
    x.insert_to_database(timestamp,total,free,used)
while True:
    information()
    print("Inserting to database succeeded...")
    time.sleep(1)