from pydantic import BaseModel
from datetime import datetime


class VotoCreate(BaseModel):
    codigo: str
    candidato_id: int


class VotoResponse(BaseModel):
    success: bool
    message: str


class CandidatoResponse(BaseModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True


class ResultadoResponse(BaseModel):
    candidato: str
    votos: int


class VotoResponseData(BaseModel):
    id: int
    codigo: str
    candidato_id: int
    timestamp: datetime

    class Config:
        orm_mode = True

class ErrorResponse(BaseModel):
    success: bool
    message: str