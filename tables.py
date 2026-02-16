from db import engine
from sqlalchemy import  MetaData , Column

metadata = MetaData()

#user table
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key= True),
    Column("name", String(length=50), nullable=False),
    Column("email", String, nullable=False, unique=True)

)
#create table in database
def create_table():
    metadata.create_all(engine)