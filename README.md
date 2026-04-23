# 🚚 Freight Calculation API

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-D71F00)](https://www.sqlalchemy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#license)
[![Status](https://img.shields.io/badge/status-active-success)]()
[![Deploy on Railway](https://img.shields.io/badge/deploy-Railway-0B0D0E?logo=railway&logoColor=white)](https://web-production-39b08.up.railway.app/docs)

REST API for **road freight cost calculation** based on real Brazilian logistics business rules — per-ton tariffs, per-state tolls, ad valorem/insurance, and interstate ICMS tax.

> 💡 Companion backend for a Streamlit freight calculator frontend. Demonstrates a full-stack approach: web UI for operators + REST API for system-to-system integration.

---

## 🔗 Live Demo

**Swagger UI:** https://web-production-39b08.up.railway.app/docs

Interactive API docs with all endpoints. Try `POST /rotas` to register a route, then `POST /calcular` to compute freight cost. Demo data persists across deploys (SQLite on Railway volume).

---

## ✨ Features

- 🧮 **Full freight calculation** — base freight + tolls + ad valorem/insurance + ICMS, itemized
- 🗺️ **Route CRUD** — register routes with per-ton tariffs and per-state toll lists
- 💰 **Interstate ICMS** — automatic rate lookup following ANTT/CONFAZ matrix
- 📊 **Transparent output** — every component of the cost returned separately
- 📖 **Interactive docs** — Swagger UI at `/docs` and ReDoc at `/redoc` out of the box
- 💾 **Persistent storage** — SQLite on Railway volume, data survives redeploys

---

## 🛠️ Tech Stack

| Layer        | Technology     |
| ------------ | -------------- |
| Language     | Python 3.11+   |
| Framework    | FastAPI        |
| ORM          | SQLAlchemy 2.0 |
| Database     | SQLite         |
| ASGI server  | Uvicorn        |
| Validation   | Pydantic v2    |
| Deploy       | Railway        |

---

## 📐 Business Rules

Every `/calcular` request is resolved as:

```
frete_base       = peso_toneladas × tarifa_por_tonelada
advalorem_seguro = valor_nota × 0.74%
pedagio_total    = Σ pedágios da rota
subtotal         = frete_base + pedagio_total + advalorem_seguro
icms             = subtotal × alíquota_interestadual(origem → destino)
total            = subtotal + icms
```

ICMS rates follow the Brazilian interstate matrix (7% for Norte/Nordeste/Centro-Oeste destinations, 12% for Sul/Sudeste, etc).

---

## 🔌 Endpoints

| Method | Path                            | Description                  |
| ------ | ------------------------------- | ---------------------------- |
| POST   | `/rotas`                        | Register a new route         |
| GET    | `/rotas`                        | List all routes              |
| GET    | `/rotas/{origem}/{destino}`     | Get a specific route         |
| PUT    | `/rotas/{origem}/{destino}`     | Update route tariff/tolls    |
| DELETE | `/rotas/{origem}/{destino}`     | Delete route                 |
| POST   | `/calcular`                     | Calculate full freight cost  |

Full interactive documentation at `GET /docs`.

---

## 📋 Example: Calculate Freight

**Request:**

```http
POST /calcular
Content-Type: application/json

{
  "origem": "SP",
  "destino": "MG",
  "peso_toneladas": 28,
  "valor_nota": 150000.00
}
```

**Response:**

```json
{
  "origem": "SP",
  "destino": "MG",
  "peso_toneladas": 28,
  "valor_nota": 150000.00,
  "frete_base": 4200.00,
  "pedagio_total": 85.50,
  "advalorem_seguro": 1110.00,
  "subtotal": 5395.50,
  "aliquota_icms": 12,
  "icms": 647.46,
  "total": 6042.96,
  "detalhes_pedagio": [
    { "estado": "SP", "valor": 42.75 },
    { "estado": "MG", "valor": 42.75 }
  ]
}
```

---

## 🚀 Running Locally

```bash
# 1. Clone
git clone https://github.com/Azevedo-073/api-frete.git
cd api-frete

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the server
uvicorn main:app --reload

# 4. Open Swagger UI
# → http://127.0.0.1:8000/docs
```

The local SQLite file (`frete.db`) is created automatically on first run.

---

## ☁️ Deploying on Railway

1. Fork this repo
2. Create a new Railway project → **Deploy from GitHub repo**
3. Attach a **Volume** to the service with mount path `/app/data`
4. Add an environment variable: `DB_PATH=/app/data/frete.db`
5. Railway detects FastAPI via the `Procfile` and serves it on the generated domain

---

## 📁 Project Structure

```
api-frete/
├── main.py          # FastAPI app + route handlers
├── database.py      # SQLAlchemy models (Rota, Pedagio) + session
├── schemas.py       # Pydantic schemas (request/response)
├── icms.py          # Interstate ICMS rate lookup
├── requirements.txt # Pinned dependencies
├── Procfile         # Railway start command
├── README.md
└── .gitignore
```

---

## 🗺️ Roadmap

- [x] Deploy to Railway with persistent SQLite volume
- [x] Complete README with endpoints + example payload
- [ ] Migrate SQLite → PostgreSQL for production durability
- [ ] API key authentication
- [ ] Rate-limiting middleware
- [ ] Dockerfile for containerized deploy
- [ ] GitHub Actions CI (lint + pytest)
- [ ] Full pytest coverage on all endpoints

---

## 👤 Author

**Marco Azevedo**  
Logistics automation — building real tools for real freight operations in Brazil.

- 💼 [LinkedIn](https://www.linkedin.com/in/marco-otávio-azevedo)
- 🐙 [GitHub](https://github.com/Azevedo-073)

---

## 📄 License

MIT