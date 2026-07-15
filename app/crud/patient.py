from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientUpdate


def create_patient(db: Session, patient_data: PatientCreate):
    new_patient = Patient(**patient_data.dict())
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient


def get_patient(db: Session, patient_id: int):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


def get_all_patients(db: Session):
    return db.query(Patient).all()


def update_patient(db: Session, patient_id: int, patient_data: PatientUpdate):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    update_data = patient_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(patient, key, value)

    db.commit()
    db.refresh(patient)
    return patient


def delete_patient(db: Session, patient_id: int):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    db.delete(patient)
    db.commit()
    return patient