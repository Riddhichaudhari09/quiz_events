# Django Quiz & Events Application

A simple Quiz & Events Web Application built using **Django**, **SQLite**, and **TailwindCSS**.  
This project was created as part of an interview assignment.

---

## 🚀 Features

### **Quiz Section**
- List all quizzes
- Start a quiz
- Dynamic MCQ questions
- Score calculation
- Result display
- Store submission + answers in DB

### **Event Section**
- List upcoming events (title, date, location)

### **Tech Stack**
- Backend: Django (latest)
- Database: SQLite
- Frontend: Django Templates + TailwindCSS

---

## 🛠️ Installation & Setup Instructions

### **1. Clone Repository**
```bash
git clone https://github.com/<your-username>/django-quiz-events-app.git
cd django-quiz-events-app

### ** Create Virtual Environment:

python -m venv venv
# Activate virtual environment
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows

### **Install Requirements:

pip install -r requirements.txt

### **Run Migrations:

python manage.py migrate

### **Start Development Server:

python manage.py runserver

### **Now open in browser:

👉 http://127.0.0.1:8000/

### **Project Structure:

django-quiz-events-app/
├── quiz/                  # Quiz app
├── events/                # Events app
├── templates/             # HTML templates
├── static/                # CSS, JS, images
├── manage.py
├── requirements.txt
└── README.md

