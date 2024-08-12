import time
from memory_details import pc_details
from main_class import DatabaseForDetails
delay = 60
x=DatabaseForDetails("pcRamDetails","postgres","1234","127.0.0.1","5432","pcram")
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
    time.sleep(delay)