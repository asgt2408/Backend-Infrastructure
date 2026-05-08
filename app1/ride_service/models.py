from sqlalchemy import String, Integer, Column, Boolean, DateTime, Float
from ride_service.database import Base
from datetime import datetime

class Ride(Base):
    __tablename__ = "rides"

    id = Column(Integer, primary_key=True, index=True)


    user_id = Column(Integer, nullable=False)
    driver_id = Column(Integer, nullable=True)


    pickup_lat = Column(Float, nullable=False)
    pickup_lng = Column(Float, nullable=False)


    status = Column(String(20), default="REQUESTED")


    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 

    payment_method = Column(String(20))
    payment_status = Column(String(20))
    fare = Column(Float)
