from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Country(Base):

    __tablename__ = "Country"

    id = Column (Integer, primary_key=True, index=True)
    code = Column (String, unique=True)
    name = Column (String)

    #provinces = relationship("Province", back_populates="provinces")

class Province(Base):

    __tablename__ = "Province"

    id = Column (Integer, primary_key=True, index=True)
    name = Column (String)
    code = Column (String)
    country_code = Column(String, ForeignKey(Country.id))

    #country = relationship ("Procedure", back_populates= "procedures")

class Procedure(Base):

    __tablename__ = "Procedure"

    id = Column(Integer, primary_key=True, index=True)
    code_number = Column(String, unique=True)
    type = Column (String)
    province_code = Column(String, ForeignKey(Province.id))

    

