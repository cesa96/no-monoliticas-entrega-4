from propiedades.modulos.clientes.dominio.eventos import ClienteCreada, ClienteCancelada, ClienteAprobada, ClientePagada
from propiedades.seedwork.aplicacion.handlers import Handler
from propiedades.modulos.clientes.infraestructura.despachadores import Despachador

class HandlerClienteIntegracion(Handler):

    @staticmethod
    def handle_cliente_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-cliente')

    @staticmethod
    def handle_cliente_cancelada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-cliente')

    @staticmethod
    def handle_cliente_aprobada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-cliente')

    @staticmethod
    def handle_cliente_pagada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-cliente')


    