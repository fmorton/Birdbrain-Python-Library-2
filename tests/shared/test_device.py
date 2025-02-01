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
    with pytest.raises(BirdbrainException) as e:
        hummingbird = BirdbrainDevice.connect("C", True)
    assert e.value.message == "No connection: C"

def test_connect_to_disconnected_device_no_exception():
    hummingbird = BirdbrainDevice.connect("C", False)

    assert not hummingbird.connected
    assert hummingbird.device == 'C'

def test_connect_to_disconnected_device_with_exception():
    with pytest.raises(BirdbrainException) as e:
        hummingbird = BirdbrainDevice.connect("C", True)
    assert e.value.message == "No connection: C"

def test_is_hummingbird():
    hummingbird = BirdbrainDevice.connect("A")

    assert hummingbird.is_hummingbird

def test_is_finch():
    hummingbird = BirdbrainDevice.connect("A")

    assert not hummingbird.is_finch()

def test_is_valid():
    hummingbird = BirdbrainDevice.connect("A")

    assert hummingbird.is_valid(1, "123")
    assert hummingbird.is_valid("1", "123")
    assert not hummingbird.is_valid(4, "123")
    assert not hummingbird.is_valid("4", "123")
    assert not hummingbird.is_valid(None, "123")

def test_is_connected_and_valid():
    hummingbird = BirdbrainDevice.connect("A")

    assert hummingbird.is_connected_and_valid(1, "123")
    assert hummingbird.is_connected_and_valid("1", "123")
    assert not hummingbird.is_connected_and_valid(4, "123")
    assert not hummingbird.is_connected_and_valid("4", "123")
    assert not hummingbird.is_connected_and_valid(None, "123")
