from birdbrain_exception import BirdbrainException
from birdbrain_request import BirdbrainRequest
from birdbrain_utility import BirdbrainUtility

import pytest

def test_request_uri():
    uri = BirdbrainRequest.uri(["in", "1", "2", "3", "4", [ "99", 99 ], "something"])

    assert uri == "http://127.0.0.1:30061/in/1/2/3/4/99/99/something"

def test_connected():
    assert BirdbrainRequest.is_connected("A")

def test_not_connected():
    assert not BirdbrainRequest.is_connected("C")

def test_not_connected_connected():
    assert not BirdbrainRequest.is_not_connected("A")

def test_not_connected_not_connected():
    assert BirdbrainRequest.is_not_connected("C")

def test_response_with_false_arg():
    assert not BirdbrainRequest.response("1", "false", "2")

def test_response():
    response = BirdbrainRequest.response("hummingbird", "in", "orientation", "Shake", "A")

def test_response_no_connection():
    with pytest.raises(BirdbrainException) as e:
        response = BirdbrainRequest.response("hummingbird", "in", "orientation", "Shake", "C")

    assert e.value.message == "Error: The device is not connected"

def test_disconnect():
    response = BirdbrainRequest.disconnect("A")

    assert response == 'all stopped'

def test_disconnect():
    with pytest.raises(BirdbrainException) as e:
        BirdbrainRequest.disconnect("C")

    assert e.value.message == "Error: The device is not connected"
