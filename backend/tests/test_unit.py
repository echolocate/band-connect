from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Agent, Bands

test_band={
    "id": 1,
    "name": "The Rutles",
    "phone": 123456789,
    "signed": False
    }
        
test_agent={
    "id": 1,
    "agent_name": "Leggy Mountbatten",
    "phone": 987654321
    }

class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        # Will be called before every test
        db.create_all()
        db.session.add(Tasks(description="Run unit tests"))
        db.session.commit()

    def tearDown(self):
        # Will be called after every test
        db.session.remove()
        db.drop_all()

class TestRead(TestBase):

    def test_read_all_agents(self):
        response = self.client.get(url_for('read_agents'))
        all_agents = { "agents": [test_agent] }
        self.assertEquals(all_agents, response.json)
    
    def test_read_agent(self):
        response = self.client.get(url_for('read_agent'))
        self.assertEquals(test_agent, response.json)

    def test_read_all_bands(self):
        response = self.client.get(url_for('read_bands'))
        all_bands = { "bands": [test_band] }
        self.assertEquals(all_bands, response.json)
    
    def test_read_band(self):
        response = self.client.get(url_for('read_band', id=1))
        self.assertEquals(test_band, response.json)

class TestCreate(TestBase):

    def test_create_agent(self):
        response = self.client.post(
            url_for('create_agent'),
            json={"agent_name": "Dick Jaws", "phone":"0123456789"},
            follow_redirects=True
        )
        self.assertEquals(b"Added agent: Dick Jaws", response.data)
        self.assertEquals(Agent.query.get(2).agent_name, "Dick Jaws")
    
class TestUpdate(TestBase):

    def test_update_task(self):
        response = self.client.post(
            url_for('update_task', id=1),
            data={"description": "Testing update functionality"},
            follow_redirects=True
        )
        self.assertIn(b"Testing update functionality", response.data)
    
    def test_complete_task(self):
        response = self.client.get(url_for('complete_task', id=1), follow_redirects=True)
        self.assertEqual(Tasks.query.get(1).completed, True)
    
    def test_incomplete_task(self):
        response = self.client.get(url_for('incomplete_task', id=1), follow_redirects=True)
        self.assertEqual(Tasks.query.get(1).completed, False)
        

class TestDelete(TestBase):

    def test_delete_task(self):
        response = self.client.get(
            url_for('delete_task', id=1),
            follow_redirects=True
        )
        self.assertNotIn(b"Run unit tests", response.data)
