from propiedades.seedwork.aplicacion.servicios import Servicio
from propiedades.modulos.clientes.dominio.entidades import Reserva
from propiedades.modulos.clientes.dominio.fabricas import Fabricaclientes
from propiedades.modulos.clientes.infraestructura.fabricas import FabricaRepositorio
from propiedades.modulos.clientes.infraestructura.repositorios import RepositorioReservas
from propiedades.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from .mapeadores import MapeadorReserva

from .dto import ReservaDTO

import asyncio

class ServicioReserva(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_clientes: Fabricaclientes = Fabricaclientes()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_clientes(self):
        return self._fabrica_clientes       
    
    def crear_reserva(self, reserva_dto: ReservaDTO) -> ReservaDTO:
        reserva: Reserva = self.fabrica_clientes.crear_objeto(reserva_dto, MapeadorReserva())
        reserva.crear_reserva(reserva)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioReservas.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, reserva)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

        return self.fabrica_clientes.crear_objeto(reserva, MapeadorReserva())

    def obtener_reserva_por_id(self, id) -> ReservaDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioReservas.__class__)
        return self.fabrica_clientes.crear_objeto(repositorio.obtener_por_id(id), MapeadorReserva())

