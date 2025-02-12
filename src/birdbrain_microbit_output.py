from birdbrain_exception import BirdbrainException
from birdbrain_request import BirdbrainRequest

class BirdbrainMicrobitOutput(BirdbrainRequest):
    @classmethod
    def microbit_display(self, state, device, list):
        if len(list) != 25: raise BirdbrainException("Error: microbit_display() requires a list of length 25")

        return BirdbrainRequest.response_status('hummingbird', 'out', 'symbol', device, state.microbit_display_map_as_string(list))

    @classmethod
    def microbit_clear_display(self, state, device):
        return microbit_display(state, device, BirdbrainState.microbit_empty_display_map())

    @classmethod
    def microbit_point(self, state, device, x, y, value):
        index = ((x * 5) + y - 6)

        state.microbit_display_map[index] = value

        return microbit_display(state, device, state.microbit_display_map)

    @classmethod
    def microbit_print(self, device, message):
        calc_message = message.gsub(' ', '%20')

        request_status(response_body('hummingbird', 'out', 'print', calc_message, device))

    #####----------------------------------
    def setDisplay(self, LEDlist):
        """Set Display of the LED Array on microbit with the given input LED
        list of 0's and 1's."""

        # Check if LED_string is valid to be printed on the display
        # Check if the length of the array to form a symbol not equal than 25
        if (len(LEDlist) != 25):
            print("Error: setDisplay() requires a list of length 25")
            return             # if the array is the wrong length, don't want to do anything else

        # Check if all the characters entered are valid
        for index in range(0, len(LEDlist)):
            LEDlist[index] = self.clampParametersToBounds(LEDlist[index], 0, 1)

        # Reset the display status
        self.symbolvalue = LEDlist

        # Convert the LED_list to  an appropriate value which the server can understand
        LED_string = self.process_display(LEDlist)
        # Send the http request
        response = self.send_httprequest_micro("symbol", LED_string)
        return response

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

    def setPoint(self, x, y, value):
        """Choose a certain LED on the LED Array and switch it on or off.
        The value specified should be 1 for on, 0 for off."""

        # Check if x, y and value are valid
        x = self.clampParametersToBounds(x, 1, 5)
        y = self.clampParametersToBounds(y, 1, 5)
        value = self.clampParametersToBounds(value, 0, 1)

        # Calculate which LED should be selected
        index = (x - 1) * 5 + (y - 1)

        # Update the state of the LED displayf
        self.symbolvalue[index] = value

        # Convert the display status to  an appropriate value which the server can understand
        outputString = self.process_display(self.symbolvalue)

        # Send the http request
        response = self.send_httprequest_micro("symbol", outputString)
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

