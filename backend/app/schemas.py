from typing import Optional

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class AgentCreate(BaseModel):
    name: str
    description: Optional[str] = None


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    agent_id: Optional[int] = None


class WorkflowCreate(BaseModel):
    name: str
    prompt: str
    steps: str
