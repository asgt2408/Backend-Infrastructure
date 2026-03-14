from fastapi import APIRouter,Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from user_service.models import User,Base
from user_service.database import engine,SessionLocal
from sqlalchemy.orm import Session
from jose import jwt

router = APIRouter()

SECRET_KEY="mysectetkey"
ALGORITHM="HS256"

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@router.get("/profile")
def get_profile(token : str = Depends(oauth2_scheme), db : Session = Depends(get_db)):

	payload = jwt.decode(token,SECRET_KEY,algorithms=["HS256"])
	email = payload.get("email")

	user = db.query(User).filter(User.email == email).first()

	return {
		"username" : user.username,
		"Email" : user.email
		}
