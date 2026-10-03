from fastapi import FastAPI, Depends
from location_update.main import router as loc_update_router
from register.main import router as register_router
from online.main import router as go_online_router
from offline.offline import router as offline_router
from routes.status import router as status_router
from routes.accept_offline import router as accept_offline_router

app = FastAPI()

app.include_router(register_router, prefix='/register', tags=["Driver"])
app.include_router(go_online_router, prefix='/online', tags=["Driver"])
app.include_router(loc_update_router, prefix='/location', tags=["Driver"])
app.include_router(offline_router, prefix='/offline', tags=["Driver"])
app.include_router(status_router)
app.include_router(accept_offline_router)