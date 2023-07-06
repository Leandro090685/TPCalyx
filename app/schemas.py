from pydantic import BaseModel

class ProcedureBase(BaseModel):
    code_number:str
    type:str

    class Config:
        orm_mode = True

class ProcedureCreate(ProcedureBase):
   province_code:str
    
   
class ProcedureResponse(ProcedureCreate):
    id:int

class ProcedureResponseProvince(BaseModel):
    id:int
    code_number:str
    type:str

    class Config:
        orm_mode = True

class ProcedureQuantityProvince(BaseModel):
    province:str
    procedures_quantity: int

    class Config:
        orm_mode = True

    
#---------------------------------------------------------------#

class ProvinceBase(BaseModel):
    name: str
    code: str

    class Config:
        orm_mode = True

class ProvinceCreate(ProvinceBase):
    country_code:str


class ProvinceResponse(ProvinceCreate):
    id:int
    procedures: list[ProcedureResponseProvince] = []
    
    
class ProvinceResponseCountry(ProvinceBase):
    id:int

 
#---------------------------------------------------------------------#

class CountryBase(BaseModel):
    name: str
    code: str

    class Config:
        orm_mode = True

class CountryCreate(CountryBase):
    pass

   
class CountryResponse(CountryBase):
    id: int
    provinces:list[ProvinceResponseCountry] = [] 

    


