from pydantic import BaseModel


class ProcedureCreate(BaseModel):
    code_number: str
    type: str
    province_code:str
    
    class Config:
        orm_mode = True

class ProcedureResponse(ProcedureCreate):
    code_number:str
    type: str
    province_code: str
    id: int

class ProvinceCreate(BaseModel):
    name:str
    code:str
    country_code:str

class ProvinceResponse(ProvinceCreate):
    name:str
    code: str
    country_code: str
    id:int
    #procedures: list(Procedure) = []

    class Config:
        orm_mode = True

class CountryCreate(BaseModel):
    code:str
    name:str

class CountryResponse(CountryCreate):
    name:str
    code:str
    id:int
    #provinces: list(Province) = []

    class Config:
        orm_mode = True


