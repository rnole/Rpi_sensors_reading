from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class Sensors_data(Base):

    __tablename__ = 'Sensors_data'
    
    id = Column(Integer, primary_key=True)
    sensor_id   = Column(Integer)
    timestamp   = Column(String)
    co          = Column(Float)
    o3          = Column(Float)
    no2         = Column(Float)
    so2         = Column(Float)
    co2         = Column(Float)
    temperature = Column(Float)
    humidity    = Column(Float)
    uv          = Column(Float)
    luminosity  = Column(Float)
    pm1         = Column(Float)
    pm25        = Column(Float)
    pm10        = Column(Float)
    noise       = Column(Float)
  
    








    












