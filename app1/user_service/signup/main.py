from fastapi import Depends,HTTPException,APIRouter
from pydantic import BaseModel
from user_service.database import engine,SessionLocal
from user_service.models import Base,User
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

router = APIRouter()


Base.metadata.create_all(bind=engine)

@router.get("/")
def home():
	return{
	"Signup for users working"
}

class Usercreate(BaseModel):
	username: str
	email : str
	password : str

@router.post("/signup")
def signup(user:Usercreate, db: Session = Depends(get_db)):
		password_bytes = user.password.encode("utf-8")[:72]
		hashed_password = pwd_context.hash(password_bytes.decode("utf-8", "ignore"))

		new_user = User(
		username = user.username,
		email = user.email,
		password = hashed_password
		)

		try:
			db.add(new_user)
			db.commit()
			db.refresh(new_user)

		except IntegrityError:
			db.rollback()
			raise HTTPException(
				status_code=400,
				detail="Email entered already Exists"
				)
		return {
			"id":new_user.id,
			"username":new_user.username,
			"email":new_user.email
			}
