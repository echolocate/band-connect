from application import db

class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    agent_name = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.Integer(20), nullable=False)
    bands = db.relationship('Band', backref='agentbr')
    
class Bands(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    # signed = db.Column(db.Boolean, nullable=False, default=False)
    agent_id = db.Column(db.Integer, db.ForeignKey('agent.id'), nullable=False)


