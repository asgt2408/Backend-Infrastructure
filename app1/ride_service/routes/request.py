from fastapi import APIRouter, Depends, HTTPException
from  ride_service.database import SessionLocal,engine
from ride_service.models import Ride,Base
from sqlalchemy.orm import Session
from pydantic import BaseModel

Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
	db = SessionLocal()

	try:
		yield db
	finally:
		db.close()


class RideModel(BaseModel):
	user_id : int
	pickup_lat : float
	pickup_lng : float


@router.post("/request")
def req(data : RideModel, db:Session = Depends(get_db)):

	ride = Ride(
		user_id = data.user_id,
		pickup_lat = data.pickup_lat,
		pickup_lng = data.pickup_lng
	)

	db.add(ride)
	db.commit()
	db.refresh(ride)

	return {
		"Message": "Ride Requested Successfully"
	}


