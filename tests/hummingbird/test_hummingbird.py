import pytest
import time

from birdbrain_exception import BirdbrainException
from birdbrain_microbit import BirdbrainMicrobit
from BirdBrain import BirdbrainHummingbird

def test_connect_device_name_as_none():
    with pytest.raises(BirdbrainException) as e:
        hummingbird = BirdbrainHummingbird(None)
    assert e.value.message == "Missing device name"

def test_connect_bad_device_name():
    with pytest.raises(BirdbrainException) as e:
        hummingbird = BirdbrainHummingbird('D')
    assert e.value.message == "Invalid device name: D"

def test_connect_valid_device_name():
    hummingbird = BirdbrainHummingbird("A")

    assert hummingbird.device == "A"

def test_is():
    hummingbird = BirdbrainHummingbird("A")

    assert hummingbird.is_connected()
    assert not hummingbird.is_microbit()
    assert hummingbird.is_hummingbird()
    assert not hummingbird.is_finch()

def test_led():
    hummingbird = BirdbrainHummingbird("A")

    assert hummingbird.led(1, 100)
    time.sleep(0.25)

    assert hummingbird.led(1, 0)
    time.sleep(0.25)

    assert hummingbird.led(1, 50)
    time.sleep(0.25)

    hummingbird.led(1, 0)

def test_led_alias():
    hummingbird = BirdbrainHummingbird("A")

    assert hummingbird.setLED(1, 100)
    time.sleep(0.25)

    assert hummingbird.setLED(1, 0)

def test_led_no_connection():
    with pytest.raises(BirdbrainException) as e:
        hummingbird = BirdbrainHummingbird('C')
        #hummingbird.led(1, 100)
    assert e.value.message == "No connection: C"
