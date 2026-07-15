from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate, DoctorUpdate


def create_doctor(db: Session, doctor_data: DoctorCreate):
    new_doctor = Doctor(**doctor_data.dict())
    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)
    return new_doctor


def get_doctor(db: Session, doctor_id: int):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor


def get_all_doctors(db: Session):
    return db.query(Doctor).all()


def update_doctor(db: Session, doctor_id: int, doctor_data: DoctorUpdate):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    update_data = doctor_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(doctor, key, value)

    db.commit()
    db.refresh(doctor)
    return doctor


def delete_doctor(db: Session, doctor_id: int):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    db.delete(doctor)
    db.commit()
    return doctor