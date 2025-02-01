from birdbrain_exception import BirdbrainException
from birdbrain_utility import BirdbrainUtility

import time
import urllib.request

class BirdbrainRequest:
    BIRDBRAIN_TEST = False

    @classmethod
    def uri(self, *args):
        return("http://127.0.0.1:30061/" + BirdbrainUtility.flatten_string(args[0]))

    @classmethod
    def is_not_connected_response(self, response):
        return((response.lower() == "not connected"))

    @classmethod
    def response(self, *args):
        if "false" in args: return False

        try:
            if BirdbrainRequest.BIRDBRAIN_TEST: print("Test:", self.uri(args))

            response_request = urllib.request.urlopen(self.uri(args))
        except (ConnectionError, urllib.error.URLError):
            raise(BirdbrainException("Error: Request to device failed"))

        response = response_request.read().decode('utf-8').lower()

        if (self.is_not_connected_response(response)): raise(BirdbrainException("Error: The device is not connected"))

        time.sleep(0.01)  # Hack to prevent http requests from overloading the BlueBird Connector

        return response

    @classmethod
    def is_connected(self, device):
        try:
            response = self.response('hummingbird', 'in', 'orientation', 'Shake', device)
        except BirdbrainException:
            return False

        return True

    @classmethod
    def is_not_connected(self, device):
        return(not self.is_connected(device))

    @classmethod
    def stop_all(self, device):
        return(self.request_status(self.response('hummingbird', 'out', 'stopall', device)))

    @classmethod
    def request_status(self, status):
     if BirdbrainRequest.BIRDBRAIN_TEST: print("Test: request status is", status)

     if status is None: return None

     if status == 'true': return(True)
     if status == 'led set': return(True)
     if status == 'triled set': return(True)
     if status == 'servo set': return(True)
     if status == 'buzzer set': return(True)
     if status == 'symbol set': return(True)
     if status == 'print set': return(True)
     if status == 'all stopped': return(True)

     if status == 'finch moved': return(True)
     if status == 'finch turned': return(True)
     if status == 'finch wheels started': return(True)
     if status == 'finch wheels stopped': return(True)
     if status == 'finch encoders reset': return(True)

     if status == 'false': return(False)
     if status == 'not connected': return(False)
     if status == 'invalid orientation': return(False)

     return(None)

    @classmethod
    def xyz_response(self, device, sensor):
        x = self.response('hummingbird', 'in', sensor, 'X', device)

        y = self.response('hummingbird', 'in', sensor, 'Y', device)
        z = self.response('hummingbird', 'in', sensor, 'Z', device)

        return [float(x), float(y), float(z)]

    @classmethod
    def calculate_angle(self, intensity):
        return int(intensity * 255 / 180)

    @classmethod
    def calculate_intensity(self, intensity):
        return int(intensity * 255 / 100)

#    @classmethod
#    def calculate_speed(self, speed):
#        return 255 if speed.between?(-10, 10)
#
#        # QUESTION: why this calculation instead of normal mapping to 0..255 (and 255 means stop)
#        return ((speed * 23 / 100) + 122)
#
#    @classmethod
#    def calculate_left_or_right(self, direction):
#        if direction == BirdbrainDevice.LEFT: return 'Left'
#        if direction == BirdbrainDevice.RIGHT: return 'Right'
#
#        return false

    @classmethod
    def bounds(self, input, input_min, input_max, pass_through_input = None):
        if pass_through_input is not None and (input == pass_through_input): return input

        if input < input_min: return input_min
        if input > input_max: return input_max

        return input
