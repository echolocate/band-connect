from application import db

class Bands(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    # signed = db.Column(db.Boolean, nullable=False, default=False)
