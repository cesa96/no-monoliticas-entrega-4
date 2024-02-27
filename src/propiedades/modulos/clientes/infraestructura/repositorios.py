""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de clientes

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de clientes

"""

from propiedades.config.db import db
from propiedades.modulos.clientes.dominio.repositorios import RepositorioClientes, RepositorioProveedores
from propiedades.modulos.clientes.dominio.objetos_valor import NombreAero, Odo, Leg, Segmento, Itinerario, CodigoIATA
from propiedades.modulos.clientes.dominio.entidades import Proveedor, Aeropuerto, Cliente
from propiedades.modulos.clientes.dominio.fabricas import Fabricaclientes
from .dto import Cliente as ClienteDTO
from .mapeadores import MapeadorCliente
from uuid import UUID



class RepositorioClientesSQLite(RepositorioClientes):

    def __init__(self):
        self._fabrica_clientes: Fabricaclientes = Fabricaclientes()

    @property
    def fabrica_clientes(self):
        return self._fabrica_clientes

    def obtener_por_id(self, id: UUID) -> Cliente:
        cliente_dto = db.session.query(ClienteDTO).filter_by(id=str(id)).one()
        return self.fabrica_clientes.crear_objeto(cliente_dto, MapeadorCliente())

    def obtener_todos(self) -> list[Cliente]:
        # TODO
        raise NotImplementedError

    def agregar(self, cliente: Cliente):
        cliente_dto = self.fabrica_clientes.crear_objeto(cliente, MapeadorCliente())
        db.session.add(cliente_dto)

    def actualizar(self, cliente: Cliente):
        # TODO
        raise NotImplementedError

    def eliminar(self, cliente_id: UUID):
        # TODO
        raise NotImplementedError