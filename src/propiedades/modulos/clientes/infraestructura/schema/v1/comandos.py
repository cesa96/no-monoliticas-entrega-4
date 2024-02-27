from pulsar.schema import *
from dataclasses import dataclass, field
from propiedades.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearClientePayload(ComandoIntegracion):
    id_usuario = String()
    # TODO Cree los records para itinerarios

class ComandoCrearCliente(ComandoIntegracion):
    data = ComandoCrearClientePayload()