from fastapi import FastAPI, Depends
from driver_service.location_update.main import router as loc_update_router
from driver_service.register.main import router as register_router
from driver_service.online.main import router as go_online_router
from driver_service.offline.offline import router as offline_router

app = FastAPI()

app.include_router(register_router, prefix='/Driver', tags=["Driver"])
app.include_router(go_online_router, prefix='/Driver', tags=["Driver"])
app.include_router(loc_update_router, prefix='/Driver', tags=["Driver"])
app.include_router(offline_router, prefix='/Driver', tags=["Driver"])