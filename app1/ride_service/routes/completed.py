from fastapi import APIRouter, HTTPException, Depends
from database import SessionLocal
from models import Ride, Base
import httpx
from sqlalchemy.orm import Session
from logger import logger

router = APIRouter()

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()


@router.post('/')
def ride_completed(ride_id:int,driver_id:int,db:Session = Depends(get_db)):

	updated = db.query(Ride).filter(Ride.id==ride_id,
		Ride.status=="STARTED").update({
		"status":"COMPLETED"
		})

	httpx.put(f"http://localhost:8002/online/{driver_id}")

	db.commit()

	logger.info(f"Ride Completed, | ride_id={ride_id}, driver_id={driver_id}")

	return {
		"message":"Ride completed successfully",
		"ride_id":ride_id
		}
