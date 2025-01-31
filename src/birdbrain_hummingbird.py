import sys
import time

import urllib.request

from birdbrain_exception import BirdbrainException
from birdbrain_hummingbird_output import BirdbrainHummingbirdOutput
from birdbrain_microbit import BirdbrainMicrobit

class BirdbrainHummingbird(BirdbrainMicrobit):
    """Hummingbird Bit Class includes the control of the outputs and inputs
        present on the Hummingbird Bit."""

    def __init__(self, device = 'A', raise_exception_if_no_connection = True):
        """Class initializer. Specify device letter A, B or C."""
        device_object = BirdbrainHummingbird.connect(device, raise_exception_if_no_connection)

        if not self.is_hummingbird():
            raise BirdbrainException("Error: Device " + device + " is not a Hummingbird")

    def led(self, port, intensity):
        BirdbrainHummingbirdOutput.led(self.device, port, intensity)
        ####DEBUG###BirdbrainHummingbirdOutput.led(device, port, intensity) if connected_and_valid?(port, VALID_LED_PORTS)

    def isPortValid(self, port, portMax):
        """This function checks whether a port is within the given bounds.
        It returns a boolean value that is either true or false and prints
        an error if necessary."""

        if ((port < 1) or (port > portMax)):
            print("Error: Please choose a port value between 1 and " + str(portMax))
            return False
        else:
            return True

    def calculate_LED(self, intensity):
        """ Utility function to covert LED from 0-100 to 0-255."""

        intensity_c = int((intensity * 255) / 100)

        return intensity_c

    def calculate_RGB(self, r_intensity, g_intensity, b_intensity):
        """Utility function to covert RGB LED from 0-100 to 0-255."""

        r_intensity_c = int((r_intensity * 255) / 100)
        g_intensity_c = int((g_intensity * 255) / 100)
        b_intensity_c = int((b_intensity * 255) / 100)

        return (r_intensity_c, g_intensity_c, b_intensity_c)

    def calculate_servo_p(self, servo_value):
        """Utility function to covert Servo from 0-180 to 0-255."""

        servo_value_c = int((servo_value * 254) / 180)

        return servo_value_c

    def calculate_servo_r(self, servo_value):
        """Utility function to covert Servo from -100 - 100 to 0-255."""

        # If the vlaues are above the limits fix the instensity to maximum value,
        # if less than the minimum value fix the intensity to minimum value
        if ((servo_value > -10) and (servo_value < 10)):
            servo_value_c = 255
        else:
            servo_value_c = int((servo_value * 23 / 100) + 122)
        return servo_value_c

    # -------------------------------------------------------------------------
    # SEND HTTP REQUESTS
    # -------------------------------------------------------------------------
    def send_httprequest_in(self, peri, port):
        pass

    def send_httprequest(self, peri, port, value):
        pass

    # Hummingbird Aliases
    #dial = getDial
    #distance = getDistance
    #is_hummingbird = isHummingbird
    #is_port_valid = isPortValid
    #led = setLED
    #light = getLight
    #position_servo = setPositionServo
    #rotation_servo = setRotationServo
    #sensor = getSensor
    #sound = getSound
    # stop_all = stopAll
    # temperature = getTemperature
    #tri_led = setTriLED
    #voltage = getVoltage

    # END class Hummingbird

