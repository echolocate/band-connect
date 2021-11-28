from application import app
from application.forms import TaskForm
from flask import render_template, request, redirect, url_for, jsonify
import requests

backend_host = "bc-app_backend:5000"

@app.route('/')
@app.route('/home')
def home():
    all_bands = requests.get(f"http://{backend_host}/read/allTasks").json()
    return render_template('index.html', title="Home", all_tasks=all_tasks["tasks"])

@app.route('/create/task', methods=['GET','POST'])
def create_task():
    form = TaskForm()

    if request.method == "POST":
        response = requests.post(
            f"http://{backend_host}/create/task",
            json={"description": form.description.data}
        )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for('home'))