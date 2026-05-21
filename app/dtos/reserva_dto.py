from pydantic import BaseModel, field_validator
from datetime import datetime


class CriarReservaRequest(BaseModel):
    quadra_id: int
    usuario_id: int
    inicio: datetime
    fim: datetime

    @field_validator("fim")
    @classmethod
    def fim_deve_ser_apos_inicio(cls, fim, info):
        inicio = info.data.get("inicio")
        if inicio and fim <= inicio:
            raise ValueError("O horário de fim deve ser posterior ao início")
        return fim


class ReservaResponse(BaseModel):
    id: int
    quadra_id: int
    usuario_id: int
    inicio: datetime
    fim: datetime
    status: str
