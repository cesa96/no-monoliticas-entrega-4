from pydispatch import dispatcher

from .handlers import HandlerClienteIntegracion

from propiedades.modulos.clientes.dominio.eventos import ClienteCreada, ClienteCancelada, ClienteAprobada, ClientePagada

dispatcher.connect(HandlerClienteIntegracion.handle_cliente_creada, signal=f'{ClienteCreada.__name__}Integracion')
dispatcher.connect(HandlerClienteIntegracion.handle_cliente_cancelada, signal=f'{ClienteCancelada.__name__}Integracion')
dispatcher.connect(HandlerClienteIntegracion.handle_cliente_pagada, signal=f'{ClientePagada.__name__}Integracion')
dispatcher.connect(HandlerClienteIntegracion.handle_cliente_aprobada, signal=f'{ClienteAprobada.__name__}Integracion')