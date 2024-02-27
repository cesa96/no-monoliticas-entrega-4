import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from propiedades.modulos.clientes.infraestructura.schema.v1.eventos import EventoClienteCreado
from propiedades.modulos.clientes.infraestructura.schema.v1.comandos import ComandoCrearCliente
from propiedades.seedwork.infraestructura import utils

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-cliente', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedades-sub-eventos', schema=AvroSchema(EventoClienteCreado))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-cliente', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='propiedades-sub-comandos', schema=AvroSchema(ComandoCrearCliente))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()