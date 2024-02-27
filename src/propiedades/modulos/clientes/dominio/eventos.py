from __future__ import annotations
from dataclasses import dataclass, field
import uuid
from propiedades.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class ClienteCreado(EventoDominio):
    id_cliente: uuid.UUID = None
    fecha_creacion: datetime = None
    
