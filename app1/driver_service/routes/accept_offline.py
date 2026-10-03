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

@router.put("/accept_offline/{driver_id}")
def accept_offline(driver_id:int, db:Session = Depends(get_db)):
    driver = db.query(Driver).filter(Driver.id==driver_id).first()

    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")

    driver.is_online = 0

    db.commit()

    return {
        "message":"Driver is now offline",
        "driver_id":driver_id
    }
