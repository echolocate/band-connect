from application import app
from application.forms import CreateBandForm, CreateAgentForm
from flask import render_template, request, redirect, url_for, jsonify
import requests
from os import getenv

@app.route('/', methods=['GET'])
def home():
    bands = requests.get("http://bc-backend:5000/read/allBands").json()["bands"]
    return render_template('index.html', title="Home", bands=bands)

@app.route('/create/agent', methods=['GET','POST'])
def create_agent():
    form = CreateAgentForm()

    if request.method == "POST":
        response = requests.post(
            f"http://{backend}/create/agent",
            json={
                "name": form.name.data, 
                "phone": form.phone.data
            }
        )        
        return redirect(url_for('home'))

    return render_template("create_agent.html", title="Add agent", form=form)
    

# @app.route('/create/band', methods=['GET','POST'])
# def create_band():
#     form = BandForm()

#     if request.method == "POST":
#         response = requests.post(
#             f"http://{backend_host}/create/band",
#             json={"name": form.name.data}
#         )
#         app.logger.info(f"Response: {response.text}")
#         return redirect(url_for('home'))

# @app.route('/update/band/<int:id>', methods=['GET','POST'])
# def update_band(id):
#     form = BandForm()
#     band = requests.get(f"http://{backend_host}/read/band/{id}").json()
#     app.logger.info(f"Band: {band}")

#     if request.method == "POST":
#         response = requests.put(
#             f"http://{backend_host}/update/band/{id}",
#             json={"description": form.description.data}
#         )
#         return redirect(url_for('home'))

# @app.route('/update/agent/<int:id>', methods=['GET','POST'])
# def update_agent(id):
#     form = AgentForm()
#     task = requests.get(f"http://{backend_host}/read/task/{id}").json()
#     app.logger.info(f"Task: {task}")

#     if request.method == "POST":
#         response = requests.put(
#             f"http://{backend_host}/update/task/{id}",
#             json={"description": form.description.data}
#         )
#         return redirect(url_for('home'))



# @app.route('/delete/band/<int:id>')
# def delete_band(id):
#     response = requests.delete(f"http://{backend_host}/delete/band/{id}")
#     app.logger.info(f"Response: {response.text}")
#     return redirect(url_for('home'))