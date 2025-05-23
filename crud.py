from sqlmodel import Session, select
from models import User
import schemas


def create_user(session: Session, user_create: schemas.UserCreate) -> User:
    db_user = User(name=user_create.name, age=user_create.age, email=user_create.email)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def get_users(session: Session) -> User:
    return session.exec(select(User)).all()


def get_user(session: Session, id: int) -> User:
    return session.get(User, id)


def update_user(session: Session, id: int, user_update: schemas.UserUpdate) -> User:
    # 查询用户
    db_user = session.get(User, id)
    if not db_user:
        return None
    update_data = user_update.model_dump(exclude_unset=True)
    for key, val in update_data.items():
        setattr(db_user, key, val)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def delete_user(session: Session, id: int) -> bool:
    db_user = session.get(User, id)
    if not db_user:
        return False
    session.delete(db_user)
    session.commit()
    return True
