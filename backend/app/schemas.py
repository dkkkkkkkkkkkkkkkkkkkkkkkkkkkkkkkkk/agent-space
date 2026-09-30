from typing import Optional

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    username: str


class AgentCreate(BaseModel):
    name: str
    description: Optional[str] = None


class AgentOut(BaseModel):
    id: int
    name: str
    description: Optional[str]
    status: str


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    agent_id: Optional[int] = None


class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str
    agent_id: Optional[int]


class WorkflowCreate(BaseModel):
    name: str
    prompt: str
    steps: str


class WorkflowOut(BaseModel):
    id: int
    name: str
    prompt: str
    steps: str
