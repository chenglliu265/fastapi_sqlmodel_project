from sqlmodel import SQLModel
from pydantic import EmailStr
from typing import Optional


class UserBase(SQLModel):
    name: str
    age: Optional[int] = None
    email: str


class UserCreate(UserBase):
    pass


class UserUpdate(SQLModel):
    name: str
    age: Optional[int] = None
    email: str


class UserRead(UserBase):
    id: int
