""" Mapeadores para la capa de infrastructura del dominio de clientes

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from propiedades.seedwork.dominio.repositorios import Mapeador
from propiedades.modulos.clientes.dominio.objetos_valor import Genero, TipoCliente
from propiedades.modulos.clientes.dominio.entidades import  Cliente
from .dto import Cliente as ClienteDTO
from propiedades.seedwork.dominio.objetos_valor import DatoContacto, Direccion, TipoContacto

class MapeadorCliente(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'


    def entidad_a_dto(self, entidad: Cliente) -> ClienteDTO:
        
        cliente_dto = ClienteDTO()
        cliente_dto.fecha_creacion = entidad.fecha_creacion
        cliente_dto.fecha_actualizacion = entidad.fecha_actualizacion
        cliente_dto.id = str(entidad.id_cliente)


        cliente_dto.nombres = entidad.nombres
        cliente_dto.apellidos = entidad.apellidos
        cliente_dto.identificacion = entidad.identificacion
        cliente_dto.fecha_nacimiento = entidad.fecha_nacimiento
        cliente_dto.genero = entidad.genero
        cliente_dto.direccion = entidad.direccion.direccion
        cliente_dto.telefono= entidad.telefono.value
        cliente_dto.correo= entidad.correo.value
        cliente_dto.tipoCliente = entidad.tipoCliente
        cliente_dto.sitioWeb =entidad.sitioWeb

        return cliente_dto

    def dto_a_entidad(self, dto: ClienteDTO) -> Cliente:
        direccion  = Direccion(None, None, dto.direccion)
        telefono = DatoContacto(None, TipoContacto.PHONE, dto.telefono)
        correo = DatoContacto(None, TipoContacto.MAIL, dto.correo)
        cliente = Cliente(dto.id, dto.fecha_creacion, dto.fecha_actualizacion, dto.nombres, dto.apellidos, dto.identificacion, dto.fecha_nacimiento, dto.genero, direccion, telefono, correo, dto.tipoCliente, dto.sitioWeb)

        
        return cliente