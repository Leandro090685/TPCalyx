from sqlalchemy.orm import Session
from app import models, schemas



def create_procedure(db: Session, procedure: schemas.ProcedureCreate):
    db_procedure = models.Procedure(code_number= procedure.code_number, type= procedure.type, province_code = procedure.province_code)
    db.add(db_procedure)
    db.commit()
    db.refresh(db_procedure)
    return db_procedure

def create_country(db:Session, country: schemas.CountryCreate):
    db_country = models.Country(name= country.name, code = country.code)
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
    country = db.query(models.Country).filter(models.Country.code == code).first()
    provinces = db.query(models.Province).filter(models.Province.country_code == code).all()
    list_provinces = []
    cont = 0
    for province in provinces:
        province_data = {
            'id': provinces[cont].__dict__['id'],
            'name': provinces[cont].__dict__['name'],
            'code': provinces[cont].__dict__['code']
        }
        list_provinces.append(province_data)
        cont += 1
    data = {
        'name': country.__dict__['name'],
        'code': country.__dict__['code'],
        'id': country.__dict__['id'],
        'provinces': list_provinces
    }
    return data 

def get_all_countries(db: Session, skip: int = 0, limit: int =100):
    return db.query(models.Country).offset(skip).limit(limit).all()
    
def get_province_by_code(db: Session, code: str):
    province = db.query(models.Province).filter(models.Province.code == code).first()
    procedures = db.query(models.Procedure).filter(models.Procedure.province_code == code).all()
    list_procedures = []
    cont = 0
    for procedure in procedures:
        procedure_data = {
            'id': procedures[cont].__dict__['id'],
            'code_number': procedures[cont].__dict__['code_number'],
            'type': procedures[cont].__dict__['type']
        }
        list_procedures.append(procedure_data)
        cont +=1
    data = {
        'name': province.__dict__['name'],
        'code': province.__dict__['code'],
        'country_code': province.__dict__['country_code'],
        'id': province.__dict__['id'],
        'procedures': list_procedures
    }
    return data
    

def get_all_provinces(db: Session, skip: int = 0, limit: int =100):
    return db.query(models.Province).offset(skip).limit(limit).all()

def get_procedure_by_code(db: Session, code_number: str):
    return db.query(models.Procedure).filter(models.Procedure.code_number == code_number).first()

def get_all_procedures(db: Session, skip: int = 0, limit: int =100):
    return db.query(models.Procedure).offset(skip).limit(limit).all()

def get_quantity_by_code(db:Session, code:str):
    list = db.query(models.Procedure).filter(models.Procedure.province_code == code).all()
    province = db.query(models.Province).filter(models.Province.code == code).first()
    data = {
        "province":province.__dict__['name'].upper(),
        "procedures_quantity": len(list)
    }
    return data

def get_procedures_by_province(db:Session, code:str):
    list = db.query(models.Procedure).filter(models.Procedure.province_code == code).all()
    data_final = []
    for i in list:
        data = {
            'id':i.__dict__['id'],
            'code_number':i.__dict__['code_number'],
            'type': i.__dict__['type']
            }
        data_final.append(data)
    return data_final
   