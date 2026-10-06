from sqlalchemy import Column, Integer, String

from .database import Base

class Student(Base):

    __tablename__ = "students"

    roll_no = Column(Integer,primary_key=True, index=True)
    name = Column(String,nullable=False)
    email = Column(String, unique=True, nullable=False)
    branch = Column(String, nullable=False)

    