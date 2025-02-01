import sys
import time

import urllib.request

from birdbrain_exception import BirdbrainException
from birdbrain_hummingbird_output import BirdbrainHummingbirdOutput
from birdbrain_microbit import BirdbrainMicrobit

class BirdbrainHummingbird(BirdbrainMicrobit):
    """Hummingbird Bit Class includes the control of the outputs and inputs
        present on the Hummingbird Bit."""
    VALID_LED_PORTS = '123'

    def __init__(self, device = 'A', raise_exception_if_no_connection = True):
        """Class initializer. Specify device letter A, B or C."""
        device_object = BirdbrainHummingbird.connect(device, raise_exception_if_no_connection)

        if not self.is_hummingbird():
            raise BirdbrainException("Error: Device " + device + " is not a Hummingbird")

    def led(self, port, intensity):
        if self.is_connected_and_valid(port, self.VALID_LED_PORTS):
            return BirdbrainHummingbirdOutput.led(self.device, port, intensity)

    def tri_led(self, port, r_intensity, g_intensity, b_intensity):
        if self.is_connected_and_valid(port, self.VALID_LED_PORTS):
            return BirdbrainHummingbirdOutput.tri_led(self.device, port, r_intensity, g_intensity, b_intensity)

    #def calculate_servo_r(self, servo_value):
    #    """Utility function to covert Servo from -100 - 100 to 0-255."""
    #
    #    # If the values are above the limits fix the instensity to maximum value,
    #    # if less than the minimum value fix the intensity to minimum value
    #    if ((servo_value > -10) and (servo_value < 10)):
    #        servo_value_c = 255
    #    else:
    #        servo_value_c = int((servo_value * 23 / 100) + 122)
    #    return servo_value_c

    # Hummingbird Aliases
    #dial = getDial
    #distance = getDistance
    #is_hummingbird = isHummingbird
    #is_port_valid = isPortValid
    setLED = led
    #light = getLight
    #position_servo = setPositionServo
    #rotation_servo = setRotationServo
    #sensor = getSensor
    #sound = getSound
    # stop_all = stopAll
    # temperature = getTemperature
    setTriLED = tri_led
    #voltage = getVoltage

