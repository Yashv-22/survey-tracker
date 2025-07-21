import sqlite3
from config import Config

# Create DB and table if not exists
def init_db():
    conn = sqlite3.connect(Config.DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_code TEXT UNIQUE NOT NULL,
            client_name TEXT NOT NULL,
            country TEXT NOT NULL,
            cpi REAL NOT NULL,
            loi INTEGER NOT NULL,
            status TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

# Add a new project
def add_project(data):
    conn = sqlite3.connect(Config.DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO projects
        (project_code, client_name, country, cpi, loi, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data['project_code'],
        data['client_name'],
        data['country'],
        data['cpi'],
        data['loi'],
        data['status']
    ))
    conn.commit()
    conn.close()

# Get all projects
def get_projects():
    conn = sqlite3.connect(Config.DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects")
    projects = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return projects

# Delete a project
def delete_project(project_code):
    conn = sqlite3.connect(Config.DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM projects WHERE project_code = ?", (project_code,))
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected > 0
