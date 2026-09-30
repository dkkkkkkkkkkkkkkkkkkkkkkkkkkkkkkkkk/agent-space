from sqlalchemy.orm import Session

from app.models import Agent, Task, User, Workflow
from app.security import hash_password


def create_user(db: Session, email: str, username: str, password: str):
    user = User(
        email=email,
        username=username,
        password_hash=hash_password(password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def create_agent(db: Session, name: str, description: str, owner_id: int):
    agent = Agent(name=name, description=description, owner_id=owner_id)
    db.add(agent)
    db.commit()
    db.refresh(agent)
    return agent


def list_agents(db: Session, owner_id: int):
    return db.query(Agent).filter(Agent.owner_id == owner_id).all()


def create_task(db: Session, title: str, description: str, owner_id: int, agent_id: int | None = None):
    task = Task(title=title, description=description, owner_id=owner_id, agent_id=agent_id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def list_tasks(db: Session, owner_id: int):
    return db.query(Task).filter(Task.owner_id == owner_id).all()


def create_workflow(db: Session, name: str, prompt: str, steps: str, owner_id: int):
    workflow = Workflow(name=name, prompt=prompt, steps=steps, owner_id=owner_id)
    db.add(workflow)
    db.commit()
    db.refresh(workflow)
    return workflow


def list_workflows(db: Session, owner_id: int):
    return db.query(Workflow).filter(Workflow.owner_id == owner_id).all()
