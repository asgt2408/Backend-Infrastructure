from fastapi import APIRouter, Depends
from pydantic import BaseModel


def get_db():
	db = SessionLocal()

	try:
		yield db
	finally:
		db.close()


class Userride(BaseModel):
	user_id : int
	pickup_lat : float
	pickup_lng : float

@router.post("/user_location")
def user_loc(user : Userride, db: Session = Depends(get_db)):

	drivers = db.query(Driver).filter(Driver.is_online==True).all()

	if not drivers:
		raise HTTPException(status_code=404,detail="Drivers Not Availvable")


	nearest_driver = none
	min_distance = float("inf")

	for d in drivers:


		distance = ((d.lat-user.pickup_lat)**2 + (d.lng - user.pickup_lng)**2)**0.5

		if(distance < min_distance):
			min_distance = distance
			nearest_driver = d

	if not nearest_driver:
		raise HTTPException(status_code=404,detail="No valid Drivers found")


	return {
		"Message":"Driver Assigned Succussfully"
		"Driver_id":nearest_driver.id
		"distance":min_distance
	}
