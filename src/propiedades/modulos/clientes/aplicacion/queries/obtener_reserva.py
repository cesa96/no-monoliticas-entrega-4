from propiedades.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from propiedades.seedwork.aplicacion.queries import ejecutar_query as query
from propiedades.modulos.clientes.infraestructura.repositorios import RepositorioReservas
from dataclasses import dataclass
from .base import ReservaQueryBaseHandler
from propiedades.modulos.clientes.aplicacion.mapeadores import MapeadorReserva
import uuid

@dataclass
class ObtenerReserva(Query):
    id: str

class ObtenerReservaHandler(ReservaQueryBaseHandler):

    def handle(self, query: ObtenerReserva) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioReservas.__class__)
        reserva =  self.fabrica_clientes.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorReserva())
        return QueryResultado(resultado=reserva)

@query.register(ObtenerReserva)
def ejecutar_query_obtener_reserva(query: ObtenerReserva):
    handler = ObtenerReservaHandler()
    return handler.handle(query)