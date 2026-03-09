from fastapi import FastAPI,Depends,HTTPException
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


app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
	return{
	"Signup for users working"
}

class Usercreate(BaseModel):
	username: str
	email : str
	password : str

@app.post("/signup")
def signup(user:Usercreate, db: Session = Depends(get_db)):
		hashed_password = pwd_context.hash(user.password)

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
