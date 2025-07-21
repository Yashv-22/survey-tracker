# 📊 Survey Tracker

A simple full-stack web app to create, manage, and track survey projects.  
Built with **Python Flask (backend)**, **SQLite (database)**, **HTML/CSS/Bootstrap (frontend)**, and **Vanilla JS**.

---

## 🚀 Features
- ✅ Create new survey projects
- ✅ View, filter, and delete projects from dashboard
- ✅ Export projects as CSV
- ✅ Responsive UI with Bootstrap 4
- ✅ Backend API with Flask (SQLite database, no external DB needed)

---

## 📸 Screenshots

### 🎯 Dashboard Page
![Dashboard Screenshot](screenshots/dashboard.png)

### ➕ Create Project Page
![Create Project Screenshot](screenshots/create_project.png)

---

## 💻 Tech Stack
| Layer         | Tech                 |
|---------------|----------------------|
| Frontend      | HTML, CSS, Bootstrap |
| Backend       | Python Flask         |
| Database      | SQLite (Built-in)    |

---

## 📂 Folder Structure
survey-tracker/
├── app.py
├── config.py
├── models.py
├── requirements.txt
├── static/
│ ├── script.js
│ ├── style.css
├── templates/
│ ├── index.html
│ └── dashboard.html

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/survey-tracker.git
cd survey-tracker

2️⃣ Create Virtual Environment
# Create virtualenv
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Flask App
flask run
By default, the app runs at: http://127.0.0.1:5000

5️⃣ Access the Application
Create Project: http://127.0.0.1:5000
Dashboard: http://127.0.0.1:5000/dashboard.html

📦 API Endpoints
| Method | Endpoint               | Description          |
| ------ | ---------------------- | -------------------- |
| POST   | `/api/create-project`  | Create a new project |
| GET    | `/api/projects`        | Get all projects     |
| DELETE | `/api/projects/<code>` | Delete a project     |

📝 Requirements
Python 3.7+

Flask

Flask-Cors

👥 Contributing
Pull requests are welcome. For major changes, please open an issue first.

📜 License
MIT License © 2025 Yashvardhan Mishra
