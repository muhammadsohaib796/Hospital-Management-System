from pydantic import BaseModel
from typing import Optional
from datetime import date


class PatientCreate(BaseModel):
    name: str
    age: int
    gender: str
    disease: Optional[str] = None
    doctor_id: Optional[int] = None
    admission_date: Optional[date] = None


class PatientUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    disease: Optional[str] = None
    doctor_id: Optional[int] = None
    admission_date: Optional[date] = None


class PatientResponse(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    disease: Optional[str] = None
    doctor_id: Optional[int] = None
    admission_date: Optional[date] = None

    class Config:
        from_attributes = True