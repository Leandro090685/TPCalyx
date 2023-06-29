#Acá solo debe ir los endpoints de la API
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from utils.db import get_db
from app.database import SessionLocal, engine
from app.models import Country, Procedure, Province
from app.schemas import CountryResponse, ProcedureResponse, ProvinceResponse
from app.crud import get_provinces
app = FastAPI()

@app.get("/provinces")
def province_by_id(db: Session = Depends(get_db)):
    db_province = get_provinces(db = db)
    if db_province is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_province 
