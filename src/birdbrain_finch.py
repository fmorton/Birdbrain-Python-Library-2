import sys
import time

import urllib.request

from birdbrain_exception import BirdbrainException
from birdbrain_microbit import BirdbrainMicrobit

class BirdbrainFinch(BirdbrainMicrobit):
    """The Finch class includes the control of the outputs and inputs present
    in the Finch robot. When creating an instance, specify which robot by the
    device letter used in the BlueBirdConnector device list (A, B, or C)."""

    def __init__(self, device='A', raise_exception_if_no_connection = True):
        """Class initializer. """

        self.device_object = BirdbrainFinch.connect(device, raise_exception_if_no_connection)

        if not self.is_finch():
            raise BirdbrainException("Error: Device " + device + " is not a Finch")

    # Finch Utility Functions
    @staticmethod
    def __calculate_RGB(r_intensity, g_intensity, b_intensity):
        """Utility function to covert RGB LED from 0-100 to 0-255"""

        r_intensity_c = int((r_intensity * 255) / 100)
        g_intensity_c = int((g_intensity * 255) / 100)
        b_intensity_c = int((b_intensity * 255) / 100)

        return (r_intensity_c, g_intensity_c, b_intensity_c)

    @staticmethod
    def __formatRightLeft(direction):
        """Utility function to format a selection of right or left for a backend request."""

        if direction == "R" or direction == "r" or direction == "Right" or direction == "right":
            return "Right"
        elif direction == "L" or direction == "l" or direction == "Left" or direction == "left":
            return "Left"
        else:
            print("Error: Please specify either 'R' or 'L' direction.")
            return None

    @staticmethod
    def __formatForwardBackward(direction):
        """Utility function to format a selection of forward or backward for a backend request."""

        if direction == "F" or direction == "f" or direction == "Forward" or direction == "forward":
            return "Forward"
        elif direction == "B" or direction == "b" or direction == "Backward" or direction == "backward":
            return "Backward"
        else:
            print("Error: Please specify either 'F' or 'B' direction.")
            return None

    def __send_httprequest_in(self, peri, port):
        pass

    def __send_httprequest_out(self, arg1, arg2, arg3):
        pass

    def __send_httprequest_move(self, arg1, arg2, arg3, arg4):
        pass

    # Finch Aliases
    #acceleration = getAcceleration
    #beak = setBeak
    #compass = getCompass
    #distance = getDistance
    #encoder = getEncoder
    #light = getLight
    #line = getLine
    #magnetometer = getMagnetometer
    #motors = setMotors
    #move = setMove
    #orientation = getOrientation
    #reset_encoders = resetEncoders
    #tail = setTail
    #turn = setTurn

    # END class Finch
