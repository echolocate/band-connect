from application import app, db
from application.models import Bands, Agent
from flask import render_template, request, redirect, url_for, Response, jsonify

@app.route('/create/agent', methods=['POST'])
def create_agent():
    package = request.json
    new_agent = Agent(agent_name=package["agent_name"], Agent(phone=package["phone"]))
    db.session.add(new_agent)
    db.session.commit()
    return Response(f"Added agent: {new_agent.name}", mimetype='text/plain')

@app.route('/create/band', methods=['POST'])
def create_band():
    package = request.json
    new_band = Bands(name=package["name"], Bands(phone=package["phone"]))
    db.session.add(new_band)
    db.session.commit()
    return Response(f"Added band: {new_band.name}", mimetype='text/plain')

@app.route('/read/allBands', methods=['GET'])
def read_bands():
    all_bands = Bands.query.all()
    bands_dict = {"bands": []}
    for band in all_bands:
        tasks_dict["bands"].append(
            {
                "id": bands.id,
                "bandname": bands.name,
                #"signed": band.signed
            }
        )
    return jsonify(bands_dict)

@app.route('/read/allAgents', methods=['GET'])
def read_agents():
    all_agents = Agent.query.all()
    agent_dict = {"agent": []}
    for agent in all_agents:
        tasks_dict["agent"].append(
            {
                "id": agent.id,
                "agentname": agent_name.name,
                #"signed": band.signed
            }
        )
    return jsonify(agent_dict)

@app.route('/delete/band/<int:id>', methods=['DELETE'])
def delete_band(id):
    band = Bands.query.get(id)
    db.session.delete(band)
    db.session.commit()
    return Response(f"Band with ID: {id} signed and removed", mimetype='text/plain')
