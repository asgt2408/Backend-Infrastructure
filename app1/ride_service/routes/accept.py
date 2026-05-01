from fastapi import APIRouter, Depends, HTTPException
from ride_service.models import Base, Ride
from sqlalchemy.orm import Session
from driver_service.models import Base, Driver
from ride_service.database import SessionLocal
router = APIRouter()

def get_db():
	db = SessionLocal()

	try:
		yield db
	finally:
		db.close()



@router.get("/accept")
def extract(ride_id: int, driver_id:int,db: Session = Depends(get_db)):

	ride = db.query(Ride).filter(Ride.id==ride_id).first()

	if not ride:
		raise HTTPException(status_code=404, detail="Ride not found")

	driver = db.query(Driver).filter(Driver.id==driver_id).first()

	if not driver:
		raise HTTPException(status_code=404,detail="Driver not found")

	if ride.status!='REQUESTED':
		raise HTTPException(status_code=404,detail="Ride already taken")



	if driver.is_online!=1:
		raise HTTPException(status_code=404,detail="Driver not available")

	driver.is_online = 0
	ride.driver_id = driver_id
	ride.status = 'Accepted'

	db.commit()

	return {
		"message":"Ride Accepted",
		"Ride_id":ride_id,
		"Driver_id":driver_id,
	}

