# API de Cálculo de Frete Rodoviário

API REST desenvolvida com **FastAPI** e **SQLite** para cálculo de frete rodoviário, contemplando tarifa por tonelada, pedágios por rota, ad valorem/seguro e ICMS interestadual.

## Tecnologias
- Python 3.11+
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

## Instalação

```bash
pip install fastapi uvicorn sqlalchemy
```

## Executar

```bash
uvicorn main:app --reload
```

Acesse a documentação interativa em: http://localhost:8000/docs

## Regras de Negócio

| Componente | Cálculo |
|---|---|
| Frete base | Peso (ton) × Tarifa da rota |
| Pedágio | Soma fixa por estados percorridos |
| Ad valorem + Seguro | 0,74% do valor da nota fiscal |
| Subtotal | Frete base + Pedágio + Ad valorem/Seguro |
| ICMS | Subtotal × alíquota interestadual (tabela ANTT/CONFAZ) |
| **Total** | **Subtotal + ICMS** |

## Endpoints

### Rotas
| Método | Endpoint | Descrição |
|---|---|---|
| POST | `/rotas` | Cadastrar nova rota |
| GET | `/rotas` | Listar todas as rotas |
| GET | `/rotas/{origem}/{destino}` | Buscar rota específica |
| PUT | `/rotas/{origem}/{destino}` | Atualizar rota |
| DELETE | `/rotas/{origem}/{destino}` | Remover rota |

### Cálculo
| Método | Endpoint | Descrição |
|---|---|---|
| POST | `/calcular` | Calcular frete completo |

## Exemplo de Uso

### 1. Cadastrar rota SP → MG

```json
POST /rotas
{
  "origem": "SP",
  "destino": "MG",
  "tarifa_por_tonelada": 350.00,
  "pedagios": [
    {"estado": "SP", "valor": 120.00},
    {"estado": "MG", "valor": 320.00}
  ]
}
```

### 2. Calcular frete

```json
POST /calcular
{
  "origem": "SP",
  "destino": "MG",
  "peso_toneladas": 10.5,
  "valor_nota": 50000.00
}
```

### Resposta
```json
{
  "origem": "SP",
  "destino": "MG",
  "peso_toneladas": 10.5,
  "valor_nota": 50000.0,
  "frete_base": 3675.00,
  "pedagio_total": 440.00,
  "advalorem_seguro": 370.00,
  "subtotal": 4485.00,
  "aliquota_icms": 12.0,
  "icms": 538.20,
  "total": 5023.20,
  "detalhes_pedagio": [
    {"id": 1, "estado": "SP", "valor": 120.00},
    {"id": 2, "estado": "MG", "valor": 320.00}
  ]
}
```
