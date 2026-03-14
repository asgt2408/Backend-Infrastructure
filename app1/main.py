from fastapi import FastAPI,Depends

from user_service.signup.main import router as signup_router
from user_service.login.main import router as login_router
from user_service.profile.main import router as profile_router

app = FastAPI()

app.include_router(signup_router,prefix='/auth',tags=["Auth"])
app.include_router(login_router,prefix='/auth',tags=["Auth"])
app.include_router(profile_router,prefix='/user',tags=["User"])

