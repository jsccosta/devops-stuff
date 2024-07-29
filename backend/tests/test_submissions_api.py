import pytest
from app.api import submissions
from app.main import app

import os

current_dir = os.path.dirname(os.path.abspath(__file__))
test_pdf = os.path.join(current_dir, 'files', 'v1-doc.pdf')

@pytest.fixture  
def client():  
    with app.test_client() as client:  
        yield client 
        
@pytest.fixture  
def json_headers():  
    return {"Content-Type": "application/json"} 

json_data = {
    "account_name": 'Test Account',
    "underwriter": "Test Underwriter",
    "domicile": "Test Domicile",
    "broker": "Test Broker",
    "files": test_pdf,
    "files": test_pdf,
    "files": test_pdf
}

def test_add(client, json_headers, json_data):  
    response = client.post("/api/v1/submissions", headers=json_headers, json=json_data)  
    assert response.status_code == 200  
    # assert response.json == 3  