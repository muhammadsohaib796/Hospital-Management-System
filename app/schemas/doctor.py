from pydantic import BaseModel, EmailStr
from typing import Optional

class DoctorCreate(BaseModel):
    name: str
    specialization: str
    email: EmailStr
    phone: Optional[str] = None
    salary: Optional[float] = None

class DoctorUpdate(BaseModel):
    name: Optional[str] = None
    specialization: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    salary: Optional[float] = None

class DoctorResponse(BaseModel):
    id: int
    name: str
    specialization: str
    email: str
    phone: Optional[str] = None
    salary: Optional[float] = None

    class Config:
        from_attributes = True