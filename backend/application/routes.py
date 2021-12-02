from application import app, db
from application.models import Band, Agent
from flask import request, jsonify

@app.route('/create/agent', methods=["POST"])
def create_agent():
    package = request.json
    new_agent = Agent(
        name=package["name"], 
        phone=package["phone"]
    )
    db.session.add(new_agent)
    db.session.commit()
    return f"Added agent: '{new_agent.name}' to database"

@app.route('/create/band/<int:agent_id>', methods=['POST'])
def create_band(agent_id):
    package = request.json
    new_band = Band(
        name=package["name"],
        phone=package["phone"],
        signed=package["signed"],
        agent_id = agent_id
    )
    db.session.add(new_band)
    db.session.commit()
    return f"Added band: {new_band.name}"

@app.route('/read/allAgents', methods=['GET'])
def read_agents():
    all_agents = Agent.query.all()
    package = {"agents": []}
    for agent in all_agents:
        bands = []
        for band in agent.bands:
            bands.append(
                {
                    "id": band.id,
                    "name": band.name,
                    "agent_id": band.agent_id,
                    "phone": band.phone
                }
            )
        package["agents"].append(
            {
                "id": agent.id,
                "name": agent.name,
                "phone": agent.phone,
                "bands": bands
            }
        )
    return jsonify(package)

@app.route('/read/allBands', methods=['GET'])
def read_bands():
    all_bands = Bands.query.all()
    bands_dict = {"bands": []}
    for band in all_bands:
        bands_dict["bands"].append(
            {
                "id": Band.id,
                "name": Band.name,
                "phone": Band.phone,
                "signed": band.signed
            }
        )
    return jsonify(bands_dict)

@app.route('/read/band/<int:id>', methods=['GET'])
def read_band(id):
    band = Band.query.get(id)
    bands_dict = {
        "id": Band.id,
        "name": Band.name,
        "phone": Band.phone,
        "signed": Band.signed
        }
    return jsonify(bands_dict)

@app.route('/read/agent/<int:id>', methods=['GET'])
def read_agent(id):
    agent = Agent.query.get(id)
    agents_dict = {
        "id": agent.id,
        "name": agent.name,
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
    return f"Updated agent (ID: {id}) with name: {agent.name}, phone number {agent.phone}"

@app.route('/update/band/<int:id>', methods=['PUT'])
def update_band(id):
    package = request.json
    bands = Band.query.get(id)
    bands.name = package["name"]
    bands.phone = package["phone"]
    db.session.commit()
    return f"Updated bands (ID: {id}) with name: {bands.name}, phone number {bands.phone}"

@app.route('/delete/band/<int:id>', methods=['DELETE'])
def delete_band(id):
    band = Band.query.get(id)
    db.session.delete(band)
    db.session.commit()
    return Response(f"Band with ID: {id} now signed", mimetype='text/plain')
