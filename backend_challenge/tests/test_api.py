import requests as rq
import pytest

# The URL will be used to try to connect to your API on a local network
# Theses are the ONLY two values you may need the change, the rest of the tests should not be touched.
URL = r'http://127.0.0.1'
PORT = 8000


calls = [
    '/coffee',
    '/coffee/?order=desc',
    '/coffee/2',
    '/post',
]
    
@pytest.mark.parametrize('test_input', ['/coffee/ping', '/post/ping'])
def test_ping(test_input):
    '''Calls to the ping route should return a {status: good}'''
    assert rq.get(f"{URL}:{PORT}{test_input}").json()['status'].lower() == 'good'
    
    
@pytest.mark.parametrize('test_input, expect', [(x, 200) for x in calls])
def test_status(test_input, expect):
    '''All Calls should return a 200 status'''
    assert rq.get(f"{URL}:{PORT}{test_input}").status_code == expect

    
def test_get_black_coffee():
    coffee = rq.get(f"{URL}:{PORT}/coffee/1").json()
    for k in coffee:
        coffee = coffee[k]
        break
    assert coffee['name'].lower() == 'black'
    