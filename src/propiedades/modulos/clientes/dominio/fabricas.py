""" Fábricas para la creación de objetos del dominio de clientes

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de clientes

"""

from .entidades import Cliente, Cliente
from .reglas import MinimoUnItinerario, RutaValida
from .excepciones import TipoObjetoNoExisteEnDominioclientesExcepcion
from propiedades.seedwork.dominio.repositorios import Mapeador, Repositorio
from propiedades.seedwork.dominio.fabricas import Fabrica
from propiedades.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaCliente(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            cliente: Cliente = mapeador.dto_a_entidad(obj)

            #self.validar_regla(MinimoUnItinerario(cliente.itinerarios))
            #[self.validar_regla(RutaValida(ruta)) for itin in cliente.itinerarios for odo in itin.odos for segmento in odo.segmentos for ruta in segmento.legs]
            
            return cliente

@dataclass
class Fabricaclientes(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Cliente.__class__:
            fabrica_cliente = _FabricaCliente()
            return fabrica_cliente.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioclientesExcepcion()

