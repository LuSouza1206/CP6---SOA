from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.dtos.reserva_dto import CriarReservaRequest, ReservaResponse
from app.services.reserva_service import ReservaService

router = APIRouter(prefix="/reservas", tags=["Reservas"])
service = ReservaService()


@router.post(
    "",
    response_model=ReservaResponse,
    status_code=201,
    summary="Criar reserva de quadra",
)
def criar_reserva(dto: CriarReservaRequest):
    """
    Cria uma nova reserva para uma quadra esportiva.

    - Valida se a quadra existe
    - Valida conflito de horário
    - Retorna a reserva criada com status 201
    """
    reserva = service.criar_reserva(dto)
    return reserva
