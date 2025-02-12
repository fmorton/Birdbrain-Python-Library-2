from birdbrain_exception import BirdbrainException
from birdbrain_request import BirdbrainRequest
from birdbrain_state import BirdbrainState

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
    def microbit_print(self, device, message):
        calc_message = message.gsub(' ', '%20')

        request_status(response_body('hummingbird', 'out', 'print', calc_message, device))

    #####----------------------------------


    def print(self, message):
        """Print the characters on the LED screen."""

        # Warn the user about any special characters - we can mostly only print English characters and digits
        for letter in message:
            if not (((letter >= 'a') and (letter <= 'z')) or ((letter >= 'A') and (letter <= 'Z')) or
                    ((letter >= '0') and (letter <= '9')) or (letter == ' ')):
                print("Warning: Many special characters cannot be printed on the LED display")

        # Need to replace spaces with %20
        message = message.replace(' ', '%20')

        # Empty out the internal representation of the display, since it will be blank when the print ends
        self.symbolvalue = [0]*25

        # Send the http request
        response = self.send_httprequest_micro("print", message)
        return response



    def playNote(self, note, beats):
        """Make the buzzer play a note for certain number of beats. Note is the midi
        note number and should be specified as an integer from 32 to 135. Beats can be
        any number from 0 to 16. One beat corresponds to one second."""

        # Check that both parameters are within the required bounds
        note = self.clampParametersToBounds(note, 32, 135)
        beats = self.clampParametersToBounds(beats, 0, 16)

        note = self.__constrainToInt(note)
        beats = int(beats * (60000 / TEMPO))

        # Send HTTP request
        # response = self.__send_httprequest_out("playnote", note, beats)
        http_request = self.base_request_out + "/playnote/" + str(note) + "/" + str(beats) + "/" + str(self.device_s_no)
        response = self._send_httprequest(http_request)
        return response

