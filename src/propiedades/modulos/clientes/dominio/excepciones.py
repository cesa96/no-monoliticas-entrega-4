""" Excepciones del dominio de clientes

En este archivo usted encontrará los Excepciones relacionadas
al dominio de clientes

"""

from propiedades.seedwork.dominio.excepciones import ExcepcionFabrica

class TipoObjetoNoExisteEnDominioclientesExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una fábrica para el tipo solicitado en el módulo de clientes'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)