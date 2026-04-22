from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime
from driver_service.database import Base
from datetime import datetime


class Driver(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, unique=True, nullable=False)

    vehicle_number = Column(String(100), nullable=False)

    is_online = Column(Boolean, default=False)

    lat = Column(Float, nullable=True)
    lng = Column(Float, nullable=True)

    last_seen = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)
