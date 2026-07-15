# Hospital Management System API

A backend CRUD (Create, Read, Update, Delete) application built with **FastAPI** to manage hospital records — Doctors, Patients, and Staff. Built as a hands-on learning project to practice clean backend architecture, ORM usage, and database migrations.

## Features

- RESTful CRUD APIs for Doctors, Patients, and Staff
- SQLAlchemy ORM for database models
- Pydantic schemas for request/response validation
- Alembic for database migrations (version-controlled schema changes)
- Foreign key relationship between Patient and Doctor
- Proper error handling with HTTP status codes (404 for missing records)
- Auto-generated interactive API docs (Swagger UI)
- Environment-based configuration (credentials never hardcoded)

## Project Structure
HospitalManagement/
├── app/
│   ├── main.py          # App entry point, includes all routers
│   ├── database.py      # DB engine, session, and get_db dependency
│   ├── config.py         # Loads settings from .env
│   │
│   ├── models/           # SQLAlchemy table definitions
│   │   ├── doctor.py
│   │   └── patient.py
│   │
│   ├── schemas/           # Pydantic request/response schemas
│   │   ├── doctor.py
│   │   └── patient.py
│   │
│   ├── crud/               # Database operation functions
│   │   ├── doctor.py
│   │   └── patient.py
│   │
│   └── routes/             # API endpoint definitions
│       ├── doctor.py
│       └── patient.py
│
├── alembic/                # Migration scripts
├── requirements.txt
├── .gitignore
└── README.md



## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd HospitalManagement
```

### 2. Create and activate a virtual environment

```bash
python -m venv hospital_env
```

Windows (PowerShell):
```bash
.\hospital_env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a MySQL database

```sql
CREATE DATABASE hospital_db;
```

### 5. Configure environment variables

Create a `.env` file in the project root:


### 6. Run database migrations

```bash
alembic upgrade head
```

### 7. Start the server

```bash
uvicorn app.main:app --reload
```

### 8. Open the API docs

Visit [http://localhost:8000/docs](http://localhost:8000/docs) to test all endpoints interactively.

## API Endpoints

### Doctor
| Method | Endpoint | Description |
|---|---|---|
| POST | `/doctor/` | Create a new doctor |
| GET | `/doctor/` | Get all doctors |
| GET | `/doctor/{id}` | Get a doctor by ID |
| PUT | `/doctor/{id}` | Update a doctor |
| DELETE | `/doctor/{id}` | Delete a doctor |

### Patient
| Method | Endpoint | Description |
|---|---|---|
| POST | `/patient/` | Create a new patient |
| GET | `/patient/` | Get all patients |
| GET | `/patient/{id}` | Get a patient by ID |
| PUT | `/patient/{id}` | Update a patient |
| DELETE | `/patient/{id}` | Delete a patient |

### Staff *(coming soon)*
| Method | Endpoint | Description |
|---|---|---|
| POST | `/staff/` | Create a new staff member |
| GET | `/staff/` | Get all staff |
| GET | `/staff/{id}` | Get a staff member by ID |
| PUT | `/staff/{id}` | Update a staff member |
| DELETE | `/staff/{id}` | Delete a staff member |

## Database Schema

**Doctor**
- id, name, specialization, email, phone, salary

**Patient**
- id, name, age, gender, disease, doctor_id (FK → Doctor), admission_date

**Staff**
- id, name, role, shift, salary

## Author

Muhammad Sohaib — learning backend development with FastAPI