from birdbrain_constant import BirdbrainConstant
from birdbrain_exception import BirdbrainException
from BirdBrain import BirdbrainFinch

import pytest
import time

def test_is():
    finch = BirdbrainFinch.connect("B")

    assert finch.is_connected()
    assert not finch.is_microbit()
    assert not finch.is_hummingbird()
    assert finch.is_finch()

def test_beak_with_alias():
    finch = BirdbrainFinch('B')

    finch.beak(100, 50, 50)
    time.sleep(0.25)
    finch.setBeak(0, 0, 0)

def test_tail_with_alias():
    finch = BirdbrainFinch("B")

    assert finch.tail(1, 10, 0, 50)
    time.sleep(0.1)
    assert finch.tail(1, "50", 0, "0")
    time.sleep(0.1)
    assert finch.tail("2", "50", 0, "0")
    time.sleep(0.1)
    assert finch.tail(3, "50", 0, "0")
    time.sleep(0.1)
    assert finch.tail(4, "50", 0, "0")
    time.sleep(0.1)
    assert finch.tail("all", 100, 0, 100)
    time.sleep(0.1)
    assert finch.setTail("all", 0, 0, 0)

def test_move_with_alias():
    finch = BirdbrainFinch("B")

    assert finch.move(BirdbrainConstant.FORWARD, 4, 20)
    assert finch.move(BirdbrainConstant.FORWARD, "4", "20")
    assert finch.move(BirdbrainConstant.BACKWARD, 4, 20)
    assert finch.setMove(BirdbrainConstant.BACKWARD, "4", "20")

    with pytest.raises(BirdbrainException) as e:
        finch = BirdbrainFinch("B")

        assert finch.move(None, 4, 20)
        assert e.value.message == "Error: Request to device failed"

    with pytest.raises(BirdbrainException) as e:
        finch = BirdbrainFinch("B")

        assert finch.move("BAD", 4, 20)
    assert e.value.message == "Error: Request to device failed"

def test_is_moving():
    finch = BirdbrainFinch("B")

    assert finch.move(BirdbrainConstant.FORWARD, 4, 5)
    assert finch.is_moving()

    finch.stop_all()

    time.sleep(1)

    assert not finch.is_moving()

def test_turn_with_alias():
    finch = BirdbrainFinch("B")

    finch.turn("L", 45, 50)
    finch.turn("R", 45, 50)
    finch.turn("L", "45", 50)
    finch.setTurn("R", 45, "50")
