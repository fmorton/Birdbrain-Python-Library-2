import pytest
import time

from birdbrain_exception import BirdbrainException
from birdbrain_hummingbird_input import BirdbrainHummingbirdInput

def test_acceleration():
    #response = BirdbrainHummingbirdInput.acceleration("A", "Accelerometer")
    response = BirdbrainHummingbirdInput.acceleration("A")

    assert (-100.0 <= response[0] <= 100.0)
    assert (-100.0 <= response[1] <= 100.0)
    assert (-100.0 <= response[2] <= 100.0)

    assert isinstance(response[0], float)
    assert isinstance(response[1], float)
    assert isinstance(response[2], float)

def test_compass():
    #response = BirdbrainHummingbirdInput.compass("A", "Compass")
    response = BirdbrainHummingbirdInput.compass("A")

    assert (0 <= response <= 359)
    assert isinstance(response, int)

def test_magnetometer():
    response = BirdbrainHummingbirdInput.magnetometer("A")

    assert (-180.0 <= response[0] <= 180.0)
    assert (-180.0 <= response[1] <= 180.0)
    assert (-180.0 <= response[2] <= 180.0)

    assert isinstance(response[0], int)
    assert isinstance(response[1], int)
    assert isinstance(response[2], int)

