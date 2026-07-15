from fastapi import FastAPI
from app.routes.doctor import router as doctor_router

app = FastAPI()

app.include_router(doctor_router)

@app.get("/")
def read_root():
    return {"message": "Hospital Management System is running"}