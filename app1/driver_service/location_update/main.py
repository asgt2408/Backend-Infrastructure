from fastapi import APIRouter, Depends, HTTPException
from driver_service.database import SessionLocal
from driver_service.models import Driver
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime


router = APIRouter()

def get_db():
	db = SessionLocal()

	try:
		yield db
	finally:
		db.close()

class LocationUpdate(BaseModel):
	driver_id : int
	lat : float
	lng : float

@router.post("/loc_update")
def l(loc : LocationUpdate, db: Session = Depends(get_db)):

	driver = db.query(Driver).filter(Driver.id == loc.driver_id).first()

	if not driver:
		raise HTTPException(status_code=404, detail="Driver Id not found")

	if not driver.is_online:
		raise HTTPException(status_code=404, detail="Driver is offline")

	driver.lat = loc.lat
	driver.lng = loc.lng
	driver.last_seen = datetime.utcnow()

	db.commit()

	return {
		"message": "Location Updated",
		"Driver_id": driver.id

	}
