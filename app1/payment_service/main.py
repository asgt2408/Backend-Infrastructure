from fastapi import FastAPI
from payment_service.payment import router as payment_router        

app = FastAPI()

app.include_router(payment_router,prefix='/payment',tags=["Payment"])