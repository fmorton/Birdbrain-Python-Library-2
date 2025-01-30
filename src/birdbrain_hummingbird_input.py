import sys
import time

import urllib.request

from birdbrain_exception import BirdbrainException
from birdbrain_microbit import BirdbrainMicrobit

class BirdbrainHummingbirdInput(BirdbrainRequest):
    # -------------------------------------------------------------------------
    # HUMMINGBIRD BIT INPUT
    # -------------------------------------------------------------------------
    def getSensor(self, port):
        """Read the value of the sensor attached to a certain port.
        If the port is not valid, it returns -1."""

        # Early return if we can't execute the command because the port is invalid
        if not self.isPortValid(port, 3):
            return -1

        response = self.send_httprequest_in("sensor", port)
        return response

    def getLight(self, port):
        """Read the value of the light sensor attached to a certain port."""

        response = self.getSensor(port)
        light_value = int(response * LIGHT_FACTOR)
        return light_value

    def getSound(self, port):
        """Read the value of the sound sensor attached to a certain port."""

        if port == "microbit" or port == "micro:bit" or port == "Microbit":
            return Microbit.getSound(self)

        response = self.getSensor(port)
        sound_value = int(response * SOUND_FACTOR)
        return sound_value

    def getDistance(self, port):
        """Read the value of the distance sensor attached to a certain port."""

        response = self.getSensor(port)
        distance_value = int(response * DISTANCE_FACTOR)
        return distance_value

    def getDial(self, port):
        """Read the value of the dial attached to a certain port."""

        response = self.getSensor(port)
        dial_value = int(response * DIAL_FACTOR)
        if (dial_value > 100):
            dial_value = 100
        return dial_value

    def getVoltage(self, port):
        """Read the value of  the dial attached to a certain port."""

        response = self.getSensor(port)
        voltage_value = response * VOLTAGE_FACTOR
        return voltage_value
