from fastapi import APIRouter
from .main_class import DatabaseForDetails
x=DatabaseForDetails("pcRamDetails","postgres","1234","127.0.0.1","5432","pcram")
router=APIRouter()
@router.get("/{n}")
def show_deatails(n):    
    return x.get_data_from_database(n)