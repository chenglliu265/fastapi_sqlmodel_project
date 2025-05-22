from fastapi import FastAPI,status,HTTPException,Depends
from contextlib  import asynccontextmanager
from db import init_db,get_session
from sqlmodel import Session
import schemas
from typing import List
import crud


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
    # Clean up the ML models and release the resources

app = FastAPI(lifespan=lifespan)


#登録
@app.post("/users/",response_model=schemas.UserRead,status_code=status.HTTP_201_CREATED)
def create_user(user:schemas.UserCreate,db:Session=Depends(get_session)):
    db_user = crud.create_user(db,user)
    return db_user

#取得
@app.get("/users/",response_model=List[schemas.UserRead])
def read_users(db:Session=Depends(get_session)):
    return crud.get_users(db)