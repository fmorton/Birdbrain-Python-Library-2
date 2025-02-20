from birdbrain_microbit_input import BirdbrainMicrobitInput
from birdbrain_request import BirdbrainRequest

class BirdbrainHummingbirdInput(BirdbrainRequest):
    @classmethod
    def acceleration(self, device):
        """Gives the acceleration of X,Y,Z in m/sec2, relative
        to the Finch's position."""

        return BirdbrainMicrobitInput.acceleration(device)

    @classmethod
    def compass(self, device):
        """Returns values 0-359 indicating the orentation of the Earth's
        magnetic field, relative to the Finch's position."""

        return BirdbrainMicrobitInput.compass(device)

    @classmethod
    def magnetometer(self, device):
        """Return the values of X,Y,Z of a magnetommeter, relative to the Finch's position."""

        return BirdbrainMicrobitInput.magnetometer(device)

    @classmethod
    def orientation(self, device):
        """Return the orentation of the Hummingbird. Results found in BirdbrainConstant.HUMMINGBIRD_ORIENTATION_RESULTS"""

        return BirdbrainMicrobitInput.orientation(device)

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
