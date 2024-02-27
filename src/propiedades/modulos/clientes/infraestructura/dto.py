"""DTOs para la capa de infrastructura del dominio de clientes

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de clientes

"""

from propiedades.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

class Cliente(db.Model):
    __tablename__ = "clientes"
    id = db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    nombres = db.Column(db.String, nullable=True)
    apellidos = db.Column(db.String, nullable=True)
    identificacion = db.Column(db.String, nullable=True)
    fecha_nacimiento = db.Column(db.DateTime, nullable=True)
    genero = db.Column(db.String, nullable=True)
    direccion = db.Column(db.String, nullable=True)
    telefono  = db.Column(db.String, nullable=True)
    correo  = db.Column(db.String, nullable=True)
    tipoCliente = db.Column(db.String, nullable=True)
    sitioWeb = db.Column(db.String, nullable=True)

