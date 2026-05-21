from app.dtos.reserva_dto import CriarReservaRequest, ReservaResponse
from app.repositories.reserva_repository import QuadraRepository, ReservaRepository
from app.errors.exceptions import QuadraNaoEncontradaError, ConflitoDeHorarioError


class ReservaService:
    def __init__(self):
        self.quadra_repo = QuadraRepository()
        self.reserva_repo = ReservaRepository()

    def criar_reserva(self, dto: CriarReservaRequest) -> ReservaResponse:
        # Regra 1: quadra deve existir
        quadra = self.quadra_repo.buscar_por_id(dto.quadra_id)
        if not quadra:
            raise QuadraNaoEncontradaError(dto.quadra_id)

        # Regra 2: sem conflito de horário
        conflito = self.reserva_repo.verificar_conflito(dto.quadra_id, dto.inicio, dto.fim)
        if conflito:
            raise ConflitoDeHorarioError(dto.quadra_id, str(dto.inicio), str(dto.fim))

        # Persistir
        reserva = self.reserva_repo.salvar(dto.quadra_id, dto.usuario_id, dto.inicio, dto.fim)

        return ReservaResponse(
            id=reserva.id,
            quadra_id=reserva.quadra_id,
            usuario_id=reserva.usuario_id,
            inicio=reserva.inicio,
            fim=reserva.fim,
            status=reserva.status,
        )
