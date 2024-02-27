"""Objetos valor reusables parte del seedwork del proyecto

En este archivo usted encontrará los objetos valor reusables parte del seedwork del proyecto

"""

from dataclasses import dataclass
from abc import ABC, abstractmethod
from enum import Enum
from .entidades import Locacion
from datetime import datetime

@dataclass(frozen=True)
class ObjetoValor:
    ...

class TipoContacto(Enum):
    MAIL = "Correo"
    PHONE = "Teléfono"

@dataclass(frozen=True)
class Codigo(ABC, ObjetoValor):
    codigo: str

@dataclass(frozen=True)
class Pais(ObjetoValor):
    codigo: Codigo
    nombre: str

@dataclass(frozen=True)
class Ciudad(ObjetoValor):
    pais: Pais
    codigo: Codigo
    nombre: str


@dataclass(frozen=True)
class Direccion(ObjetoValor):
    pais: Pais
    ciudad: Ciudad
    direccion: str

@dataclass(frozen=True)
class DatoContacto(ObjetoValor):
    pais: Pais
    tipoContacto: TipoContacto
    contacto: str

    

