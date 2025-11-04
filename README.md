# 🧠 Intern Employee Management & AI Task Suggestion System

A Django REST Framework (DRF)** powered backend for managing employees, daily tasks, and AI-generated task suggestions.  
The system automates task assignments, email notifications, and integrates AI (OpenAI GPT 3.5 / OpenRouter) to generate smart next-task recommendations based on employee job roles and current progress.

---

## 🚀 Features

- 🧑‍💼 **Employee Management**
  - Add, edit, and view employee details
  - Role and job title–based organization

- 🧾 **Task Management**
  - Assign daily tasks to employees
  - Track task progress with start & end times
  - Capture screenshots and related resources

- 🤖 **AI Task Suggestions**
  - Integrates OpenAI / OpenRouter API to suggest next tasks
  - Suggests tasks based on job title and current performance
  - Auto-generates 10 default tasks for new employees (if none exist)

- ⏰ **Automated Email System**
  - Uses **Django Q (ORM backend)** for background task scheduling
  - Sends daily email notifications to employees at 9 AM with their assigned tasks

- 📬 **Background Scheduler**
  - Django Q handles automatic background execution (daily 9AM)
  - Reliable and server-friendly background task management

---

## 🏗️ Tech Stack

| Component | Technology |
|------------|-------------|
| Backend | Django 5.x, Django REST Framework |
| Database | Mysql |
| Task Queue | Django Q (ORM Backend) |
| AI Integration | OpenAI / OpenRouter API |
| Authentication | Knox / Token Authentication |
| Email | Django Email Backend (SMTP) |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
git clone https://github.com/surendransbscit/InternProjectEmadHubBackend.git
cd InternProjectEmadHubBackend

python -m venv venv
venv\Scripts\activate   # For Windows
# source venv/bin/activate  # For Linux/Mac

pip install -r requirements.txt #install all packages

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser # django Admin Access

python manage.py runserver # run server



