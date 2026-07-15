from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.patient import PatientCreate, PatientUpdate, PatientResponse
from app.crud import patient as patient_crud

router = APIRouter(prefix="/patient", tags=["Patient"])


@router.post("/", response_model=PatientResponse)
def create_patient(patient_data: PatientCreate, db: Session = Depends(get_db)):
    return patient_crud.create_patient(db, patient_data)


@router.get("/", response_model=list[PatientResponse])
def get_all_patients(db: Session = Depends(get_db)):
    return patient_crud.get_all_patients(db)


@router.get("/{patient_id}", response_model=PatientResponse)
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    return patient_crud.get_patient(db, patient_id)


@router.put("/{patient_id}", response_model=PatientResponse)
def update_patient(patient_id: int, patient_data: PatientUpdate, db: Session = Depends(get_db)):
    return patient_crud.update_patient(db, patient_id, patient_data)


@router.delete("/{patient_id}", response_model=PatientResponse)
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    return patient_crud.delete_patient(db, patient_id)