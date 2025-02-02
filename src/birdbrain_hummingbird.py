import sys
import time

import urllib.request

from birdbrain_constant import BirdbrainConstant
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
            raise BirdbrainException("Device " + device + " is not a Hummingbird")

    def led(self, port, intensity):
        return BirdbrainHummingbirdOutput.led(self.device, port, intensity)

    def tri_led(self, port, r_int, g_int, b_int):
        return BirdbrainHummingbirdOutput.tri_led(self.device, port, r_int, g_int, b_int)

    def position_servo(self, port, angle):
        return BirdbrainHummingbirdOutput.position_servo(self.device, port, angle)

    def rotation_servo(self, port, speed):
        return BirdbrainHummingbirdOutput.rotation_servo(self.device, port, speed)

    # Hummingbird Aliases
    #dial = getDial
    #distance = getDistance
    #is_hummingbird = isHummingbird
    setLED = led
    #light = getLight
    setPositionServo = position_servo
    setRotationServo = rotation_servo
    #sensor = getSensor
    #sound = getSound
    # stop_all = stopAll
    # temperature = getTemperature
    setTriLED = tri_led
    #voltage = getVoltage

