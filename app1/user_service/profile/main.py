from fastapi import APIRouter,Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from models import User,Base
from database import engine,SessionLocal
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

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@router.get("/profile")
def get_profile(token : str = Depends(oauth2_scheme), db : Session = Depends(get_db)):

	payload = jwt.decode(token,SECRET_KEY,algorithms=["HS256"])
	username = payload.get("Username")

	user = db.query(User).filter(User.username == username).first()

	if not user:
		raise HTTPException(status_code=404, detail="User not found")

	return {
		"username" : user.username,
		"Email" : user.email
		}
