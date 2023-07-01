from pydantic import BaseModel


class ProcedureCreate(BaseModel):
    code_number: str
    type: str
    province_code:str
    
    class Config:
        orm_mode = True

class ProcedureResponse(ProcedureCreate):
    id:int


class ProvinceCreate(BaseModel):
    name:str
    code:str
    country_code:str


class ProvinceResponse(ProvinceCreate):
    id:int
    #procedures : list[ProcedureResponse]
    
    class Config:
        orm_mode = True


class CountryCreate(BaseModel):
    name:str
    code:str
    

class CountryResponse(CountryCreate):
    id:int
    #provinces: list [] 

    class Config:
        orm_mode = True


