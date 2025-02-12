from birdbrain_exception import BirdbrainException
from birdbrain_hummingbird import BirdbrainHummingbird
from birdbrain_microbit import BirdbrainMicrobit
from birdbrain_state import BirdbrainState

import pytest
import time
import random

def test_connect_device_name_as_none():
    with pytest.raises(BirdbrainException) as e:
        microbit = BirdbrainMicrobit(None)
    assert e.value.message == "Missing device name"

def test_connect_bad_device_name():
    with pytest.raises(BirdbrainException) as e:
        microbit = BirdbrainMicrobit.connect('D')
    assert e.value.message == "Invalid device name: D"

def test_connect_valid_device_name():
    microbit = BirdbrainMicrobit.connect("A")

    assert microbit.device == "A"

def test_is():
    microbit = BirdbrainMicrobit.connect("A")

    assert microbit.is_connected()
    assert not microbit.is_microbit()
    assert microbit.is_hummingbird()
    assert not microbit.is_finch()

def test_microbit_display_with_alias():
    hummingbird = BirdbrainHummingbird("A")

    assert hummingbird.microbit_display([ 1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1 ])

    time.sleep(0.5)

    assert hummingbird.setDisplay([ 0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0 ])

    time.sleep(0.5)

    hummingbird.stop_all()

def test_microbit_display_wrong_size():
    with pytest.raises(BirdbrainException) as e:
        hummingbird = BirdbrainHummingbird("A")

        hummingbird.microbit_display([ 0,1 ])
    assert e.value.message == "Error: microbit_display() requires a list of length 25"
