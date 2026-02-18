from db import engine
from sqlalchemy import  MetaData , Column, String, ForeignKey , Table , Integer
Forie

metadata = MetaData()

#user table
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key= True),
    Column("name", String(length=50), nullable=False),
    Column("email", String, nullable=False, unique=True)
)

posts = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key= True),
    Column("user_id",  Integer, ForeignKey("user.id" , ondelete="CASCADE"), nullable=False),
    Column("title", String, nullable=False),
    Column("content", String, nullable=False)
)

profile = Table(
    "profile",
    metadata,
    Column("id", Integer, primary_key= True),
    Column("user_id",  Integer, ForeignKey("user.id" , ondelete="CASCADE"), nullable=False),
    Column("bio", String, unique=False),
    Column("address", String, nullable=False)
)

#create table in database
def create_table():
    metadata.create_all(engine)