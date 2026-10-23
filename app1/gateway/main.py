from fastapi import FastAPI
from routes.user import router as user_router
from routes.driver import router as driver_router
from routes.ride import router as ride_router

app = FastAPI()

app.include_router(user_router)
app.include_router(driver_router)
app.include_router(ride_router)

@app.get("/")
def home():
    return{
        "message": "Gateway is running"
    }