from birdbrain_constant import BirdbrainConstant
from birdbrain_exception import BirdbrainException
from birdbrain_request import BirdbrainRequest
from birdbrain_state import BirdbrainState
from birdbrain_utility import BirdbrainUtility

class BirdbrainMicrobitOutput(BirdbrainRequest):
    @classmethod
    def microbit_display(self, state, device, list):
        if len(list) != 25: raise BirdbrainException("Error: microbit_display() requires a list of length 25")

        return BirdbrainRequest.response_status('hummingbird', 'out', 'symbol', device, state.microbit_display_map_as_string(list))

    @classmethod
    def microbit_clear_display(self, state, device):
        return self.microbit_display(state, device, BirdbrainState.microbit_empty_display_map())

    @classmethod
    def microbit_point(self, state, device, x, y, value):
        index = ((x * 5) + y - 6)

        try:
            state.microbit_display_map[index] = value
        except IndexError:
            raise BirdbrainException("Error: microbit_point out of range")

        return self.microbit_display(state, device, state.microbit_display_map)

    @classmethod
    def microbit_print(self, state, device, message):
        """Print the characters on the LED screen."""

        # clear internal representation of the display since it will be blank when the print ends
        self.microbit_clear_display(state, device)

        # need to encode space for uri (used to be %20)
        message = message.replace(' ', '+')

        return BirdbrainRequest.response_status('hummingbird', 'out', 'print', message)

    @classmethod
    def microbit_play_note(self, device, note, beats):
        """Make the buzzer play a note for certain number of beats. Note is the midi
        note number and should be specified as an integer from 32 to 135. Beats can be
        any number from 0 to 16. One beat corresponds to one second."""

        note = BirdbrainUtility.bounds(note, 32, 135)
        beats = int(BirdbrainUtility.decimal_bounds(beats, 0, 16) * BirdbrainConstant.BEATS_TEMPO_FACTOR)

        return BirdbrainRequest.response_status('hummingbird', 'out', 'playnote', note, beats, device)
