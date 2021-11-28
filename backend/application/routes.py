from application import app, db
from application.models import Bands
from flask import render_template, request, redirect, url_for, Response, jsonify

@app.route('/create/band', methods=['POST'])
def create_band():
    package = request.json
    new_band = Band(band_name=package["band_name"])
    db.session.add(new_band)
    db.session.commit()
    return Response(f"Added band: {new_band.description}", mimetype='text/plain')

@app.route('/read/allBands', methods=['GET'])
def read_bands():
    all_bands = Bands.query.all()
    bands_dict = {"bands": []}
    for band in all_bands:
        tasks_dict["bands"].append(
            {
                "id": task.id,
                "bandname": band.name,
                #"signed": band.signed
            }
        )
    return jsonify(bands_dict)