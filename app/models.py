from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Country(Base):

    __tablename__ = "Country"

    id = Column (Integer, primary_key=True, index=True)
    name = Column (String)
    code = Column (String, unique=True)
    

    provinces = relationship("Province", back_populates="country")

class Province(Base):

    __tablename__ = "Province"

    id = Column (Integer, primary_key=True, index=True)
    name = Column (String)
    code = Column (String, unique=True)
    country_code = Column(String, ForeignKey(Country.code)) 

    country = relationship ("Country", back_populates= "provinces")
    procedures = relationship("Procedure", back_populates="provinces")

class Procedure(Base):

    __tablename__ = "Procedure"

    id = Column(Integer, primary_key=True, index=True)
    code_number = Column(String, unique=True)
    type = Column (String)
    province_code = Column(String, ForeignKey(Province.code))

    provinces = relationship("Province", back_populates="procedures")

