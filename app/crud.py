from sqlalchemy.orm import Session
from app import models, schemas



def create_procedure(db: Session, procedure: schemas.ProcedureCreate):
    db_procedure = models.Procedure(code_number= procedure.code_number, type= procedure.type, province_code = procedure.province_code)
    db.add(db_procedure)
    db.commit()
    db.refresh(db_procedure)
    return db_procedure

def create_country(db:Session, country: schemas.CountryCreate):
    db_country = models.Country(code = country.code, name= country.name)
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return db_country

def create_province(db:Session, province: schemas.ProvinceCreate):
    db_province = models.Province(name = province.name, code=province.code, country_code = province.country_code)
    db.add(db_province)
    db.commit()
    db.refresh(db_province)
    return db_province