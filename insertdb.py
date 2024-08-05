from backend import pc_details
import time
from database import database_for_details
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
    time.sleep(60)