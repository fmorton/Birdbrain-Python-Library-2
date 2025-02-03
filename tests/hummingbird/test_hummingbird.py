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

def test_led_with_alias():
    hummingbird = BirdbrainHummingbird("A")

    assert hummingbird.led(1, 100)
    time.sleep(0.25)

    assert hummingbird.led(1, 0)
    time.sleep(0.25)

    assert hummingbird.led(1, 50)
    time.sleep(0.25)

    hummingbird.setLED(1, 0)

def test_led_no_connection():
    with pytest.raises(BirdbrainException) as e:
        hummingbird = BirdbrainHummingbird('C')

        hummingbird.led(1, 100)
    assert e.value.message == "No connection: C"

def test_tri_led_with_alias():
    hummingbird = BirdbrainHummingbird("A")

    assert hummingbird.tri_led(1, 50, "50", 0)
    time.sleep(0.25)

    assert hummingbird.setTriLED(1, 100, "0", "0")
    time.sleep(0.25)

    assert hummingbird.tri_led(1, 0, "0", "0")
    time.sleep(0.25)

def test_position_servo_with_alias():
    hummingbird = BirdbrainHummingbird("A")

    assert hummingbird.position_servo(1, 50)
    time.sleep(0.5)

    assert hummingbird.setPositionServo(1, "130")

def test_rotation_servo_with_alias():
    hummingbird = BirdbrainHummingbird("A")

    assert hummingbird.rotation_servo(2, 50)
    time.sleep(0.25)

    assert hummingbird.setRotationServo(2, "-50")
    time.sleep(0.25)

    assert hummingbird.rotation_servo(2, 100)
    time.sleep(0.25)

    assert hummingbird.setRotationServo(2, -100)
    time.sleep(0.25)

    assert hummingbird.setRotationServo(2, 0)
