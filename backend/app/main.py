from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.auth import get_current_user, get_db
from app.crud import create_agent, create_task, create_user, create_workflow, get_user_by_email, list_agents, list_tasks, list_workflows
from app.database import Base, engine
from app.models import User
from app.schemas import AgentCreate, TaskCreate, UserCreate, WorkflowCreate
from app.security import create_access_token, verify_password

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Agent Space API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Agent Space API is running"}


@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    token = create_access_token(user.id)
    return {"access_token": token, "token_type": "bearer"}


@app.post("/register")
def register(payload: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_email(db, payload.email):
        raise HTTPException(status_code=400, detail="Email already exists")
    user = create_user(db, payload.email, payload.username, payload.password)
    token = create_access_token(user.id)
    return {"access_token": token, "token_type": "bearer"}


@app.get("/me")
def me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "username": current_user.username,
    }


@app.post("/agents")
def create_new_agent(payload: AgentCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    agent = create_agent(db, payload.name, payload.description or "", current_user.id)
    return {"id": agent.id, "name": agent.name, "description": agent.description, "status": agent.status}


@app.get("/agents")
def get_agents(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return list_agents(db, current_user.id)


@app.post("/tasks")
def create_new_task(payload: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    task = create_task(db, payload.title, payload.description or "", current_user.id, payload.agent_id)
    return {"id": task.id, "title": task.title, "description": task.description, "status": task.status}


@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return list_tasks(db, current_user.id)


@app.post("/workflows")
def create_new_workflow(payload: WorkflowCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    workflow = create_workflow(db, payload.name, payload.prompt, payload.steps, current_user.id)
    return {"id": workflow.id, "name": workflow.name, "prompt": workflow.prompt, "steps": workflow.steps}


@app.get("/workflows")
def get_workflows(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return list_workflows(db, current_user.id)
