from sqlalchemy import Column, ForeignKey, Integer, String

from .database import Base


class Name(Base):
    __tablename__ = "names"

    id = Column(Integer, primary_key=True)
    name = Column(String)



