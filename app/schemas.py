from pydantic import BaseModel


class ProcedureCreate(BaseModel):
    code_number: str
    type: str
    province_code:str
    
   
class ProcedureResponse(ProcedureCreate):
    id:int

    class Config:
        orm_mode = True

class ProcedureResponseCode(BaseModel):
    id: int
    code_number:str
    type:str

#---------------------------------------------------------------#

class ProvinceCreate(BaseModel):
    name:str
    code:str
    country_code:str


class ProvinceResponse(BaseModel):
    id:int
    name:str
    code:str
    
    class Config:
        orm_mode = True

class ProvinceProceduresResponse(ProvinceCreate):
    id:int
    procedures:list[ProcedureResponseCode] = []

#---------------------------------------------------------------------#

class CountryCreate(BaseModel):
    name:str
    code:str
    

class CountryResponse(CountryCreate):
    id:int
    provinces:list[ProvinceResponse] = [] 

    class Config:
        orm_mode = True


