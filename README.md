# AI App Compiler

Compiler-style AI system:

Natural Language -> Structured IR -> Validation -> Repair -> Runtime

## Features

- Multi-stage pipeline
- Deterministic JSON generation
- Schema validation
- Repair engine
- Runtime generation
- FastAPI backend
- React frontend

## Run Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Run Frontend

```bash
cd frontend
npm install
npm start
```