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

def get_country_by_code(db: Session, code: str):
    return db.query(models.Country).filter(models.Country.code == code).first()

def get_all_countries(db: Session, skip: int = 0, limit: int =100):
    return db.query(models.Country).offset(skip).limit(limit).all()
    
def get_province_by_code(db: Session, code: str):
    return db.query(models.Province).filter(models.Province.code == code).first()

def get_all_provinces(db: Session, skip: int = 0, limit: int =100):
    return db.query(models.Province).offset(skip).limit(limit).all()

def get_procedure_by_code(db: Session, code_number: str):
    return db.query(models.Procedure).filter(models.Procedure.code_number == code_number).first()

def get_all_procedures(db: Session, skip: int = 0, limit: int =100):
    return db.query(models.Procedure).offset(skip).limit(limit).all()