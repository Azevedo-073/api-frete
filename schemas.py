from pydantic import BaseModel, Field
from typing import List


# --- Pedágio ---

class PedagioBase(BaseModel):
    estado: str = Field(..., example="SP")
    valor: float = Field(..., example=120.00)

class PedagioCreate(PedagioBase):
    pass

class PedagioOut(PedagioBase):
    id: int
    class Config:
        from_attributes = True


# --- Rota ---

class RotaCreate(BaseModel):
    origem: str = Field(..., example="SP")
    destino: str = Field(..., example="MG")
    tarifa_por_tonelada: float = Field(..., example=350.00)
    pedagios: List[PedagioCreate] = Field(default=[], example=[
        {"estado": "SP", "valor": 120.00},
        {"estado": "MG", "valor": 320.00}
    ])

class RotaOut(BaseModel):
    id: int
    origem: str
    destino: str
    tarifa_por_tonelada: float
    pedagios: List[PedagioOut]
    class Config:
        from_attributes = True


# --- Cálculo ---

class CalculoInput(BaseModel):
    origem: str = Field(..., example="SP")
    destino: str = Field(..., example="MG")
    peso_toneladas: float = Field(..., gt=0, example=10.5)
    valor_nota: float = Field(..., gt=0, example=50000.00)

class CalculoOutput(BaseModel):
    origem: str
    destino: str
    peso_toneladas: float
    valor_nota: float
    frete_base: float
    pedagio_total: float
    advalorem_seguro: float
    subtotal: float
    aliquota_icms: float
    icms: float
    total: float
    detalhes_pedagio: List[PedagioOut]
