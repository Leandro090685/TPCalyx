#Acá solo debe ir los endpoints de la API
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from utils.db import get_db
from app.database import engine, Base 
from app import crud
from app import schemas

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/procedures", response_model=schemas.ProcedureResponse)
def procedure(procedure: schemas.ProcedureCreate, db:Session = Depends(get_db)):
    db_procedure = crud.get_procedure_by_code(db=db, code_number=procedure.code_number)
    if db_procedure:
        raise HTTPException(status_code=400, detail="THE CODE NUMBER FOR PROCEDURE ALREADY EXISTS")
    db_province = crud.get_province_by_code(db=db, code = procedure.province_code)
    if db_province is None:
        raise HTTPException(status_code=400, detail="THE PROVINCE CODE DOESN'T EXISTS")
    return crud.create_procedure(procedure=procedure, db=db)
    

@app.post("/countries", response_model=schemas.CountryResponse)
def country(country: schemas.CountryCreate, db:Session = Depends(get_db)):
    db_country = crud.get_country_by_code(db=db, code=country.code)
    if db_country:
        raise HTTPException(status_code=400, detail="THE COUNTRY CODE ALREADY EXISTS")
    return crud.create_country(country=country, db=db)
     

@app.post("/provinces", response_model=schemas.ProvinceResponse)
def province(province: schemas.ProvinceCreate, db:Session = Depends(get_db)):
    db_province = crud.get_province_by_code(db=db, code= province.code)
    if db_province:
        raise HTTPException(status_code=400, detail="THE PROVINCE CODE ALREADY EXISTS")
    db_country = crud.get_country_by_code(db=db, code = province.country_code)
    if db_country is None:
        raise HTTPException(status_code=400, detail="THE COUNTRY CODE DOESN'T EXISTS")
    return crud.create_province(province=province, db=db)


@app.get("/countries/{code}", response_model= schemas.CountryResponse)
def get_country(code:str, db: Session = Depends(get_db)):
    db_country = crud.get_country_by_code(db, code)
    if db_country is None:
        raise HTTPException(status_code=404, detail="Country doesn't exist")
    return db_country

@app.get("/countries", response_model=list[schemas.CountryResponse])
def read_countries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    countries = crud.get_all_countries(db, skip=skip, limit=limit)
    return countries

@app.get("/provinces/{code}", response_model=schemas.ProvinceResponse)
def get_province(code:str, db: Session = Depends(get_db)):
    db_province = crud.get_province_by_code(db, code)
    if db_province is None:
        raise HTTPException(status_code=404, detail= "Province doesn't exist")
    return db_province

@app.get("/provinces", response_model=list[schemas.ProvinceResponse])
def read_provinces(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    provinces = crud.get_all_provinces(db, skip=skip, limit=limit)
    return provinces

@app.get("/procedures/{code_number}", response_model=schemas.ProcedureResponse)
def get_procedure(code_number:str, db: Session = Depends(get_db)):
    db_procedure = crud.get_procedure_by_code(db, code_number)
    if db_procedure is None:
        raise HTTPException(status_code=404, detail="Procedure doesn't exist")
    return db_procedure

@app.get("/procedures", response_model=list[schemas.ProcedureResponse])
def read_procedures(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    procedures = crud.get_all_procedures(db, skip=skip, limit=limit)
    return procedures

@app.get("/provinces/{code}/procedures_quantity", response_model=schemas.ProcedureQuantityProvince)
def read_quantity_procedures(code:str, db:Session=Depends(get_db)):
    db_quantity = crud.get_quantity_by_province_code(db, code)
    if db_quantity is None:
        raise HTTPException(status_code=404, detail="Province doesn't exist")
    return db_quantity

@app.get("/provinces/{code}/procedures", response_model=list[schemas.ProcedureResponseProvince])
def read_procedures(code:str, db:Session = Depends(get_db)):
    db_procedures = crud.get_procedures_by_province_code(db, code)
    if len(db_procedures) == 0:
        raise HTTPException(status_code=404, detail="Procedure for this code province doesn't exist")
    return db_procedures
