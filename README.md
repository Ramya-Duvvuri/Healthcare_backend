
# MediConnect – Healthcare Backend API

[![Python](https://img.shields.io/badge/python-3.x-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-4.x-green)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.x-blueviolet)](https://www.django-rest-framework.org/)


A **robust backend API** for managing **patients, doctors, and appointments**, built with **Django & Django REST Framework**. Designed for fast, secure, and scalable healthcare management.

---

## 🚀 Features

- User authentication with **JWT** & **role-based access** (patients, doctors, admin)
- CRUD operations for **patients**, **doctors**, and **appointments**
- RESTful API endpoints with **validation & error handling**
- Modular, maintainable Django project structure for **scalability & readability**

---

## 🛠 Tech Stack

- **Backend:** Django, Django REST Framework  
- **Database:** SQLite (development) / PostgreSQL (production)  
- **Authentication:** JWT / Token-based  
- **Environment:** Python 3.x, Virtualenv  

---

## ⚡ Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/Ramya-Duvvuri/Healthcare_backend.git
cd Healthcare_backend
````

### 2. Set up virtual environment & install dependencies

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```
DJANGO_SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

### 4. Run migrations & start server

```bash
python manage.py migrate
python manage.py runserver
```

Server will run at: `http://127.0.0.1:8000/`

---

## 📂 Project Structure

```
Healthcare_backend/
│
├── api/               # App for patients, doctors, appointments
├── users/             # App for user management & authentication
├── Healthcare_backend/ # Django settings & URLs
├── manage.py
├── requirements.txt
└── .env
```

---

## 📚 API Endpoints

### Authentication

* **POST** `/users/login/` – Login user & return JWT
* **POST** `/users/register/` – Register new user

### Patients

* **GET** `/patients/` – List all patients
* **POST** `/patients/` – Create new patient
* **PUT** `/patients/{id}/` – Update patient
* **DELETE** `/patients/{id}/` – Delete patient

### Doctors

* **GET** `/doctors/` – List all doctors
* **POST** `/doctors/` – Add new doctor
* **PUT** `/doctors/{id}/` – Update doctor
* **DELETE** `/doctors/{id}/` – Delete doctor

### Appointments

* **GET** `/appointments/` – List all appointments
* **POST** `/appointments/` – Create appointment
* **PUT** `/appointments/{id}/` – Update appointment
* **DELETE** `/appointments/{id}/` – Delete appointment

---

## 🤝 Contributing

1. Fork → Create branch → Commit → Push → Pull Request
2. Follow existing **code style**
3. Write **tests** for new features
4. Ensure **code passes linting & tests** before submitting



