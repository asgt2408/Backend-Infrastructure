from fastapi import FastAPI,Depends

from user_service.signup.main import router as signup_router
from user_service.login.main import router as login_router
from user_service.profile.main import router as profile_router
from driver_service.register.main import router as register_router
from driver_service.online.main import router as go_online_router
from driver_service.location_update.main import router as loc_update_router

from ride_service.routes.request import router as request_router
from ride_service.routes.accept import router as accept_router
from ride_service.routes.starts import router as start_router
from ride_service.routes.completed import router as complete_router

app = FastAPI()

app.include_router(signup_router,prefix='/auth',tags=["Auth"])
app.include_router(login_router,prefix='/auth',tags=["Auth"])
app.include_router(profile_router,prefix='/user',tags=["User"])

app.include_router(register_router,prefix='/Driver',tags=["Driver"])
app.include_router(go_online_router,prefix='/Driver',tags=["Driver"])
app.include_router(loc_update_router,prefix='/Driver',tags=["Driver"])


app.include_router(request_router,prefix='/Ride',tags=["Ride"])
app.include_router(accept_router,prefix='/Ride',tags=["Ride"])
app.include_router(start_router,prefix='/start',tags=["Ride"])
app.include_router(complete_router,prefix='/complete',tags=["Ride"])
