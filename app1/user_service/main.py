from fastapi import FastAPI, Depends
from signup.main import router as signup_router
from login.main import router as login_router
from profile.main import router as profile_router

app = FastAPI()
app.include_router(signup_router, prefix='/signup', tags=["Auth"])
app.include_router(login_router, prefix='/login', tags=["Auth"])
app.include_router(profile_router, prefix='/profile', tags=["Profile"])
