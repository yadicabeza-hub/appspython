import pytest
import os
import sys

# Agregar ruta para que los imports funcionen
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from run import create_app
from database import db
from models import Phase, Project

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_phase_creation(app):
    with app.app_context():
        phase = Phase(name="Testing Phase", description="A phase for testing", order=1)
        db.session.add(phase)
        db.session.commit()
        
        saved_phase = Phase.query.first()
        assert saved_phase.name == "Testing Phase"
        assert saved_phase.order == 1

def test_project_creation(app):
    with app.app_context():
        # First create a phase
        phase = Phase(name="Init", description="Desc", order=1)
        db.session.add(phase)
        db.session.commit()
        
        # Then create project
        proj = Project(name="Test Project", description="Test Desc", current_phase_id=phase.id)
        db.session.add(proj)
        db.session.commit()
        
        saved_proj = Project.query.first()
        assert saved_proj.name == "Test Project"
        assert saved_proj.phase.name == "Init"
