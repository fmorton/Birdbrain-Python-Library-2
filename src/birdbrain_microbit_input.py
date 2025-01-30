import sys
import time

import urllib.request

from birdbrain_exception import BirdbrainException
from birdbrain_microbit import BirdbrainMicrobit

class BirdbrainMicrobitInput(BirdbrainRequest):
    # -----------------------------------------------------------------------------
    # INPUTS MICROBIT
    # -----------------------------------------------------------------------------
    def _getXYZvalues(self, sensor, intResult):
        """Return the X, Y, and Z values of the given sensor."""

        dimension = ['X', 'Y', 'Z']
        values = []

        for i in range(0, 3):
            # Send HTTP request
            response = self.send_httprequest_micro_in(sensor, dimension[i])
            if intResult:
                values.append(int(response))
            else:
                values.append(round(float(response), 3))

        return (values[0], values[1], values[2])

    def getAcceleration(self):
        """Gives the acceleration of X,Y,Z in m/sec2."""

        return self._getXYZvalues("Accelerometer", False)

    def getCompass(self):
        """Returns values 0-359 indicating the orentation of the Earth's
        magnetic field."""

        # Send HTTP request
        response = self.send_httprequest_micro_in("Compass", None)
        compass_heading = int(response)
        return compass_heading

    def getMagnetometer(self):
        """Return the values of X,Y,Z of a magnetommeter."""

        return self._getXYZvalues("Magnetometer", True)

    def getButton(self, button):
        """Return the status of the button asked. Specify button 'A', 'B', or
        'Logo'. Logo available for V2 micro:bit only."""

        button = button.upper()
        # Check if the button A and button B are represented in a valid manner
        if ((button != 'A') and (button != 'B') and (button != 'LOGO')):
            print("Error: Button must be A, B, or Logo.")
            sys.exit()
        # Send HTTP request
        response = self.send_httprequest_micro_in("button", button)
        # Convert to boolean form
        if (response == "true"):
            button_value = True
        elif (response == "false"):
            button_value = False
        else:
            print("Error in getButton: " + response)
            sys.exit()

        return button_value

    def getSound(self):
        """Return the current sound level as an integer between 1 and 100.
        Available for V2 micro:bit only."""

        response = self.send_httprequest_micro_in("V2sensor", "Sound")

        try:
            value = int(response)
        except (ConnectionError, urllib.error.URLError):
            print("Error in getSound: " + response)
            sys.exit()

        return value

    def getTemperature(self):
        """Return the current temperature as an integer in degrees Celcius.
        Available for V2 micro:bit only."""

        response = self.send_httprequest_micro_in("V2sensor", "Temperature")

        try:
            value = int(response)
        except (ConnectionError, urllib.error.URLError):
            print("Error in getTemperature: " + response)
            sys.exit()

        return value

    def isShaking(self):
        """Return true if the device is shaking, false otherwise."""

        # Send HTTP request
        response = self.send_httprequest_micro_in("Shake", None)
        if (response == "true"):  # convert to boolean
            shake = True
        else:
            shake = False

        return shake

    def getOrientation(self):
        """Return the orentation of the micro:bit. Options include:
        "Screen up", "Screen down", "Tilt left", "Tilt right", "Logo up",
        "Logo down", and "In between"."""

        orientations = ["Screen%20Up", "Screen%20Down", "Tilt%20Left", "Tilt%20Right", "Logo%20Up", "Logo%20Down"]
        orientation_result = ["Screen up", "Screen down", "Tilt left", "Tilt right", "Logo up", "Logo down"]

        # Check for orientation of each device and if true return that state
        for targetOrientation in orientations:
            response = self.send_httprequest_micro_in(targetOrientation, None)
            if (response == "true"):
                return orientation_result[orientations.index(targetOrientation)]

        # If we are in a state in which none of the above seven states are true
        return "In between"

    def stopAll(self):
        """Stop all device outputs (ie. Servos, LEDs, LED Array, Motors, etc.)."""

        time.sleep(0.1)         # Hack to give stopAll() time to act before the end of a program
        response = self.send_httprequest_stopAll()
        self.symbolvalue = [0]*25
        return response

