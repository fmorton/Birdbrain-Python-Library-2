import pytest
import time

from birdbrain_exception import BirdbrainException
from birdbrain_microbit import BirdbrainMicrobit
from BirdBrain import BirdbrainHummingbird

def test_connect_device_name_as_none():
    with pytest.raises(BirdbrainException) as e:
        hummingbird = BirdbrainHummingbird.connect(None)
    assert e.value.message == "Missing device name"

def test_connect_bad_device_name():
    with pytest.raises(BirdbrainException) as e:
        hummingbird = BirdbrainHummingbird.connect('D')
    assert e.value.message == "Invalid device name: D"

def test_connect_valid_device_name():
    hummingbird = BirdbrainHummingbird.connect("A")

    assert hummingbird.device == "A"

def test_is():
    microbit = BirdbrainMicrobit.connect("A")

    assert not microbit.is_microbit()
    assert microbit.is_hummingbird()
    assert not microbit.is_finch()

#def test_blink():
#    bird = BirdbrainHummingbird('A')
#
#    for i in range(0, 2):
#        bird.setLED(1, 100)
#        time.sleep(0.1)
#        bird.setLED(1, 0)
#        time.sleep(0.1)
#
#    bird.stopAll()
