from robot.microbit_output import MicrobitOutput
from robot.request import Request
from robot.state import State


def test_windows_support(mocker):
    mocker.patch.object(Request, "response_from_uri", return_value="200")

    Request.is_connected('A')

    state = State()

    assert MicrobitOutput.point(state, "A", 3, 3, True)
