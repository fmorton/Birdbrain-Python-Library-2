import pytest

from birdbrain_exception import BirdbrainException
from birdbrain_finch import BirdbrainFinch
from birdbrain_hummingbird import BirdbrainHummingbird

def helper_test_shared(device):
    response = device.acceleration()
    response = device.getAcceleration()

    assert (-100.0 <= response[0] <= 100.0)
    assert (-100.0 <= response[1] <= 100.0)
    assert (-100.0 <= response[2] <= 100.0)

    assert isinstance(response[0], float)
    assert isinstance(response[1], float)
    assert isinstance(response[2], float)


    response = device.compass()
    response = device.getCompass()

    assert (0 <= response <= 359)
    assert isinstance(response, int)


    response = device.magnetometer()
    response = device.getMagnetometer()

    assert (-100 <= response[0] <= 100)
    assert (-100 <= response[1] <= 100)
    assert (-100 <= response[2] <= 100)

    assert isinstance(response[0], int)
    assert isinstance(response[1], int)
    assert isinstance(response[2], int)


    assert not device.button("A")
    assert not device.button("B")
    assert not device.button("LOGO")
    assert not device.button("Logo")
    assert not device.getButton("logo")

    with pytest.raises(BirdbrainException) as e:
        device.button("BAD")
    assert e.value.message == "Error: Request to device failed"

def test_shared():
    helper_test_shared(BirdbrainHummingbird("A"))
    helper_test_shared(BirdbrainFinch("B"))
