from fastapi import FastAPI
from app.routes.doctor import router as doctor_router
from app.routes.patient import router as patient_router

app = FastAPI()

app.include_router(doctor_router)
app.include_router(patient_router)

@app.get("/")
def read_root():
    return {"message": "Hospital Management System is running"}