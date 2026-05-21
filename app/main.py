from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.controllers.reserva_controller import router as reserva_router
from app.errors.handlers import quadra_nao_encontrada_handler, conflito_horario_handler
from app.errors.exceptions import QuadraNaoEncontradaError, ConflitoDeHorarioError

app = FastAPI(
    title="QuadraFast API",
    version="1.0.0",
    docs_url="/v1/docs",
)

# Registro de rotas versionadas
app.include_router(reserva_router, prefix="/v1")

# Handlers de erro globais
app.add_exception_handler(QuadraNaoEncontradaError, quadra_nao_encontrada_handler)
app.add_exception_handler(ConflitoDeHorarioError, conflito_horario_handler)
