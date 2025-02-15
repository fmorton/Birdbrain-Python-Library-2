from birdbrain_constant import BirdbrainConstant
from birdbrain_exception import BirdbrainException
from birdbrain_utility import BirdbrainUtility

import time
import urllib.request

class BirdbrainRequest:
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
            if BirdbrainConstant.BIRDBRAIN_TEST: print("Test: URI", self.uri(args))

            response_request = urllib.request.urlopen(self.uri(args))
        except (ConnectionError, urllib.error.URLError, urllib.error.HTTPError):
            raise(BirdbrainException("Error: Request to device failed"))

        response = response_request.read().decode('utf-8').lower()

        if BirdbrainConstant.BIRDBRAIN_TEST: print("Test: response", response)

        if (self.is_not_connected_response(response)): raise(BirdbrainException("Error: The device is not connected"))

        time.sleep(0.01)  # hack to prevent http requests from overloading the BlueBird Connector

        return response

    @classmethod
    def response_status(self, *args):
        return BirdbrainRequest.request_status(BirdbrainRequest.response(args))

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
     if BirdbrainConstant.BIRDBRAIN_TEST: print("Test: request status is", status)

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
        return int(int(intensity) * 255 / 180)

    @classmethod
    def calculate_intensity(self, intensity):
        return int(int(self.bounds(intensity, 0, 100)) * 255 / 100)

    @classmethod
    def calculate_speed(self, speed):
        if int(speed) in range(-10, 10): return 255

        # QUESTION: why this calculation instead of normal mapping to 0..255 (and 255 means stop)
        # return ((int(speed) * 23 / 100) + 122)

        if int(speed) < 0:
            return int(119 - (-int(speed) / 100 * 45))
        else:
            return int((int(speed) / 100 * 25) + 121)

    @classmethod
    def calculate_left_or_right(self, direction):
        if direction == BirdbrainConstant.LEFT: return 'Left'
        if direction == BirdbrainConstant.RIGHT: return 'Right'

        return None

    @classmethod
    def validate(self, validate, valid_range, validate_message):
        if not str(validate) in valid_range: raise BirdbrainException(validate_message)

        return True

    @classmethod
    def validate_port(self, port, valid_range, allow_all = False):
        if allow_all and str(port) == 'all': return True

        return BirdbrainRequest.validate(port, valid_range, f"Port {str(port)} out of range.")

    @classmethod
    def bounds(self, input, input_min, input_max, pass_through_input = None):
        #if pass_through_input is not None and (input == pass_through_input): return int(input)

        if int(input) < int(input_min): return int(input_min)
        if int(input) > int(input_max): return int(input_max)

        return int(input)

    @classmethod
    def tri_led_response(self, device, port, r_intensity, g_intensity, b_intensity, valid_range, allow_all = False):
        """Set TriLED  of a certain port requested to a valid intensity."""
        self.validate_port(port, valid_range, allow_all)

        calc_r = BirdbrainRequest.calculate_intensity(r_intensity)
        calc_g = BirdbrainRequest.calculate_intensity(g_intensity)
        calc_b = BirdbrainRequest.calculate_intensity(b_intensity)

        return BirdbrainRequest.response_status('hummingbird', 'out', 'triled', port, calc_r, calc_g, calc_b, device)
