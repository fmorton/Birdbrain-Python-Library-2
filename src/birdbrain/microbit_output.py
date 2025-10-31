from birdbrain.constant import Constant
from birdbrain.exception import Exception
from birdbrain.request import Request
from birdbrain.state import State
from birdbrain.utility import Utility


class MicrobitOutput(Request):
    @classmethod
    def display(self, state, device, list):
        if len(list) != 25:
            raise Exception("Error: display() requires a list of length 25")

        return Request.response_status('hummingbird', 'out', 'symbol', device, state.display_map_as_string(list))

    @classmethod
    def clear_display(self, state, device):
        return self.display(state, device, State.microbit_empty_display_map())

    @classmethod
    def point(self, state, device, x, y, value):
        index = (x * 5) + y - 6

        try:
            state.display_map[index] = value
        except IndexError:
            raise Exception("Error: point out of range")

        return self.display(state, device, state.display_map)

    @classmethod
    def print(self, state, device, message):
        """Print the characters on the LED screen."""

        # clear internal representation of the display since it will be blank when the print ends
        self.clear_display(state, device)

        # if no message specified print as a blank
        if message is None or len(message) == 0:
            message = ' '

        # need to encode space for uri (used to be %20)
        message = message.replace(' ', '+')

        return Request.response_status('hummingbird', 'out', 'print', message, device)

    @classmethod
    def play_note(self, device, note, beats):
        """Make the buzzer play a note for certain number of beats. Note is the midi
        note number and should be specified as an integer from 32 to 135. Beats can be
        any number from 0 to 16. One beat corresponds to one second."""

        note = Utility.bounds(note, 32, 135)
        beats = int(Utility.decimal_bounds(beats, 0, 16) * Constant.BEATS_TEMPO_FACTOR)

        return Request.response_status('hummingbird', 'out', 'playnote', note, beats, device)
