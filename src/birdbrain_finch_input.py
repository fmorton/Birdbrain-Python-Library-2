from birdbrain_request import BirdbrainRequest

class BirdbrainFinchInput(BirdbrainRequest):
    # Finch Inputs
    def __getSensor(self, sensor, port):
        """Read the value of the specified sensor. Port should be specified as either 'R'
        or 'L'. If the port is not valid, returns -1."""

        # Early return if we can't execute the command because the port is invalid
        if ((not sensor == "finchOrientation") and (not port == "Left") and (not port == "Right") and
                (not ((port == "static") and (sensor == "Distance" or sensor == "finchCompass")))):
            return -1

        response = self.__send_httprequest_in(sensor, port)
        return response

    def getLight(self, direction):
        """Read the value of the right or left light sensor ('R' or 'L')."""

        direction = self.__formatRightLeft(direction)
        if direction is None:
            return 0

        response = self.__getSensor("Light", direction)
        return int(response)

    def getDistance(self):
        """Read the value of the distance sensor"""

        response = self.__getSensor("Distance", "static")
        return int(response)

    def getLine(self, direction):
        """Read the value of the right or left line sensor ('R' or 'L').
        Returns brightness as a value 0-100 where a larger number
        represents more reflected light."""

        direction = self.__formatRightLeft(direction)
        if direction is None:
            return 0

        response = self.__getSensor("Line", direction)
        return int(response)

    def getEncoder(self, direction):
        """Read the value of the right or left encoder ('R' or 'L').
        Values are returned in rotations."""

        direction = self.__formatRightLeft(direction)
        if direction is None:
            return 0

        response = self.__getSensor("Encoder", direction)
        encoder_value = round(float(response), 2)
        return encoder_value

    # The following methods override those within the Microbit
    # class to return values within the Finch reference frame.
    def getAcceleration(self):
        """Gives the acceleration of X,Y,Z in m/sec2, relative
        to the Finch's position."""

        return self._getXYZvalues("finchAccel", False)

    def getCompass(self):
        """Returns values 0-359 indicating the orentation of the Earth's
        magnetic field, relative to the Finch's position."""

        # Send HTTP request
        response = self.__getSensor("finchCompass", "static")
        compass_heading = int(response)
        return compass_heading

    def getMagnetometer(self):
        """Return the values of X,Y,Z of a magnetommeter, relative to the Finch's position."""

        return self._getXYZvalues("finchMag", True)

    def getOrientation(self):
        """Return the orentation of the Finch. Options include:
        "Beak up", "Beak down", "Tilt left", "Tilt right", "Level",
        "Upside down", and "In between"."""

        orientations = ["Beak%20Up", "Beak%20Down", "Tilt%20Left", "Tilt%20Right", "Level", "Upside%20Down"]
        orientation_result = ["Beak up", "Beak down", "Tilt left", "Tilt right", "Level", "Upside down"]

        # Check for orientation of each device and if true return that state
        for targetOrientation in orientations:
            response = self.__getSensor("finchOrientation", targetOrientation)
            if (response == "true"):
                return orientation_result[orientations.index(targetOrientation)]

        # If we are in a state in which none of the above seven states are true
        return "In between"
