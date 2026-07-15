from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(10), nullable=False)
    disease = Column(String(200), nullable=True)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    admission_date = Column(Date, nullable=False)

    doctor = relationship("Doctor")