from pydantic import BaseModel


class ProcedureResponse(BaseModel):
    code_number: str
    type: str
    province_code: str
    id: int

    class Config:
        orm_mode = True


class ProvinceResponse(BaseModel):
    name:str
    code: str
    Country_Code: str
    id:int
    #procedures: list(Procedure) = []

    class Config:
        orm_mode = True

class CountryResponse(BaseModel):
    name:str
    code:str
    id:int
    #provinces: list(Province) = []

    class Config:
        orm_mode = True


