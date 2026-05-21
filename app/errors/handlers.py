from fastapi import Request
from fastapi.responses import JSONResponse
from app.errors.exceptions import QuadraNaoEncontradaError, ConflitoDeHorarioError


def _error_response(status: int, code: str, message: str) -> JSONResponse:
    return JSONResponse(
        status_code=status,
        content={
            "status": status,
            "error": code,
            "message": message,
        }
    )


async def quadra_nao_encontrada_handler(request: Request, exc: QuadraNaoEncontradaError):
    return _error_response(404, "QUADRA_NAO_ENCONTRADA", str(exc))


async def conflito_horario_handler(request: Request, exc: ConflitoDeHorarioError):
    return _error_response(409, "CONFLITO_DE_HORARIO", str(exc))
