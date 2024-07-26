from webbrowser import get
from fastapi import FastAPI
import psycopg2
from Database import connect_to_db
app = FastAPI()
#get data from database fo show 
def get_data_from_database(n):
    try:
        connection=connect_to_db("pcRamDetails","postgres","1234","127.0.0.1","5432")
        if connection:
            cur = connection.cursor()
            command = """
            SELECT * FROM pc_ram_details12345 ORDER BY timestamp DESC LIMIT %s;
            """
            cur.execute(command,(n,))
        
            result = cur.fetchall()
            data_list=list_of_information(result)
            connection.close()
            
            print ("get data succeeded...")
            return data_list
        else:
            print("not connecct to database")
    except:
        connection.rollback()
        print("Selecting from database failed...")
        
#
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
#SHow Details
@app.get("/{n}")
def show_deatails(n):    
    return get_data_from_database(n)