import pytest
import logging
from flask.testing import FlaskClient

from app import create_app
from src.account.repository import InMemoryAccountRepository

logger = logging.getLogger(__name__)

@pytest.fixture
def client() -> FlaskClient:
    repo = InMemoryAccountRepository.build()
    return create_app(repo).test_client()

def test_get_balance(client: FlaskClient):
    expected = {}

    response = client.get('/')

    assert response.get_json() == expected

def test_list_transactions(client: FlaskClient):
    expected = [] 

    response = client.get('/transactions')

    assert response.get_json() == expected

def test_credit_transaction(client: FlaskClient):
    expected = ['id' , 'type' , 'amount', 'effectiveDate'] 

    response = client.post('/transactions', json={
        'amount': 100,
        'type': 'credit'
    })

    keys =  response.get_json().keys() 
    assert all([key in keys for key in expected])

def test_debit_without_balance(client: FlaskClient):
    expected = ['error'] 

    response = client.post('/transactions', json={
        'amount': 600,
        'type': 'debit'
    })

    keys =  response.get_json().keys() 
    assert all([key in keys for key in expected])
    assert response.status == "400 BAD REQUEST"

def test_find_transaction(client):
    expected = ['id' , 'type' , 'amount', 'effectiveDate'] 
    response = client.post('/transactions', json={
        'amount': 100,
        'type': 'credit'
    })
    transaction = response.get_json()

    path = f'transactions/{transaction.get("id")}'
    response = client.get(path)
    keys =  response.get_json().keys() 
    assert all([key in keys for key in expected])
