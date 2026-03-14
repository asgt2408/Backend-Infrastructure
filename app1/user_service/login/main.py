from fastapi import APIRouter,Depends
from pydantic import BaseModel
from user_service.models import User,Base
from sqlalchemy.orm import Session
from user_service.database import engine,SessionLocal
from passlib.context import CryptContext
from jose import jwt
from fastapi.security import OAuth2PasswordRequestForm

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()

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

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    check_user = db.query(User).filter(User.username == form_data.username).first()

    if not check_user:
        return {"message": "Invalid Login"}

    password_bytes = form_data.password.encode("utf-8")[:72]
    password = password_bytes.decode("utf-8", "ignore")

    passw = pwd_context.verify(password, check_user.password)

    if not passw:
        return {"message": "Password is Incorrect"}

    access_token = token({"Username": check_user.username})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
