from pydantic import BaseModel


class Procedure(BaseModel):
    code_number: str
    type: str
    province_code: str
    id: int

    class Config:
        orm_mode = True


class Province(BaseModel):
    name:str
    code: str
    country_code: str
    id:int
    procedures: list(Procedure) = []

    class Config:
        orm_mode = True

class Country(BaseModel):
    name:str
    code:str
    id:int
    provinces: list(Province) = []

    class Config:
        orm_mode = True

class Procedure(BaseModel):
    pass