from fastapi import FastAPI, Depends
from ride_service.routes.accept import router as accept_router
from ride_service.routes.completed import router as complete_router
from ride_service.routes.request import router as request_router
from ride_service.routes.starts import router as start_router

app = FastAPI()
app.include_router(request_router, prefix='/Ride', tags=["Ride"])
app.include_router(accept_router, prefix='/Ride', tags=["Ride"])
app.include_router(start_router, prefix='/start', tags=["Ride"])
app.include_router(complete_router, prefix='/complete', tags=["Ride"])
