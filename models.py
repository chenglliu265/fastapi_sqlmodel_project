from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    __tablename__ = "users"
    id:int = Field(default=None,primary_key=True,nullable=False)
    name:str = Field(default=None,nullable=False,max_length=50)
    age:int
    email:str=Field(default=None,unique=True,max_length=100)