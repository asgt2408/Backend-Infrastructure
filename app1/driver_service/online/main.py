from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from database import SessionLocal
from models import Base, Driver

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class DriverStatus(BaseModel):
    driver_id: int


@router.post("/")
def status(data: DriverStatus, db: Session = Depends(get_db)):
    driver = db.query(Driver).filter(Driver.id == data.driver_id).first()

    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")

    driver.is_online = True
    db.commit()

    return {
        "message": "Driver goes online",
        "Driver_id": driver.id,
    }
