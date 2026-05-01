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

	driver = db.query(Driver).filter(Driver.id==driver_id).first()

	if not driver:
                raise HTTPException(status_code=404,detail="Driver not found")


	if driver.is_online!=1:
                raise HTTPException(status_code=400,detail="Driver not available")


	updated = db.query(Ride).filter(Ride.id==ride_id , Ride.status=="REQUESTED").update({"status":"ACCEPTED","driver_id":driver_id})

	if updated == 0:
        	raise HTTPException(status_code=400, detail="Ride already taken")

	driver.is_online = 0

	db.commit()

	return {
		"message":"Ride Accepted",
		"Ride_id":ride_id,
		"Driver_id":driver_id,
	}

