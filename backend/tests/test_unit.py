from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Tasks

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

<<<<<<< HEAD
    def test_read_home_tasks(self):
        response = self.client.get(url_for('home'))
        self.assertIn(b"Run unit tests", response.data)
    
    def test_read_tasks_dictionary(self):
        response = self.client.get(url_for('read_tasks'))
        self.assertIn(b"Run unit tests", response.data)
=======
    def test_read_all_bands(self):
        response = self.client.get(url_for('read_bands'))
        all_bands = { "bands": [test_band] }
        self.assertEquals(all_bands, response.json)
    
    def test_read_band(self):
        response = self.client.get(url_for('read_band', id=1))
        self.assertEquals(test_band, response.json)
>>>>>>> feature/3-extend-table-objects

class TestCreate(TestBase):

    def test_create_task(self):
        response = self.client.post(
            url_for('create_task'),
            data={"description": "Testing create functionality"},
            follow_redirects=True
        )
        self.assertIn(b"Testing create functionality", response.data)
    
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
