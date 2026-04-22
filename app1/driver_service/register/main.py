from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from driver_service.database import SessionLocal, engine
from driver_service.models import Base, Driver

router = APIRouter()

# Create tables
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Request Schema
class DriverRegister(BaseModel):
    user_id: int
    vehicle_number: str


@router.post("/register")
def register(driver: DriverRegister, db: Session = Depends(get_db)):

    # Check if driver already exists
    existing_driver = db.query(Driver).filter(Driver.user_id == driver.user_id).first()

    if existing_driver:
        raise HTTPException(
            status_code=400,
            detail="Driver already registered"
        )

    new_driver = Driver(
        user_id=driver.user_id,
        vehicle_number=driver.vehicle_number,
        is_online=False
    )

    try:
        db.add(new_driver)
        db.commit()
        db.refresh(new_driver)

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Driver registration failed"
        )

    return {
        "driver_id": new_driver.id,
        "user_id": new_driver.user_id,
        "vehicle_number": new_driver.vehicle_number,
        "status": "Driver registered successfully"
    }
