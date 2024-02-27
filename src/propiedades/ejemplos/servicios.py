from propiedades.modulos.clientes.dominio.objetos_valor import Odo, ParametroBusca
from propiedades.modulos.clientes.dominio.entidades import Itinerario, Proveedor
from propiedades.modulos.clientes.dominio.repositorios import RepositorioProveedores as rp
from propiedades.seedwork.dominio.servicios import Servicio
from propiedades.modulos.clientes.dominio.mixins import FiltradoItinerariosMixin
from propiedades.modulos.clientes.dominio.reglas import MinimoUnAdulto, RutaValida

class ServicioBusqueda(Servicio, FiltradoItinerariosMixin):

    def buscar_itinerarios(self, odos: list[Odo], parametros: ParametroBusca) -> list[Itinerario]:
        itinerarios: list[Itinerario] = list()
        proveedores:list[Proveedor] = rp.obtener_todos()
        
        self.validar_regla(MinimoUnAdulto(parametros.pasajeros))
        [self.validar_regla(RutaValida(ruta)) for odo in odos for segmento in odo.segmentos for ruta in segmento.legs]

        itinerarios.append([proveedor.obtener_itinerarios(odos, parametros) for proveedor in proveedores])

        return self.filtrar_mejores_itinerarios(itinerarios)