# Reminder App – Backend API

This is the backend for the **Reminder App**, built using **Django** and **Django Ninja**. It exposes a set of secure RESTful APIs for user authentication and managing medicine reminders.

---

## 🚀 Tech Stack

- **Framework**: Django, Django Ninja
- **Database**: PostgreSQL (via [Neon](https://neon.tech/))
- **Authentication**: JWT-based
- **Deployment**: [Railway](https://railway.app/)

---

## 📂 Features

- ✅ User registration and login with JWT
- 💊 Create, read, update, and delete  reminders (CRUD)
- 🔒 Protected endpoints using JWT tokens
- ⚙️ Admin panel and ORM support

---

## 🛠️ Getting Started

Follow these steps to run the backend locally:

### 1. Clone the Repository

```bash
git clone https://github.com/GauravRaj6767/Reminder-App-Django-Backend-API.git
cd Reminder-App-Django-Backend-API
```

### 2. Create and Activate a Virtual Environment
On Windows:
```bash
python -m venv env
env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create .env File
```env
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=your-neon-postgres-url
```
### 5. Apply Database Migrations
```bash
python manage.py migrate
```

### 6. Start the Development Server
```bash
python manage.py runserver
```

## Visit the API at:
📡 http://localhost:8000/api
