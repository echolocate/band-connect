from application import db

class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    band = db.relationship('Bands', backref='agent')
    
class Bands(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable = False)
    signed = db.Column(db.Boolean, nullable=False, default=False)
    agent_id = db.Column(db.Integer, db.ForeignKey('agent.id'), nullable=False)


