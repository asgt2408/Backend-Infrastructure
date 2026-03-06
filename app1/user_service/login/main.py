from fastapi import FastAPI,Depends
from pydantic import BaseModel
from models import User,Base
from sqlalchemy.orm import Session
from database import engine,SessionLocal
from passlib.context import CryptContext
from jose import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


app = FastAPI()

Base.metadata.create_all(bind=engine)

SECRET_KEY="mysectetkey"
ALGORITHM="HS256"


def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

class Usercreate(BaseModel):
	username:str
	email:str
	password:str

def token(data : dict):
	token = jwt.encode(data,SECRET_KEY,algorithm = ALGORITHM)
	return token


@app.post("/login")
def login(user:Usercreate, db : Session = Depends(get_db)):

	check_user = db.query(User).filter(User.email==user.email).first()

	if not check_user:
		return {"message": "Invalid Login"}

	passw = pwd_context.verify(user.password[:72],check_user.password)

	if not passw:
		return {"message": "Password is Incorrect"}

	access_token = token({"email":check_user.email})

	return {"Message": "Login Successfull",
			"token" : access_token}


