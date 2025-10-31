import pytest
import time

from birdbrain.constant import Constant
from birdbrain.exception import Exception
from birdbrain.finch_output import FinchOutput
from birdbrain.request import Request


def test_beak():
    assert FinchOutput.beak("B", 10, 50, 50)
    time.sleep(0.15)
    assert FinchOutput.beak("B", 0, 0, 0)


def test_tail():
    assert FinchOutput.tail("B", 1, 10, 50, 50)
    time.sleep(0.1)
    assert FinchOutput.tail("B", 1, "0", 50, "0")
    time.sleep(0.1)
    assert FinchOutput.tail("B", "2", "0", 50, "0")
    time.sleep(0.1)
    assert FinchOutput.tail("B", 3, "0", 50, "0")
    time.sleep(0.1)
    assert FinchOutput.tail("B", 4, "0", 50, "0")
    time.sleep(0.1)
    assert FinchOutput.tail("B", "all", 0, 0, 100)
    time.sleep(0.1)
    assert FinchOutput.tail("B", "all", 0, 0, 0)


def test_move():
    assert FinchOutput.move("B", Constant.FORWARD, 4, 5)
    assert FinchOutput.move("B", Constant.FORWARD, "4", "5")

    assert FinchOutput.move("B", Constant.BACKWARD, 4, 5)
    assert FinchOutput.move("B", Constant.BACKWARD, "4", "5")

    with pytest.raises(Exception) as e:
        assert FinchOutput.move("B", "BAD", 4, 5)
        assert e.value.message == "Error: Request to device failed"

    with pytest.raises(Exception) as e:
        assert FinchOutput.move("B", None, 4, 5)
        assert e.value.message == "Error: Request to device failed"

    Request.stop_all("B")


def test_turn():
    assert FinchOutput.turn("B", "L", 25, 50)
    assert FinchOutput.turn("B", "R", 25, 50)
    assert FinchOutput.turn("B", "L", "25", 50)
    assert FinchOutput.turn("B", "R", 25, "50")

    with pytest.raises(Exception) as e:
        assert FinchOutput.turn("B", "BAD", 90, 50)
        assert e.value.message == "Error: Request to device failed"


def test_motors():
    assert FinchOutput.motors("B", 25, 0)
    time.sleep(0.2)
    assert FinchOutput.motors("B", -25, 0)
    time.sleep(0.2)

    assert FinchOutput.motors("B", 0, -25)
    time.sleep(0.2)
    assert FinchOutput.motors("B", "0", "25")
    time.sleep(0.2)

    Request.stop_all("B")


def test_stop():
    assert FinchOutput.move("B", Constant.FORWARD, 99999, 5, False)
    time.sleep(0.2)
    assert FinchOutput.stop("B")

    assert FinchOutput.move("B", Constant.BACKWARD, 99999, 5, False)
    time.sleep(0.2)
    assert FinchOutput.stop("B")


def test_reset_encoders():
    assert FinchOutput.reset_encoders("B")
