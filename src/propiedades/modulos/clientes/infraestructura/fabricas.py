""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de clientes

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de clientes

"""

from dataclasses import dataclass, field
from propiedades.seedwork.dominio.fabricas import Fabrica
from propiedades.seedwork.dominio.repositorios import Repositorio
from propiedades.modulos.clientes.dominio.repositorios import RepositorioClientes
from .repositorios import RepositorioClientesSQLite
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioClientes.__class__:
            return RepositorioClientesSQLite()
        else:
            raise ExcepcionFabrica()