# Agent Space

A production-oriented starter for an AI agent operating platform.

## Stack

- Backend: FastAPI + SQLAlchemy + SQLite
- Frontend: React + Vite
- Auth: JWT
- AI: OpenAI-ready service

## Quick start

### Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Access

- Frontend: http://localhost:3000
- API: http://localhost:8000

## Notes

- This starter includes users, agents, tasks, workflows, and dashboard scaffolding.
- Add your OpenAI key in `backend/.env` to enable LLM execution.
