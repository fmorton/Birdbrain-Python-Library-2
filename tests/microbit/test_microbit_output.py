from birdbrain_device import BirdbrainDevice
from birdbrain_exception import BirdbrainException
from birdbrain_microbit import BirdbrainMicrobit
from birdbrain_microbit_output import BirdbrainMicrobitOutput
from birdbrain_request import BirdbrainRequest
from birdbrain_state import BirdbrainState

import pytest
import time

def test_microbit_display():
    state = BirdbrainState()

    BirdbrainMicrobitOutput.microbit_display(state, "A", [ 0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0 ])

    time.sleep(0.5)

    BirdbrainRequest.stop_all("A")

def test_microbit_display_wrong_size():
    with pytest.raises(BirdbrainException) as e:
        state = BirdbrainState()

        list = [ 0,1 ]

        BirdbrainMicrobitOutput.microbit_display(state, "A", list)
    assert e.value.message == "Error: microbit_display() requires a list of length 25"
