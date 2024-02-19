from sqlalchemy import Column, Integer, String
from database import Base


class Admin(Base):
    __tablename__ = 'admins'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    hashed_password = Column(String(255))
    email = Column(String(100), unique=True)
    role = Column(String(50))

    # Add methods as needed, e.g., for password verification
