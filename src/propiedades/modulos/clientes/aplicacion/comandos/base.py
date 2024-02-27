from propiedades.seedwork.aplicacion.comandos import ComandoHandler
from propiedades.modulos.clientes.infraestructura.fabricas import FabricaRepositorio
from propiedades.modulos.clientes.dominio.fabricas import Fabricaclientes

class CrearClienteBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_clientes: Fabricaclientes = Fabricaclientes()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_clientes(self):
        return self._fabrica_clientes    
    