from application import app, db
from application.models import Bands, Agent
from flask import render_template, request, redirect, url_for, Response, jsonify

@app.route('/create/agent', methods=['POST'])
def create_agent():
    package = request.json
    new_agent = Agent(agent_name=package["agent_name"], phone=package["phone"])
    db.session.add(new_agent)
    db.session.commit()
    return Response(f"Added agent: {new_agent.name}", mimetype='text/plain')

@app.route('/create/band', methods=['POST'])
def create_band():
    package = request.json
    new_band = Bands(name=package["name"], phone=package["phone"], signed=package["signed"])
    db.session.add(new_band)
    db.session.commit()
    return Response(f"Added band: {new_band.name}", mimetype='text/plain')

@app.route('/read/allAgents', methods=['GET'])
def read_agents():
    all_agents = Agent.query.all()
    agents_dict = {"agents": []}
    for agent in all_agents:
        agents_dict["agents"].append(
            {
                "id": agent.id,
                "name": agent.agent_name,
                "phone": agent.phone
            }
        )
    return jsonify(bands_dict)

@app.route('/read/allBands', methods=['GET'])
def read_bands():
    all_bands = Bands.query.all()
    bands_dict = {"bands": []}
    for band in all_bands:
        bands_dict["bands"].append(
            {
                "id": bands.id,
                "name": bands.name,
                "phone": bands.phone,
                "signed": band.signed
            }
        )
    return jsonify(bands_dict)

@app.route('/read/band/<int:id>', methods=['GET'])
def read_band(id):
    band = Bands.query.get(id)
    bands_dict = {
        "id": bands.id,
        "name": bands.name,
        "phone": bands.phone,
        "signed": bands.signed
        }
    return jsonify(bands_dict)

@app.route('/read/agent/<int:id>', methods=['GET'])
def read_agent(id):
    agent = Agent.query.get(id)
    agents_dict = {
        "id": agent.id,
        "name": agent.agent_name,
        "phone": agent.phone
        }
    return jsonify(agents_dict)

@app.route('/update/agent/<int:id>', methods=['PUT'])
def update_agent(id):
    package = request.json
    agent = Agent.query.get(id)
    agent.name = package["name"]
    agent.phone = package["phone"]
    db.session.commit()
    return Response(f"Updated agent (ID: {id}) with name: {agent.name}, phone number {agent.phone}", mimetype='text/plain')

@app.route('/update/band/<int:id>', methods=['PUT'])
def update_band(id):
    package = request.json
    bands = Bands.query.get(id)
    bands.name = package["name"]
    bands.phone = package["phone"]
    db.session.commit()
    return Response(f"Updated bands (ID: {id}) with name: {bands.name}, phone number {bands.phone}", mimetype='text/plain')

@app.route('/delete/band/<int:id>', methods=['DELETE'])
def delete_band(id):
    band = Bands.query.get(id)
    db.session.delete(band)
    db.session.commit()
    return Response(f"Band with ID: {id} now signed", mimetype='text/plain')
    