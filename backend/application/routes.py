from application import app, db
from application.models import Band, Agent
from flask import request, jsonify

@app.route('/read/allBands', methods=['GET'])
def read_bands():
    all_bands = Band.query.all()
    bands_dict = {"bands": []}
    for band in all_bands:
        bands_dict["bands"].append(
            {
                "id": band.id,
                "name": band.name,
                "phone": band.phone,
                "genre": band.genre,
                "members": band.members,
                "signed": band.signed
            }
        )
    return jsonify(bands_dict)

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

@app.route('/create/band', methods=['POST'])
def create_band():
    package = request.json
    new_band = Band(
        name=package["name"],
        phone=package["phone"],
        genre = package["genre"],
        members = package["members"],
        signed=package["signed"]
    )
    db.session.add(new_band)
    db.session.commit()
    return f"Added band: '{new_band.name}'"

@app.route('/delete/band/<int:id>', methods=['DELETE'])
def delete_band(id):
    band = Band.query.get(id)
    db.session.delete(band)
    db.session.commit()
    return f"Band with ID: {id} now deleted"

# @app.route('/sign/band/<int:agent_id>/<int:band_id>', methods=['PUT'])
# def sign_band(agent_id,band_id):
#     band = Band.query.get(band_id)
#     agent = Agent.query.get(agent_id)
#     band.signed = True
#     db.session.commit()
#     return Response(f"Band with ID: {id} signed", mimetype='text/plain')

# @app.route('/read/allAgents', methods=['GET'])
# def read_agents():
#     all_agents = Agent.query.all()
#     package = {"agents": []}
#     for agent in all_agents:
#         for band in agent.bands:
#             bands.append(
#                 {
#                     "id": band.id,
#                     "name": band.name,
#                     "agent_id": band.agent_id,
#                     "phone": band.phone
#                 }
#             )
#         package["agents"].append(
#             {
#                 "id": agent.id,
#                 "name": agent.name,
#                 "phone": agent.phone,
#                 "bands": bands
#             }
#         )
#     return jsonify(package)



# @app.route('/read/band/<int:id>', methods=['GET'])
# def read_band(id):
#     band = Band.query.get(id)
#     bands_dict = 
#             {
#                   "id": band.id,
#                   "name": band.name,"phone": band.phone,
#                   "signed": band.signed
#             }
#     return jsonify(bands_dict)

# @app.route('/read/agent/<int:id>', methods=['GET'])
# def read_agent(id):
#     agent = Agent.query.get(id)
#     agents_dict = {
#         "id": agent.id,
#         "name": agent.name,
#         "phone": agent.phone
#         }
#     return jsonify(agents_dict)

# @app.route('/update/agent/<int:id>', methods=['PUT'])
# def update_agent(id):
#     package = request.json
#     agent = Agent.query.get(id)
#     agent.name = package["name"]
#     agent.phone = package["phone"]
#     db.session.commit()
#     return f"Updated agent (ID: {id}) with name: {agent.name}, phone number {agent.phone}"

# @app.route('/update/band/<int:id>', methods=['PUT'])
# def update_band(id):
#     package = request.json
#     bands = Band.query.get(id)
#     bands.name = package["name"]
#     bands.phone = package["phone"]
#     db.session.commit()
#     return f"Updated bands (ID: {id}) with name: {bands.name}, phone number {bands.phone}"

# @app.route('/delete/band/<int:id>', methods=['DELETE'])
# def delete_band(id):
#     band = Band.query.get(id)
#     db.session.delete(band)
#     db.session.commit()
#     return Response(f"Band with ID: {id} now signed", mimetype='text/plain')
