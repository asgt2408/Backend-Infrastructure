from fastapi import APIRouter, HTTPException, Depends
from ride_service.database import SessionLocal
from ride_service.models import Ride, Base
from sqlalchemy.orm import Session
from driver_service.models import Driver
from ride_service.logger import logger

router = APIRouter()

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()


@router.post('/completes')
def ride_completed(ride_id:int,driver_id:int,db:Session = Depends(get_db)):

	updated = db.query(Ride).filter(Ride.id==ride_id,
		Ride.status=="STARTED").update({
		"status":"COMPLETED"
		})

	driver = db.query(Driver).filter(Driver.id==driver_id).first()

	if driver:
		driver.is_online = 1

	db.commit()

	logger.info(f"Ride Completed, | ride_id={ride_id}, driver_id={driver_id}")

	return {
		"message":"Ride completed successfully",
		"ride_id":ride_id
		}
