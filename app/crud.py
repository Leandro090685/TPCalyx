from sqlalchemy.orm import Session
from app import models, schemas



def create_procedure(db: Session, procedure: schemas.ProcedureCreate):
    """ 
    This function creates a new procedure
    Args:
        db (Session): Database
        procedure (schemas.ProcedureCreate): Information needed to create a new procedure

    Returns:
        _type_: procedure created
    """
    db_procedure = models.Procedure(code_number= procedure.code_number, type= procedure.type, province_code = procedure.province_code)
    db.add(db_procedure)
    db.commit()
    db.refresh(db_procedure)
    return db_procedure


def create_country(db:Session, country: schemas.CountryCreate):
    """
    This function creates a country
    Args:
        db (Session): database
        country (schemas.CountryCreate): Information needed to create a country

    Returns:
        _type_: country created
    """
    db_country = models.Country(name= country.name, code = country.code)
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return db_country

def create_province(db:Session, province: schemas.ProvinceCreate):
    """
    This function is to create a province
    Args:
        db (Session): database
        province (schemas.ProvinceCreate): Information needed to create a province

    Returns:
        _type_: province created
    """
    db_province = models.Province(name = province.name, code=province.code, country_code = province.country_code)
    db.add(db_province)
    db.commit()
    db.refresh(db_province)
    return db_province



def get_country_by_code(db: Session, code: str):
    """
    This function returns the country with the code that was received by parameter

    Args:
        db (Session): database
        code (str): country code

    Returns:
        _type_: the country with that code
    """
    return db.query(models.Country).filter(models.Country.code == code).first()
    
    
    

   
def get_all_countries(db: Session, skip: int = 0, limit: int =100):
    """
    This function returns all the countries in the database
    Args:
        db (Session): database
        skip (int, optional): _description_. Defaults to 0.
        limit (int, optional): _description_. Defaults to 100.

    Returns:
        _type_: All countries
    """
    return db.query(models.Country).offset(skip).limit(limit).all()
    
    
def get_province_by_code(db: Session, code: str):
    """
    This function looks for a province by code
    Args:
        db (Session): database
        code (str): code of the province 

    Returns:
        _type_: the province with that code
    """
    return db.query(models.Province).filter(models.Province.code == code).first()
    
        

def get_all_provinces(db: Session, skip: int = 0, limit: int =100):
    """
    This function searches all the provinces in the database
    Args:
        db (Session): database
        skip (int, optional): _description_. Defaults to 0.
        limit (int, optional): _description_. Defaults to 100.

    Returns:
        _type_: All provinces
    """
    return db.query(models.Province).offset(skip).limit(limit).all()
   

def get_procedure_by_code(db: Session, code_number: str):
    """
    This function looks for a procedure by code
    Args:
        db (Session): database
        code_number (str): procedure code to look for

    Returns:
        _type_: procedure with that code
    """
    return db.query(models.Procedure).filter(models.Procedure.code_number == code_number).first()
    

def get_all_procedures(db: Session, skip: int = 0, limit: int =100):
    """
    This function searches all the procedures that are in the database
    Args:
        db (Session): database
        skip (int, optional): _description_. Defaults to 0.
        limit (int, optional): _description_. Defaults to 100.

    Returns:
        _type_: All procedures
    """
    return db.query(models.Procedure).offset(skip).limit(limit).all()

def get_quantity_by_province_code(db:Session, code:str):
    """
    This function is to know the number of procedures by province

    Args:
        db (Session): database
        code (str): province code

    Returns:
        _type_: Name of the province and number of procedures
    """
    province = db.query(models.Province).filter(models.Province.code == code).first()
    if province is not None:
        data = {"province" : province.name.upper(),
                "procedures_quantity": len(province.procedures),
                }
        return data
    return None


def get_procedures_by_province_code(db:Session, code:str):
    """
    This function is to know the details of the procedures of a province
    Args:
        db (Session): database
        code (str): province code

    Returns:
        _type_: The list of procedures of the province
    """
    return db.query(models.Procedure).filter(models.Procedure.province_code == code).all()
   
   