class QuadraNaoEncontradaError(Exception):
    def __init__(self, quadra_id: int):
        self.quadra_id = quadra_id
        super().__init__(f"Quadra {quadra_id} não encontrada")


class ConflitoDeHorarioError(Exception):
    def __init__(self, quadra_id: int, inicio: str, fim: str):
        self.quadra_id = quadra_id
        self.inicio = inicio
        self.fim = fim
        super().__init__(f"Conflito de horário na quadra {quadra_id}: {inicio} → {fim}")
