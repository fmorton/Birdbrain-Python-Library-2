import pytest
import time

from birdbrain_exception import BirdbrainException
from birdbrain_finch import BirdbrainFinch
from birdbrain_finch_output import BirdbrainFinchOutput

def test_beak():
    finch = BirdbrainFinch("B")
    
    assert BirdbrainFinchOutput.beak(finch.device, 10, 50, 50)
    time.sleep(0.5)
    assert BirdbrainFinchOutput.beak(finch.device, 0, 0, 0)

def test_tail():
    finch = BirdbrainFinch("B")
    
    assert BirdbrainFinchOutput.tail(finch.device, 1, 10, 50, 50)
    time.sleep(0.5)
    assert BirdbrainFinchOutput.tail(finch.device, 1, "0", 50, "0")
    time.sleep(0.5)
    assert BirdbrainFinchOutput.tail(finch.device, "2", "0", 50, "0")
    time.sleep(0.5)
    assert BirdbrainFinchOutput.tail(finch.device, 3, "0", 50, "0")
    time.sleep(0.5)
    assert BirdbrainFinchOutput.tail(finch.device, 4, "0", 50, "0")
    time.sleep(0.5)
    assert BirdbrainFinchOutput.tail(finch.device, "all", 0, 0, 100)
    time.sleep(0.5)
    assert BirdbrainFinchOutput.tail(finch.device, "all", 0, 0, 0)
