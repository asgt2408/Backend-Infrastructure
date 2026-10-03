from fastapi import FastAPI, Depends
from routes.accept import router as accept_router
from routes.completed import router as complete_router
from routes.request import router as request_router
from routes.starts import router as start_router

app = FastAPI()
app.include_router(request_router, prefix='/request', tags=["Ride"])
app.include_router(accept_router, prefix='/accept', tags=["Ride"])
app.include_router(start_router, prefix='/start', tags=["Ride"])
app.include_router(complete_router, prefix='/complete', tags=["Ride"])
