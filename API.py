from webbrowser import get
from fastapi import FastAPI
from database import database_for_details
app = FastAPI()
x=database_for_details("pcRamDetails","postgres","1234","127.0.0.1","5432")
@app.get("/{n}")
def show_deatails(n):    
    return x.get_data_from_database(n)