import pytest

from robot.hummingbird import Hummingbird
from robot.microbit_output import MicrobitOutput
from robot.request import Request
from robot.state import State


def test_windows_support(mocker):
    mocker.patch.object(Request, "response_from_uri", return_value="200")

    Request.is_connected('A')

    state = State()

    assert MicrobitOutput.point(state, "A", 3, 3, True)

    hummingbird = Hummingbird('A')

    with pytest.raises(Exception) as e:
        response = hummingbird.light(4)
    assert e.value.message == "Error: The device is not connected"

    with pytest.raises(Exception) as e:
        response = hummingbird.sound(4)
    assert e.value.message == "Error: The device is not connected"

    with pytest.raises(Exception) as e:
        response = HummingbirdInput.sound("A", 4)
    assert e.value.message == "Error: The device is not connected"
