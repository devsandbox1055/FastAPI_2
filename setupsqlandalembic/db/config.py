from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

class User(SQLModel,table=True):
    id:Optional[int] = Field(default=None, Primary_key=True)
    name:str

    posts:List["Post"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={"cascade":"all,delete"}
    )
class Post(SQLModel,table= True):
    id:Optional[int] = Field(default=None,primary_key=True)
    title:str
    user_id:int = Field(foreign_key="user.id")

    user: Optional[User] =  Relationship(back_populates="posts")