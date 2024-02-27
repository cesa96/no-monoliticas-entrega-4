import propiedades.seedwork.presentacion.api as api
import json
from propiedades.modulos.clientes.aplicacion.servicios import ServicioCliente
from propiedades.modulos.clientes.aplicacion.dto import ClienteDTO
from propiedades.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response
from propiedades.modulos.clientes.aplicacion.mapeadores import MapeadorClienteDTOJson
from propiedades.modulos.clientes.aplicacion.comandos.crear_cliente import CrearCliente
from propiedades.modulos.clientes.aplicacion.queries.obtener_cliente import ObtenerCliente
from propiedades.seedwork.aplicacion.comandos import ejecutar_commando
from propiedades.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('clientes', '/clientes')

@bp.route('/cliente', methods=('POST',))
def clienter():
    try:
        cliente_dict = request.json

        map_cliente = MapeadorClienteDTOJson()
        cliente_dto = map_cliente.externo_a_dto(cliente_dict)

        sr = ServicioCliente()
        dto_final = sr.crear_cliente(cliente_dto)

        return map_cliente.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/cliente-comando', methods=('POST',))
def clienter_asincrona():
    try:
        cliente_dict = request.json

        map_cliente = MapeadorClienteDTOJson()
        cliente_dto = map_cliente.externo_a_dto(cliente_dict)

        comando = CrearCliente(cliente_dto.fecha_creacion, cliente_dto.fecha_actualizacion, cliente_dto.id, cliente_dto.itinerarios)
        
        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        ejecutar_commando(comando)
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/cliente', methods=('GET',))
@bp.route('/cliente/<id>', methods=('GET',))
def dar_cliente(id=None):
    if id:
        sr = ServicioCliente()
        map_cliente = MapeadorClienteDTOJson()
        
        return map_cliente.dto_a_externo(sr.obtener_cliente_por_id(id))
    else:
        return [{'message': 'GET!'}]

@bp.route('/cliente-query', methods=('GET',))
@bp.route('/cliente-query/<id>', methods=('GET',))
def dar_cliente_usando_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerCliente(id))
        map_cliente = MapeadorClienteDTOJson()
        
        return map_cliente.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]