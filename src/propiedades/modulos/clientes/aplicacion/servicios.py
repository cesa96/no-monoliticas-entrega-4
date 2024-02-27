from propiedades.seedwork.aplicacion.servicios import Servicio
from propiedades.modulos.clientes.dominio.entidades import Cliente
from propiedades.modulos.clientes.dominio.fabricas import Fabricaclientes
from propiedades.modulos.clientes.infraestructura.fabricas import FabricaRepositorio
from propiedades.modulos.clientes.infraestructura.repositorios import RepositorioClientes
from propiedades.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from .mapeadores import MapeadorCliente

from .dto import ClienteDTO

import asyncio

class ServicioCliente(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_clientes: Fabricaclientes = Fabricaclientes()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_clientes(self):
        return self._fabrica_clientes       
    
    def crear_cliente(self, cliente_dto: ClienteDTO) -> ClienteDTO:
        cliente: Cliente = self.fabrica_clientes.crear_objeto(cliente_dto, MapeadorCliente())
        cliente.crear_cliente(cliente)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioClientes.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, cliente)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

        return self.fabrica_clientes.crear_objeto(cliente, MapeadorCliente())

    def obtener_cliente_por_id(self, id) -> ClienteDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioClientes.__class__)
        return self.fabrica_clientes.crear_objeto(repositorio.obtener_por_id(id), MapeadorCliente())

