"""Entidades del dominio de clientes

En este archivo usted encontrará las entidades del dominio de clientes

"""

from __future__ import annotations
from dataclasses import dataclass, field
import datetime
import uuid

import propiedades.modulos.clientes.dominio.objetos_valor as ov
from propiedades.modulos.clientes.dominio.eventos import ReservaCreada, ReservaAprobada, ReservaCancelada, ReservaPagada
from propiedades.seedwork.dominio.entidades import Locacion, AgregacionRaiz, Entidad
from propiedades.seedwork.dominio.objetos_valor import ObjetoValor, Codigo, Direccion, TipoContacto


@dataclass
class Cliente(AgregacionRaiz):
    id_cliente: uuid.UUID = field(hash=True, default=None)
    nombres: ov.EstadoReserva = field(default=ov.EstadoReserva.PENDIENTE)
    apellidos: str
    identificacion: str
    fecha_nacimiento: datetime
    genero: ov.Genero
    direccion: Direccion
    telefono: TipoContacto
    correo: TipoContacto
    tipoCliente: ov.TipoCliente
    sitioWeb: str

    def crear_cliente(self, cliente: Cliente):

        self.id_cliente= cliente.id_cliente
        self.nombres= cliente.nombres
        self.apellidos= cliente.apellidos
        self.identificacion= cliente.identificacion
        self.fecha_nacimiento= cliente.fecha_nacimiento
        self.genero= cliente.genero
        self.direccion= cliente.direccion
        self.telefono= cliente.telefono
        self.correo= cliente.correo
        self.tipoCliente= cliente.tipoCliente
        self.sitioWeb= cliente.sitioWeb

        self.agregar_evento(ReservaCreada(id_reserva=self.id, id_cliente=self.id_cliente, estado=self.estado.name, fecha_creacion=self.fecha_creacion))

