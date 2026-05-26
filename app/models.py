from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from .database import Base


class Candidato(Base):
    __tablename__ = "candidatos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)

    # Relación con votos
    votos = relationship("Voto", back_populates="candidato")


class Voto(Base):
    __tablename__ = "votos"

    id = Column(Integer, primary_key=True, index=True)

    # Código único para evitar doble voto
    codigo = Column(String(20), unique=True, nullable=False)

    # FK hacia candidatos
    candidato_id = Column(
        Integer,
        ForeignKey("candidatos.id"),
        nullable=False
    )

    # Fecha automática
    timestamp = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    # Relación
    candidato = relationship("Candidato", back_populates="votos")