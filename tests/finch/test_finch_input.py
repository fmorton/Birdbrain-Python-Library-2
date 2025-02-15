from birdbrain_constant import BirdbrainConstant
from birdbrain_finch import BirdbrainFinch
from birdbrain_finch_input import BirdbrainFinchInput
from birdbrain_finch_output import BirdbrainFinchOutput
from birdbrain_request import BirdbrainRequest

import time

def test_is_moving():
    assert BirdbrainFinchOutput.move("B", BirdbrainConstant.FORWARD, 7, 5, False)
    assert BirdbrainFinchInput.is_moving("B")

    BirdbrainFinchOutput.wait("B")

    assert BirdbrainFinchOutput.move("B", BirdbrainConstant.BACKWARD, 7, 5, True)

    assert BirdbrainRequest.stop_all("B")

    assert not BirdbrainFinchInput.is_moving("B")

