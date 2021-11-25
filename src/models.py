import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(20), nullable=False)
                              

class People(Base):
    __tablename__ = 'people' 
    id = Column(Integer, primary_key=True)
    height = Column(String(50))
    mass = Column(String(50))
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    eye_color = Column(String(50))
    birth_year = Column(String(50))
    gender = Column(String(50))
    name = Column(String(50), nullable=False)
    img_url: Column(String)      

    

class Planet(Base):
    __tablename__ = 'planet'  
    id = Column(Integer, primary_key=True)
    diameter = Column(String(50))
    rotation_period = Column(String(50))
    orbital_period = Column(String(50))
    gravity = Column(String(50))
    population = Column(String(50))
    climate = Column(String(50))
    terrain = Column(String(50))
    surface_water = Column(String(50))
    name = Column(String(50), nullable=False)
    img_url: Column(String)

    
 
class Favorites(Base):
    __tablename__ = 'favorites'  
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User")
    people_id = Column(Integer, ForeignKey('people.id'))
    people = relationship("People")
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship("Planet")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

