#Acá solo debe ir los endpoints de la API
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from utils.db import get_db
from app.database import SessionLocal, engine, Base
from app.models import Country, Procedure, Province
from app.schemas import CountryCreate,CountryResponse, ProcedureCreate, ProcedureResponse, ProvinceCreate, ProvinceResponse
from app.crud import create_country, create_procedure, create_province, get_country_by_code, get_all_countries, get_province_by_code, get_all_provinces, get_procedure_by_code, get_all_procedures


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

@app.get("/countries/{code}", response_model=CountryResponse)
def get_country(code:str, db: Session = Depends(get_db)):
    db_country = get_country_by_code(db, code)
    if db_country is None:
        raise HTTPException(status_code=404, detail="Country doesn't exist")
    return db_country

@app.get("/countries", response_model=list[CountryResponse])
def read_countries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    countries = get_all_countries(db, skip=skip, limit=limit)
    return countries

@app.get("/provinces/{code}", response_model=ProvinceResponse)
def get_province(code:str, db: Session = Depends(get_db)):
    db_province = get_province_by_code(db, code)
    if db_province is None:
        raise HTTPException(status_code=404, detail="Province doesn't exist")
    return db_province

@app.get("/provinces", response_model=list[ProvinceResponse])
def read_provinces(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    provinces = get_all_provinces(db, skip=skip, limit=limit)
    return provinces

@app.get("/procedures/{code_number}", response_model=ProcedureResponse)
def get_procedure(code_number:str, db: Session = Depends(get_db)):
    db_procedure = get_procedure_by_code(db, code_number)
    if db_procedure is None:
        raise HTTPException(status_code=404, detail="Procedure doesn't exist")
    return db_procedure

@app.get("/procedures", response_model=list[ProcedureResponse])
def read_procedures(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    procedures = get_all_procedures(db, skip=skip, limit=limit)
    return procedures

