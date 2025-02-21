from birdbrain_constant import BirdbrainConstant
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

    def getSensor(self, port):
        """Read the value of the sensor attached to a certain port.
        If the port is not valid, it returns -1."""

        # Early return if we can't execute the command because the port is invalid
        if not self.isPortValid(port, 3):
            return -1

        response = self.send_httprequest_in("sensor", port)
        return response

    @classmethod
    def getLight(self, port):
        """Read the value of the light sensor attached to a certain port."""
        pass
        #return self.sensor_response(device, 'Light', BirdbrainRequest.calculate_left_or_right(side))

        #response = self.getSensor(port)
        #light_value = int(response * LIGHT_FACTOR)
        #return light_value

    @classmethod
    def sound(self, device, port):
        """Read the value of the sound sensor attached to a certain port."""

        port = str(port).lower()

        if port == "microbit" or port == "micro:bit":
            return BirdbrainMicrobitInput.sound(device)

        encoder_options = {}
        encoder_options['factor'] = BirdbrainConstant.SOUND_FACTOR
        encoder_options['min_response'] = BirdbrainConstant.DEFAULT_MIN_RESPONSE
        encoder_options['max_response'] = BirdbrainConstant.DEFAULT_MAX_RESPONSE

        return self.sensor_response(device, 'sensor', port, encoder_options)

    @classmethod
    def distance(self, device, port):
        """Read the value of the distance sensor attached to a certain port."""

        encoder_options = {}
        encoder_options['factor'] = BirdbrainConstant.DISTANCE_FACTOR
        encoder_options['min_response'] = BirdbrainConstant.DEFAULT_MIN_RESPONSE
        encoder_options['max_response'] = BirdbrainConstant.DEFAULT_UNLIMITED_MAX_RESPONSE

        return self.sensor_response(device, 'sensor', port, encoder_options)

    @classmethod
    def dial(self, device, port):
        """Read the value of the dial attached to a certain port."""

        encoder_options = {}
        encoder_options['factor'] = BirdbrainConstant.DIAL_FACTOR
        encoder_options['min_response'] = BirdbrainConstant.DEFAULT_MIN_RESPONSE
        encoder_options['max_response'] = BirdbrainConstant.DEFAULT_MAX_RESPONSE

        return self.sensor_response(device, 'sensor', port, encoder_options)

    def getVoltage(self, port):
        """Read the value of  the dial attached to a certain port."""

        response = self.getSensor(port)
        voltage_value = response * VOLTAGE_FACTOR
        return voltage_value
