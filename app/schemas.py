from pydantic import BaseModel


class ProcedureCreate(BaseModel):
    code_number: str
    type: str
    province_code:str
    
   
class ProcedureResponse(ProcedureCreate):
    id:int

    class Config:
        orm_mode = True

#---------------------------------------------------------------#

class ProvinceCreate(BaseModel):
    name:str
    code:str
    country_code:str


class ProvinceResponse(ProvinceCreate):
    id:int
    
    
    class Config:
        orm_mode = True

#---------------------------------------------------------------------#

class CountryCreate(BaseModel):
    name:str
    code:str
    

class CountryResponse(CountryCreate):
    id:int
     

    class Config:
        orm_mode = True


