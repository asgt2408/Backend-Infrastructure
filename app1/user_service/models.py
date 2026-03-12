from sqlalchemy import String, Column, Integer
from user_service.database import Base

class User(Base):
	__tablename__ = "users"
	
	id = Column(Integer, primary_key=True, index=True)
	username = Column(String(100),nullable=False)
	email = Column(String(100),unique=True,nullable=False)
	password = Column(String(500),nullable=False)
