from fastapi import APIRouter, HTTPException, Depends
from database import SessionLocal
from models import Driver, Base
from sqlalchemy.orm import Session

router = APIRouter()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@router.get("/status/{driver_id}")
def get_status(driver_id:int, db:Session = Depends(get_db)):

    driver = db.query(Driver).filter(Driver.id==driver_id).first()

    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")


    return {
        "driver_id": driver.id,
        "is_online": driver.is_online
    }

