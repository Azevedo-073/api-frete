from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db, criar_tabelas, Rota, Pedagio
from schemas import RotaCreate, RotaOut, CalculoInput, CalculoOutput
from icms import get_aliquota_icms

ADVALOREM_SEGURO_PERCENTUAL = 0.74 / 100  # 0,74%

app = FastAPI(
    title="API de Cálculo de Frete",
    description="Calcula frete rodoviário com base em tarifa por tonelada, pedágios por rota, ad valorem/seguro e ICMS interestadual.",
    version="1.0.0"
)


@app.on_event("startup")
def startup():
    criar_tabelas()


# ─── ROTAS ────────────────────────────────────────────────────────────────────

@app.post("/rotas", response_model=RotaOut, summary="Cadastrar rota")
def cadastrar_rota(rota: RotaCreate, db: Session = Depends(get_db)):
    """Cadastra uma nova rota com tarifa por tonelada e pedágios por estado."""
    existente = db.query(Rota).filter(
        Rota.origem == rota.origem.upper(),
        Rota.destino == rota.destino.upper()
    ).first()
    if existente:
        raise HTTPException(status_code=400, detail="Rota já cadastrada. Use PUT para atualizar.")

    nova_rota = Rota(
        origem=rota.origem.upper(),
        destino=rota.destino.upper(),
        tarifa_por_tonelada=rota.tarifa_por_tonelada
    )
    for p in rota.pedagios:
        nova_rota.pedagios.append(Pedagio(estado=p.estado.upper(), valor=p.valor))

    db.add(nova_rota)
    db.commit()
    db.refresh(nova_rota)
    return nova_rota


@app.get("/rotas", response_model=List[RotaOut], summary="Listar rotas")
def listar_rotas(db: Session = Depends(get_db)):
    """Retorna todas as rotas cadastradas."""
    return db.query(Rota).all()


@app.get("/rotas/{origem}/{destino}", response_model=RotaOut, summary="Buscar rota")
def buscar_rota(origem: str, destino: str, db: Session = Depends(get_db)):
    """Retorna uma rota específica pelo par origem-destino."""
    rota = db.query(Rota).filter(
        Rota.origem == origem.upper(),
        Rota.destino == destino.upper()
    ).first()
    if not rota:
        raise HTTPException(status_code=404, detail="Rota não encontrada.")
    return rota


@app.put("/rotas/{origem}/{destino}", response_model=RotaOut, summary="Atualizar rota")
def atualizar_rota(origem: str, destino: str, dados: RotaCreate, db: Session = Depends(get_db)):
    """Atualiza tarifa e pedágios de uma rota existente."""
    rota = db.query(Rota).filter(
        Rota.origem == origem.upper(),
        Rota.destino == destino.upper()
    ).first()
    if not rota:
        raise HTTPException(status_code=404, detail="Rota não encontrada.")

    rota.tarifa_por_tonelada = dados.tarifa_por_tonelada
    # Remove pedágios antigos e recria
    for p in rota.pedagios:
        db.delete(p)
    rota.pedagios = [Pedagio(estado=p.estado.upper(), valor=p.valor) for p in dados.pedagios]

    db.commit()
    db.refresh(rota)
    return rota


@app.delete("/rotas/{origem}/{destino}", summary="Deletar rota")
def deletar_rota(origem: str, destino: str, db: Session = Depends(get_db)):
    """Remove uma rota e seus pedágios."""
    rota = db.query(Rota).filter(
        Rota.origem == origem.upper(),
        Rota.destino == destino.upper()
    ).first()
    if not rota:
        raise HTTPException(status_code=404, detail="Rota não encontrada.")
    db.delete(rota)
    db.commit()
    return {"mensagem": f"Rota {origem.upper()} → {destino.upper()} removida com sucesso."}


# ─── CÁLCULO ──────────────────────────────────────────────────────────────────

@app.post("/calcular", response_model=CalculoOutput, summary="Calcular frete")
def calcular_frete(dados: CalculoInput, db: Session = Depends(get_db)):
    """
    Calcula o frete completo para uma rota:
    - **Frete base** = peso (ton) × tarifa da rota
    - **Ad valorem + Seguro** = 0,74% do valor da nota fiscal
    - **Pedágio** = soma dos pedágios da rota
    - **Subtotal** = frete base + pedágio + ad valorem/seguro
    - **ICMS** = calculado sobre o subtotal (alíquota interestadual da tabela ANTT)
    - **Total** = subtotal + ICMS
    """
    rota = db.query(Rota).filter(
        Rota.origem == dados.origem.upper(),
        Rota.destino == dados.destino.upper()
    ).first()
    if not rota:
        raise HTTPException(status_code=404, detail=f"Rota {dados.origem.upper()} → {dados.destino.upper()} não cadastrada.")

    # Busca alíquota ICMS
    try:
        aliquota_icms = get_aliquota_icms(dados.origem, dados.destino)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Cálculos
    frete_base = round(dados.peso_toneladas * rota.tarifa_por_tonelada, 2)
    pedagio_total = round(sum(p.valor for p in rota.pedagios), 2)
    advalorem_seguro = round(dados.valor_nota * ADVALOREM_SEGURO_PERCENTUAL, 2)
    subtotal = round(frete_base + pedagio_total + advalorem_seguro, 2)
    icms = round(subtotal * (aliquota_icms / 100), 2)
    total = round(subtotal + icms, 2)

    return CalculoOutput(
        origem=dados.origem.upper(),
        destino=dados.destino.upper(),
        peso_toneladas=dados.peso_toneladas,
        valor_nota=dados.valor_nota,
        frete_base=frete_base,
        pedagio_total=pedagio_total,
        advalorem_seguro=advalorem_seguro,
        subtotal=subtotal,
        aliquota_icms=aliquota_icms,
        icms=icms,
        total=total,
        detalhes_pedagio=rota.pedagios
    )
