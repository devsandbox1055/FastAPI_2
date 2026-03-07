from sqlalchemy.orm import DeclarativeBase , Mapped , MappedColumn
from sqlalchemy import String
from db import engine
class Base(DeclarativeBase):
    pass

#USER MODEL/USER TABLE

class User(Base):
    __tablename__="users"

id: Mapped[int] = MappedColumn(primary_key=True)
name: Mapped[str] = MappedColumn(String(50), nullable=False)
email: Mapped[str] = MappedColumn(String, nullable=False, unique= True)

def __repr__(self) -> str:
    return f"<User(id={self.id},name={self.name}, email={self.email})>"

# CREATE TABLE
def create_tables():
    Base.metadata.create_all(engine)