from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import httpx
from database import SessionLocal
from models import Base, Ride

router = APIRouter()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@router.get("/accept")
def extract(ride_id: int, driver_id: int, db: Session = Depends(get_db)):
    response = httpx.get(f"http://localhost:8002/status/{driver_id}")

	
    print(response.status_code)
    print(response.json())

    if response.status_code == 400:
        raise HTTPException(status_code=400, detail="Driver not available")

    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Driver service error")

    driver = response.json()

    if driver["is_online"] != 1:
        raise HTTPException(status_code=400, detail="Driver not available")

    updated = db.query(Ride).filter(Ride.id == ride_id, Ride.status == "REQUESTED").update(
        {"status": "ACCEPTED", "driver_id": driver_id}
    )

    if updated == 0:
        raise HTTPException(status_code=400, detail="Ride already taken")

    httpx.put(f"http://localhost:8002/accept_offline/{driver_id}")
	
    db.commit()

    return {
        "message": "Ride Accepted",
        "Ride_id": ride_id,
        "Driver_id": driver_id,
    }

