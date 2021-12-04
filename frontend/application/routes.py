from application import app
from application.forms import CreateBandForm, CreateAgentForm
from flask import render_template, request, redirect, url_for, jsonify
import requests

@app.route('/', methods=["GET"])
def home():
    agents = requests.get(f"http://bc-backend:5000/read/allAgents").json()["agents"]
    return render_template("index.html", title="Home", agents=agents)

@app.route('/create/agent', methods=["GET", "POST"])
def create_agent():
    form = CreateAgentForm()

    if request.method == "POST":
        response = requests.post(
            f"http://bc-backend:5000/create/agent",
            json={
                "name": form.name.data,
                "phone": form.phone.data                
            }
        )
    return redirect(url_for("home"))

@app.route('/create/band', methods=['GET', 'POST'])
def create_band():
    form = CreateBandForm()

    package = requests.get(f"http://bc-backend:5000/read/allAgents").json()
    for agents in package["agents"]:
        form.agent.choices.append(agent["id"], agent["name"])

    if request.method == "POST":
        response = requests.post(
            f"http://bc-backend:5000/create/band/{form.agent.data}",
            package={
                "name": form.name.data,
                "phone": form.phone.data
            }
        )
        return redirect(url_for("home"))

    return render_template("create_band.html", title="Add Band", form=form)