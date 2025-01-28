from birdbrain_exception import BirdbrainException
from birdbrain_request import BirdbrainRequest
from birdbrain_utility import BirdbrainUtility

import pytest

def test_request_uri():
    uri = BirdbrainRequest.uri(["in", "1", "2", "3", "4", [ "99", 99 ], "something"])

    assert uri == "http://127.0.0.1:30061/hummingbird/in/1/2/3/4/99/99/something"
    
def test_response_with_false_arg():
    assert not BirdbrainRequest.response("1", "false", "2")

def test_response():
    response = BirdbrainRequest.response("in", "orientation", "Shake", "A")

def test_response_no_connection():
    with pytest.raises(BirdbrainException) as e:
        response = BirdbrainRequest.response("in", "orientation", "Shake", "C")

    assert e.value.message == "Error: The device is not connected"
 
    