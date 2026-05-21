from typing import Optional, List
from datetime import datetime
from app.models.models import Quadra, Reserva, QUADRAS, RESERVAS, next_reserva_id


class QuadraRepository:
    def buscar_por_id(self, quadra_id: int) -> Optional[Quadra]:
        return next((q for q in QUADRAS if q.id == quadra_id), None)


class ReservaRepository:
    def verificar_conflito(self, quadra_id: int, inicio: datetime, fim: datetime) -> bool:
        for r in RESERVAS:
            if r.quadra_id != quadra_id:
                continue
            # Sobreposição de intervalos: A.inicio < B.fim AND A.fim > B.inicio
            if r.inicio < fim and r.fim > inicio:
                return True
        return False

    def salvar(self, quadra_id: int, usuario_id: int, inicio: datetime, fim: datetime) -> Reserva:
        reserva = Reserva(
            id=next_reserva_id(),
            quadra_id=quadra_id,
            usuario_id=usuario_id,
            inicio=inicio,
            fim=fim,
            status="confirmada",
        )
        RESERVAS.append(reserva)
        return reserva
