#Acá solo debe ir los endpoints de la API
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from utils.db import get_db
from app.database import SessionLocal, engine, Base
from app.models import Country, Procedure, Province
from app.schemas import CountryCreate,CountryResponse, ProcedureCreate, ProcedureResponse, ProvinceCreate, ProvinceResponse
from app.crud import create_country, create_procedure, create_province 


app = FastAPI()

Base.metadata.create_all(bind=engine)



@app.post("/procedures", response_model=ProcedureResponse)
def procedure(procedure: ProcedureCreate, db:Session = Depends(get_db)):
    new_procedure = create_procedure(procedure=procedure, db=db)
    return new_procedure

@app.post("/countries", response_model=CountryResponse)
def country(country: CountryCreate, db:Session = Depends(get_db)):
    new_country = create_country(country=country, db=db)
    return new_country

@app.post("/provinces", response_model=ProvinceResponse)
def province(province: ProvinceCreate, db:Session = Depends(get_db)):
    new_province = create_province(province=province, db=db)
    return new_province


