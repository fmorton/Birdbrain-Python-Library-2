import pytest

from birdbrain.constant import Constant
from birdbrain.exception import Exception
from birdbrain.hummingbird_input import HummingbirdInput


def test_acceleration():
    response = HummingbirdInput.acceleration("A")

    assert -100.0 <= response[0] <= 100.0
    assert -100.0 <= response[1] <= 100.0
    assert -100.0 <= response[2] <= 100.0

    assert isinstance(response[0], float)
    assert isinstance(response[1], float)
    assert isinstance(response[2], float)


def test_compass():
    response = HummingbirdInput.compass("A")

    assert 0 <= response <= 359
    assert isinstance(response, int)


def test_magnetometer():
    response = HummingbirdInput.magnetometer("A")

    assert -180.0 <= response[0] <= 180.0
    assert -180.0 <= response[1] <= 180.0
    assert -180.0 <= response[2] <= 180.0

    assert isinstance(response[0], int)
    assert isinstance(response[1], int)
    assert isinstance(response[2], int)


def test_orientation():
    response = HummingbirdInput.orientation("A")

    some_position = False
    for orientation in Constant.HUMMINGBIRD_ORIENTATION_RESULTS:
        some_position = some_position or (orientation == response)

    assert some_position


def test_sensor():
    response = HummingbirdInput.sensor("A", 1)

    assert isinstance(response, float)


def test_light():
    response = HummingbirdInput.light("A", 1)
    assert 0 <= response <= 100
    assert isinstance(response, int)


def test_sound():
    response = HummingbirdInput.sound("A", 1)
    assert 0 <= response <= 100
    assert isinstance(response, int)

    with pytest.raises(Exception) as e:
        response = HummingbirdInput.sound("A", 4)
    assert e.value.message == "Error: The device is not connected"


def test_sound_microbit():
    response = HummingbirdInput.sound("A", "micro:bit")

    assert 0 <= response <= 100
    assert isinstance(response, int)


def test_distance():
    response = HummingbirdInput.distance("A", 2)

    assert 0 <= response <= 298
    assert isinstance(response, int)


def test_dial():
    response = HummingbirdInput.dial("A", 1)

    assert 0 <= response <= 100
    assert isinstance(response, int)


def test_voltage():
    response = HummingbirdInput.voltage("A", 1)

    assert 0.0 <= response <= 3.3
    assert isinstance(response, float)
