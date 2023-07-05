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

def is_exist_procedure_by_code(db:Session, code:str):
    """This function checks if there is a procedure with that code
    Args:
        db (_type_, optional): Database.
        code (_type_, optional): code to verify

    Returns:
        _type_: Procedure with that code or None
    """
    return db.query(models.Procedure).filter(models.Procedure.code_number == code).first()

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

def is_exist_country_by_code(db: Session, code: str):
    """
    This function checks if there is a country with that code
    Args:
        db (Session): database
        code (str): code to verify

    Returns:
        _type_: country if it exists or none
    """
    return db.query(models.Country).filter(models.Country.code == code).first()

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

def is_exist_province_by_code(db: Session, code: str):
    """
    This function checks if there is a province with that code
    Args:
        db (Session): database
        code (str): code to verify

    Returns:
        _type_: province if it exists or none
    """
    return db.query(models.Province).filter(models.Province.code == code).first()



def add_provinces_country(db: Session, code: str, country:str):
    """
    This function adds the provinces to the corresponding country
    Args:
        db (Session): database
        code (str): code
        country (str): country

    Returns:
        _type_: The country with the list of provinces
    """
    provinces = db.query(models.Province).filter(models.Province.country_code == code).all()
    list_provinces = []
    for province in provinces:
        province_data = {
            'id': province.id, 
            'name': province.name, 
            'code': province.code 
        }
        list_provinces.append(province_data)
    data = {
            'name': country.name,
            'code': country.code, 
            'id': country.id,
            'provinces': list_provinces
        }
    return data

def add_procedures_province(db:Session, code: str, province: str):
    """
    This function adds the procedures to the provinces
    Args:
        db (Session): database
        code (str): code
        province (str): province

    Returns:
        _type_: The provinces with the list of procedures
    """
    procedures = db.query(models.Procedure).filter(models.Procedure.province_code == code).all()
    list_procedures = []
    for procedure in procedures:
        procedure_data = {
            "id" : procedure.id,
            "code_number" : procedure.code_number,
            "type" : procedure.type
        }
        list_procedures.append(procedure_data)
    data = {
        'name': province.name,
        'code': province.code,
        'country_code': province.country_code,
        'id': province.id,
        'procedures': list_procedures 
    }
    return data



def get_country_by_code(db: Session, code: str):
    """
    This function is to search for a country by code
    Args:
        db (Session): database
        code (str): code country to search

    Returns:
        _type_: country with its list of provinces and otherwise returns none
    """
    country = db.query(models.Country).filter(models.Country.code == code).first()
    if country is not None:
        final = add_provinces_country(db=db, code=code, country=country)
        return final
    return None

   
def get_all_countries(db: Session, skip: int = 0, limit: int =100):
    """
    This function returns all the countries in the database
    Args:
        db (Session): database
        skip (int, optional): _description_. Defaults to 0.
        limit (int, optional): _description_. Defaults to 100.

    Returns:
        _type_: All countries with their provinces
    """
    all_countries = db.query(models.Country).offset(skip).limit(limit).all()
    data = []
    for i in all_countries:
        country_final = add_provinces_country(db=db, code = i.code, country = i )
        data.append(country_final)
    return data

    

def get_province_by_code(db: Session, code: str):
    """
    This function looks for a province by code
    Args:
        db (Session): database
        code (str): code of the province 

    Returns:
        _type_: The province with its procedures and if the province does not exist, it returns None
    """
    province = db.query(models.Province).filter(models.Province.code == code).first()
    if province is not None:
        final = add_procedures_province(db=db, code=code, province=province)
        return final
    return None
        

def get_all_provinces(db: Session, skip: int = 0, limit: int =100):
    """
    This function searches all the provinces in the database
    Args:
        db (Session): database
        skip (int, optional): _description_. Defaults to 0.
        limit (int, optional): _description_. Defaults to 100.

    Returns:
        _type_: All provinces with their procedures
    """
    all_provinces = db.query(models.Province).offset(skip).limit(limit).all()
    data = []
    for i in all_provinces:
        province_final = add_procedures_province(db=db, code = i.code, province= i)
        data.append(province_final)
    return data 

def get_procedure_by_code(db: Session, code_number: str):
    """
    This function looks for a procedure by code
    Args:
        db (Session): database
        code_number (str): procedure code to look for

    Returns:
        _type_: process if it exists or None
    """
    procedure = db.query(models.Procedure).filter(models.Procedure.code_number == code_number).first()
    if procedure is not None:
        return procedure
    return None 

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

def get_quantity_by_code(db:Session, code:str):
    """
    This function is to know the number of procedures by province

    Args:
        db (Session): database
        code (str): code province

    Returns:
        _type_: Name of the province and number of procedures
    """
    province = db.query(models.Province).filter(models.Province.code == code).first()
    if province is not None:
        list = db.query(models.Procedure).filter(models.Procedure.province_code == code).all()

        data = {
            "province":province.__dict__['name'].upper(),
            "procedures_quantity": len(list)
        }
        return data
    return None

def get_procedures_by_province(db:Session, code:str):
    """
    This function is to know the details of the procedures of a province
    Args:
        db (Session): database
        code (str): code of province

    Returns:
        _type_: The list of procedures of the province or None
    """
    list = db.query(models.Procedure).filter(models.Procedure.province_code == code).all()
    data_final = []
    if list != []:
        for i in list:
            data = {
                'id':i.id,
                'code_number':i.code_number,
                'type': i.type
                }
            data_final.append(data)
        return data_final
    return None
   