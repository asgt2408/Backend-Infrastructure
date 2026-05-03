from fastapi import APIRouter, HTTPException, Depends
from ride_service.database import SessionLocal
from ride_service.models import Ride, Base
from sqlalchemy.orm import Session
from driver_service.models import Driver

router = APIRouter()

def get_db():
	db = SessionLocal()

	try:
		yield db
	finally:
		db.close()

@router.get("/start")
def started(ride_id:int, driver_id:int, db: Session = Depends(get_db)):

	ride = db.query(Ride).filter(
		Ride.id == ride_id, 
		Ride.driver_id == driver_id, Ride.status == "ACCEPTED"

		).update({"status":"STARTED"})

	if not ride:
		raise HTTPException(status_code=404,detail="Invalid Ride State")

	db.commit()

	return {
		"message":"Ride started successfully",
		"ride_id":ride_id
		}
