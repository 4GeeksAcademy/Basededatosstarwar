import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Personaje(Base):
    __tablename__ = "personaje"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    color_de_cabello = Column(String(250), nullable=False)
    color_de_ojos = Column(String(250), nullable=False)
    personaje_id_ = relationship("favoritos")

class Planetas(Base):
     
    __tablename__ = "planetas"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    clima = Column(String(250), nullable=False)
    gravedad = Column(String(250), nullable=False)
    planeta_id = relationship("favoritos")

class Usuarios(Base):

    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    user_id_fav = relationship("favoritos")


class Favoritos(Base):
    __tablename__ = "favoritos"
    id = Column(Integer, primary_key=True)
    user_id=  Column(Integer, ForeignKey('usuarios.id'))
    personaje_id= Column(Integer, ForeignKey('personaje.id'))
    planeta_id = Column(Integer, ForeignKey('planetas.id'))



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
