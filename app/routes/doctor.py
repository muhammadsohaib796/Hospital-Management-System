from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.doctor import DoctorCreate, DoctorUpdate, DoctorResponse
from app.crud import doctor as doctor_crud

router = APIRouter(prefix="/doctor", tags=["Doctor"])


@router.post("/", response_model=DoctorResponse)
def create_doctor(doctor_data: DoctorCreate, db: Session = Depends(get_db)):
    return doctor_crud.create_doctor(db, doctor_data)


@router.get("/", response_model=list[DoctorResponse])
def get_all_doctors(db: Session = Depends(get_db)):
    return doctor_crud.get_all_doctors(db)


@router.get("/{doctor_id}", response_model=DoctorResponse)
def get_doctor(doctor_id: int, db: Session = Depends(get_db)):
    return doctor_crud.get_doctor(db, doctor_id)


@router.put("/{doctor_id}", response_model=DoctorResponse)
def update_doctor(doctor_id: int, doctor_data: DoctorUpdate, db: Session = Depends(get_db)):
    return doctor_crud.update_doctor(db, doctor_id, doctor_data)


@router.delete("/{doctor_id}", response_model=DoctorResponse)
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    return doctor_crud.delete_doctor(db, doctor_id)