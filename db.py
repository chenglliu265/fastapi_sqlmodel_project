from sqlmodel import SQLModel,create_engine,Session
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE,echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
