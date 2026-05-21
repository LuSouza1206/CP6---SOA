from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Quadra:
    id: int
    nome: str
    ativa: bool = True


@dataclass
class Reserva:
    id: int
    quadra_id: int
    usuario_id: int
    inicio: datetime
    fim: datetime
    status: str = "confirmada"


# --- Dados em memória (simulando banco) ---

QUADRAS: List[Quadra] = [
    Quadra(id=1, nome="Quadra Society A"),
    Quadra(id=2, nome="Quadra Tênis B"),
    Quadra(id=3, nome="Quadra Beach Vôlei C"),
]

RESERVAS: List[Reserva] = []
_next_id = 1


def next_reserva_id() -> int:
    global _next_id
    id_ = _next_id
    _next_id += 1
    return id_
