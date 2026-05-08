from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from driver_service.database import SessionLocal
from driver_service.models import Base, Driver
from pydantic import BaseModel

router = APIRouter()

def get_db():
	db = SessionLocal()

	try:
		yield db
	finally:
		db.close()

class Driveroffline(BaseModel):
	driver_id : int


@router.post("/go_offline")
def offline(data: Driveroffline, db: Session = Depends(get_db)):
	driver = db.query(Driver).filter(Driver.id==data.driver_id).first()

	if not driver:
		raise HTTPException(status_code=404, detail="Driver not found")


	driver.is_online = False
	db.commit()

	return{
		"driver_id":driver.id,
		"message":"Driver goes offline"
	}
