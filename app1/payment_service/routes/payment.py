from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from payment_service.database import SessionLocal
from ride_service.models import Ride

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/payment")
def make_payment(
    ride_id: int,
    payment_method: str,
    fare: float,
    db: Session = Depends(get_db)
):

    ride = db.query(Ride).filter(Ride.id == ride_id).first()

    if not ride:
        raise HTTPException(status_code=404, detail="Ride not found")

    if ride.status != "COMPLETED":
        raise HTTPException(status_code=400, detail="Ride not completed yet")

    ride.payment_method = payment_method
    ride.payment_status = "PAID"
    ride.fare = fare

    db.commit()

    return {
        "message": "Payment successful",
        "ride_id": ride_id,
        "fare": fare,
        "payment_method": payment_method
    }
