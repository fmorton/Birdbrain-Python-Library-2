from birdbrain_exception import BirdbrainException
from birdbrain_microbit import BirdbrainMicrobit
from birdbrain_state import BirdbrainState

import pytest

def test_connect_device_name_as_none():
    with pytest.raises(BirdbrainException) as e:
        microbit = BirdbrainMicrobit.connect(None)
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

def test_state():
    state = BirdbrainState()

    for pixel in state.microbit_display_map:
        assert pixel == 0

    assert state.microbit_display_map[0] == 0
    assert state.microbit_display_map[18] == 0

    state.set_pixel(1, 1, 1)
    state.set_pixel(4, 4, 1)
    
    assert state.microbit_display_map[0] == 1
    assert state.microbit_display_map[18] == 1
    assert state.microbit_display_map[1] == 0
    assert state.microbit_display_map[19] == 0

    s = state.microbit_display_map_as_strings()

    assert s[0] == "true"
    assert s[18] == "true"
    assert s[1] == "false"
    assert s[19] == "false"
