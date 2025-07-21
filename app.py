from flask import Flask, request, jsonify, render_template
from models import init_db, add_project, get_projects, delete_project
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Initialize DB (creates database.db and table if missing)
init_db()

# Serve HTML pages
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard.html")
def dashboard():
    return render_template("dashboard.html")

# API: Create new project
@app.route("/api/create-project", methods=["POST"])
def api_create_project():
    data = request.json
    try:
        add_project(data)
        return jsonify({"message": "Project created successfully"}), 201
    except Exception as e:
        print(e)
        return jsonify({"error": "Project creation failed"}), 500

# API: Get all projects
@app.route("/api/projects", methods=["GET"])
def api_get_projects():
    try:
        projects = get_projects()
        return jsonify(projects)
    except Exception as e:
        print(e)
        return jsonify({"error": "Could not fetch projects"}), 500

# API: Delete project
@app.route("/api/projects/<project_code>", methods=["DELETE"])
def api_delete_project(project_code):
    try:
        if delete_project(project_code):
            return jsonify({"message": "Project deleted successfully"})
        else:
            return jsonify({"error": "Project not found"}), 404
    except Exception as e:
        print(e)
        return jsonify({"error": "Failed to delete project"}), 500

if __name__ == "__main__":
    app.run(debug=True)
