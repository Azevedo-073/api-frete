import os
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Path do DB vem de env var (Railway usa /app/data/frete.db no volume)
# Local, sem env var, continua usando ./frete.db
DB_PATH = os.getenv("DB_PATH", "./frete.db")

# Garante que o diretório existe (pro volume no primeiro boot)
db_dir = os.path.dirname(DB_PATH)
if db_dir:
    os.makedirs(db_dir, exist_ok=True)

DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Rota(Base):
    __tablename__ = "rotas"

    id = Column(Integer, primary_key=True, index=True)
    origem = Column(String, nullable=False)       # ex: "SP"
    destino = Column(String, nullable=False)      # ex: "MG"
    tarifa_por_tonelada = Column(Float, nullable=False)  # R$ por tonelada
    pedagios = relationship("Pedagio", back_populates="rota", cascade="all, delete-orphan")


class Pedagio(Base):
    __tablename__ = "pedagios"

    id = Column(Integer, primary_key=True, index=True)
    rota_id = Column(Integer, ForeignKey("rotas.id"), nullable=False)
    estado = Column(String, nullable=False)       # ex: "SP"
    valor = Column(Float, nullable=False)         # R$ fixo
    rota = relationship("Rota", back_populates="pedagios")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def criar_tabelas():
    Base.metadata.create_all(bind=engine)