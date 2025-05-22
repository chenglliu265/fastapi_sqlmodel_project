from sqlmodel import Session, select
from models import User
from schemas import UserCreate

def create_user(session: Session, user_create: UserCreate) -> User:
    db_user = User(
        name=user_create.name,
        age=user_create.age,
        email=user_create.email
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

def get_users(session: Session) -> User:
    return session.exec(select(User)).all()