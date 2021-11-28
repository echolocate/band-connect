from application import app
from application.forms import BandForm
from flask import render_template, request, redirect, url_for, jsonify
import requests

backend_host = "bc-app_backend:5000"

@app.route('/')
@app.route('/home')
def home():
    all_bands = requests.get(f"http://{backend_host}/read/allBands").json()
    return render_template('index.html', title="Home", all_bands=all_bands["bands"])

@app.route('/create/band', methods=['GET','POST'])
def create_band():
    form = BandForm()

    if request.method == "POST":
        response = requests.post(
            f"http://{backend_host}/create/band",
            json={"name": form.name.data}
        )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for('home'))

@app.route('/delete/band/<int:id>')
def delete_band(id):
    response = requests.delete(f"http://{backend_host}/delete/band/{id}")
    app.logger.info(f"Response: {response.text}")
    return redirect(url_for('home'))