import psycopg2
import time
#connection to data base function
class DatabaseForDetails:
    def __init__(self,database,user,password,host,port,table_name) -> None:
        self.database=database
        self.user=user
        self.password=password
        self.host=host
        self.port=port
        self.table_name=table_name
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
            cur.execute(f"""
                CREATE TABLE IF NOT EXISTS {self.table_name}(
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
            insert_comm = f"""INSERT INTO {self.table_name}(timestamp,total,free,used) VALUES (%s,%s,%s,%s);"""
            cur.execute(insert_comm,(timestamp,total,free,used))
            connection.commit()
        except:
            print("error in insert to database")
            connection.rollback() 
    #read information
    def list_of_information(self,result):
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
            command = f"""
                SELECT * FROM {self.table_name} ORDER BY timestamp DESC LIMIT %s;
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