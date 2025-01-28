from birdbrain_device import BirdbrainDevice
from birdbrain_exception import BirdbrainException

import pytest

def test_none_device():
    with pytest.raises(BirdbrainException) as e:
        hummingbird = BirdbrainDevice.connect(None)
    assert e.value.message == "Missing device name"

def test_bad_device():
    with pytest.raises(BirdbrainException) as e:
        hummingbird = BirdbrainDevice.connect("Z")
    assert e.value.message == "Invalid device name: Z"

def test_default_connect():
    hummingbird = BirdbrainDevice.connect()

    assert hummingbird.connected
    assert hummingbird.device == 'A'

def test_connect():
    hummingbird = BirdbrainDevice.connect("A")

    assert hummingbird.connected
    assert hummingbird.device == 'A'

def test_connect_to_disconnected_device():
    hummingbird = BirdbrainDevice.connect("C")

    assert not hummingbird.connected
    assert hummingbird.device == 'C'

def test_connect_to_disconnected_device_no_exception():
    hummingbird = BirdbrainDevice.connect("C", False)

    assert not hummingbird.connected
    assert hummingbird.device == 'C'

def test_connect_to_disconnected_device_with_exception():
    with pytest.raises(BirdbrainException) as e:
        hummingbird = BirdbrainDevice.connect("C", True)
    assert e.value.message == "No connection: C"
