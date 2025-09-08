# Users API (FastAPI)

API REST para consulta de usuários com filtros, ordenação e paginação, usando base mock (JSON) passado pela Valcann.

## ▶️ Como executar

### 1) criar e ativar o venv (Windows PowerShell)
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2) instalar dependências
```bash
pip install -r requirements.txt 
```
#### (principais: fastapi, uvicorn, pydantic)

### 3) subir a API
```bash 
python -m src.app
```

* Swagger: `http://localhost:3000/docs`

* Python Version: 3.12
