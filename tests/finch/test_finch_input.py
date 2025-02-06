from birdbrain_constant import BirdbrainConstant
from birdbrain_finch import BirdbrainFinch
from birdbrain_finch_input import BirdbrainFinchInput
from birdbrain_finch_output import BirdbrainFinchOutput
from birdbrain_request import BirdbrainRequest

import time

def test_is_moving():
    assert BirdbrainFinchOutput.move("B", BirdbrainConstant.FORWARD, 4, 5)
    time.sleep(0.1)
    assert BirdbrainFinchInput.is_moving("B")

    assert BirdbrainRequest.stop_all("B")

    time.sleep(1)

    assert not BirdbrainFinchInput.is_moving("B")

