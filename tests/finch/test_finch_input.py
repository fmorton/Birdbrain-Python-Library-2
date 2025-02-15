import pytest
import time

from birdbrain_constant import BirdbrainConstant
from birdbrain_exception import BirdbrainException
from birdbrain_finch import BirdbrainFinch
from birdbrain_finch_input import BirdbrainFinchInput
from birdbrain_finch_output import BirdbrainFinchOutput
from birdbrain_request import BirdbrainRequest

def test_is_moving():
    assert BirdbrainFinchOutput.move("B", BirdbrainConstant.FORWARD, 7, 5, False)
    assert BirdbrainFinchInput.is_moving("B")

    BirdbrainFinchOutput.wait("B")

    assert BirdbrainFinchOutput.move("B", BirdbrainConstant.BACKWARD, 7, 5, True)

    assert BirdbrainRequest.stop_all("B")

    assert not BirdbrainFinchInput.is_moving("B")

def test_light():
    response = BirdbrainFinchInput.light("B", "L")

    assert (0 <= response <= 100)
    assert isinstance(response, int)

    response = BirdbrainFinchInput.light("B", "R")

    assert (0 <= response <= 100)
    assert isinstance(response, int)

    with pytest.raises(BirdbrainException) as e:
        BirdbrainFinchInput.light("B", "BAD")
    assert e.value.message == "Error: Request to device failed"

