from pulsar.schema import *
from propiedades.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class ClienteCreadoPayload(Record):
    id_reserva = String()
    id_cliente = String()
    estado = String()
    fecha_creacion = Long()

class EventoClienteCreado(EventoIntegracion):
    data = ClienteCreadoPayload()