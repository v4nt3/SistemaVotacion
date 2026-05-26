from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func

from .database import SessionLocal, engine
from .models import Base, Voto, Candidato
from .schemas import (
    VotoCreate,
    VotoResponse,
    CandidatoResponse,
    ResultadoResponse,
    ErrorResponse
)


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema de Votación de la mascota de la facultad de Ingenieria",
    description="API para gestionar votos y candidatos en un sistema de votación.",
    version="1.0.0",
)
version="1.0.0"
responses={500: {"model": ErrorResponse}}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Bienvenido al Sistema de Votación de la mascota de la facultad de Ingenieria"}


@app.get("/candidatos/", response_model=list[CandidatoResponse])
async def obtener_candidatos(db: Session = Depends(get_db)):
    candidatos = db.query(Candidato).all()
    return candidatos


@app.post("/votar/", response_model=VotoResponse)
async def votar(voto: VotoCreate, db: Session = Depends(get_db)):
    voto_existente = db.query(Voto).filter(Voto.codigo == voto.codigo).first()
    if voto_existente:
        return VotoResponse(success=False, message="Este código ya ha sido utilizado para votar.")
    
    candidato = db.query(Candidato).filter(Candidato.id == voto.candidato_id).first()
    
    if not candidato:
        return VotoResponse(success=False, message="Candidato no encontrado.")
    
    nuevo_voto = Voto(codigo=voto.codigo, candidato_id=voto.candidato_id)
    db.add(nuevo_voto)
    db.commit()

    return {"success": True, "message": "Voto registrado exitosamente."}

@app.get("/resultados/", response_model=list[ResultadoResponse])
async def obtener_resultados(db: Session = Depends(get_db)):
    resultados_db = (
        db.query(
            Candidato.nombre.label("candidato"),
            func.count(Voto.id).label("votos")
        )
        .outerjoin(Voto)
        .group_by(Candidato.id)
        .all()
    )

    return resultados_db