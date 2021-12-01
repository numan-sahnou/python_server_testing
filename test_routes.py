import pytest
import time
from handlers.routes import configure_routes
from flask import Flask

def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.get_data() == b'Assignment Numan SAHNOU'
    assert response.status_code == 200

def test_correct_mean():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/mean?list=1&list=2&list=3&list=4'
    
    response = client.get(url)
    assert response.get_data() == b'Mean of the list : 2.5'

def test_stress_requests():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/mean?list=1&list=2&list=3&list=4'
    
    start = time.time()
    for i in range(1000):
        client.get(url)
    
    end = time.time()-start
    assert (end/1000) < 100
