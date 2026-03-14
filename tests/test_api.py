import pytest
import json
import sys
import os

# Add the backend directory to the path so we can import the app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend')))

from app import create_app

@pytest.fixture
def client():
    """A test client for the app."""
    app = create_app('testing')
    with app.test_client() as client:
        yield client

def test_health_route(client):
    """Test the /health endpoint."""
    rv = client.get('/health')
    assert rv.status_code == 200
    
    data = json.loads(rv.data)
    assert data['status'] == 'success'
    assert 'version' in data['data']

def test_process_route_success(client):
    """Test the /process endpoint with valid payload."""
    payload = {
        "url": "https://example.com/video/123"
    }
    rv = client.post('/process', json=payload)
    
    assert rv.status_code == 200
    data = json.loads(rv.data)
    
    assert data['status'] == 'success'
    assert data['data']['source_url'] == payload['url']
    assert data['data']['simulated'] == True

def test_process_route_missing_url(client):
    """Test the /process endpoint with missing url."""
    payload = {
        "format": "mp4"
    }
    rv = client.post('/process', json=payload)
    
    assert rv.status_code == 400
    data = json.loads(rv.data)
    
    assert data['status'] == 'error'
    assert 'URL is required' in data['message']
