#Acá solo debe ir los endpoints de la API
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from utils.db import get_db
from app.database import SessionLocal, engine, Base
from app.models import Country, Procedure, Province
from app.schemas import CountryCreate,CountryResponse, ProcedureCreate, ProcedureResponse, ProvinceCreate, ProvinceResponse
from app.crud import create_country, create_procedure, create_province, get_country_by_code, get_all_countries, get_province_by_code, get_all_provinces, get_procedure_by_code, get_all_procedures, get_quantity_by_code, get_procedures_by_province, verificate_country_by_code, verificate_procedure_by_code, verificate_province_by_code


app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/procedures", response_model=ProcedureResponse)
def procedure(procedure: ProcedureCreate, db:Session = Depends(get_db)):
    db_procedure = verificate_procedure_by_code(db=db, code=procedure.code_number)
    if db_procedure:
        raise HTTPException(status_code=400, detail="THE CODE NUMBER FOR PROCEDURE ALREADY EXISTS")
    return create_procedure(procedure=procedure, db=db)
    

@app.post("/countries", response_model=CountryResponse)
def country(country: CountryCreate, db:Session = Depends(get_db)):
    db_country = verificate_country_by_code(db=db, code=country.code)
    if db_country:
        raise HTTPException(status_code=400, detail="THE COUNTRY CODE ALREADY EXISTS")
    return create_country(country=country, db=db)
     

@app.post("/provinces", response_model=ProvinceResponse)
def province(province: ProvinceCreate, db:Session = Depends(get_db)):
    db_province = verificate_province_by_code(db=db, code= province.code)
    if db_province:
        raise HTTPException(status_code=400, detail="THE PROVINCE CODE ALREADY EXISTS")
    return create_province(province=province, db=db)

@app.get("/countries/{code}")
def get_country(code:str, db: Session = Depends(get_db)):
    db_country = get_country_by_code(db, code)
    if db_country is False:
        raise HTTPException(status_code=404, detail="Country doesn't exist")
    return db_country

@app.get("/countries", response_model=list[CountryResponse])
def read_countries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    countries = get_all_countries(db, skip=skip, limit=limit)
    return countries

@app.get("/provinces/{code}")
def get_province(code:str, db: Session = Depends(get_db)):
    db_province = get_province_by_code(db, code)
    if db_province is False:
        raise HTTPException(status_code=404, detail="Province doesn't exist")
    return db_province

@app.get("/provinces", response_model=list[ProvinceResponse])
def read_provinces(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    provinces = get_all_provinces(db, skip=skip, limit=limit)
    return provinces

@app.get("/procedures/{code_number}", response_model=ProcedureResponse)
def get_procedure(code_number:str, db: Session = Depends(get_db)):
    db_procedure = get_procedure_by_code(db, code_number)
    if db_procedure is False:
        raise HTTPException(status_code=404, detail="Procedure doesn't exist")
    return db_procedure

@app.get("/procedures", response_model=list[ProcedureResponse])
def read_procedures(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    procedures = get_all_procedures(db, skip=skip, limit=limit)
    return procedures

@app.get("/provinces/{code}/procedures_quantity")
def read_quantity_procedures(code:str, db:Session=Depends(get_db)):
    db_quantity = get_quantity_by_code(db, code)
    if db_quantity is False:
        raise HTTPException(status_code=404, detail="Province doesn't exist")
    return db_quantity

@app.get("/provinces/{code}/procedures")
def read_procedures(code:str, db:Session = Depends(get_db)):
    db_procedures = get_procedures_by_province(db, code)
    if db_procedures is False:
        raise HTTPException(status_code=404, detail="Procedure for this code province doesn't exist")
    return db_procedures
