from birdbrain_constant import BirdbrainConstant
from birdbrain_device import BirdbrainDevice
from birdbrain_microbit_input import BirdbrainMicrobitInput
from birdbrain_request import BirdbrainRequest
from birdbrain_utility import BirdbrainUtility

class BirdbrainFinchInput(BirdbrainRequest):
    DEFAULT_DEGREES_MIN_RESPONSE = 0
    DEFAULT_DEGREES_MAX_RESPONSE = 359
    DEFAULT_FACTOR = 1.0
    DEFAULT_MIN_RESPONSE = 0.0
    DEFAULT_MAX_RESPONSE = 100.0
    DEFAULT_TYPE_METHOD = 'int'
    DEFAULT_UNLIMITED_MIN_RESPONSE = -1000000
    DEFAULT_UNLIMITED_MAX_RESPONSE = 1000000
    ORIENTATIONS = ['Beak%20Up', 'Beak%20Down', 'Tilt%20Left', 'Tilt%20Right', 'Level', 'Upside%20Down']
    ORIENTATION_RESULTS = ['Beak up', 'Beak down', 'Tilt left', 'Tilt right', 'Level', 'Upside down', 'In between']
    ORIENTATION_IN_BETWEEN = 'In between'

    @classmethod
    def is_moving(self, device):
        return BirdbrainRequest.request_status(BirdbrainRequest.response('hummingbird', 'in', 'finchIsMoving', 'static', device))

    @classmethod
    def light(self, device, side):
        """Read the value of the right or left light sensor ('R' or 'L')."""

        return self.sensor(device, 'Light', BirdbrainRequest.calculate_left_or_right(side))

    @classmethod
    def distance(self, device):
        """Read the value of the distance sensor"""

        distance_options = {}
        distance_options['factor'] = BirdbrainConstant.DISTANCE_FACTOR  # was 0.0919
        distance_options['min_response'] = self.DEFAULT_UNLIMITED_MIN_RESPONSE
        distance_options['max_response'] = self.DEFAULT_UNLIMITED_MAX_RESPONSE

        return self.sensor(device, 'Distance', 'static', distance_options)

    @classmethod
    def line(self, device, side):
        """Read the value of the right or left line sensor ('R' or 'L').
        Returns brightness as a value 0-100 where a larger number
        represents more reflected light."""

        return self.sensor(device, 'Line', BirdbrainRequest.calculate_left_or_right(side))

        #direction = self.__formatRightLeft(direction)
        #if direction is None:
        #    return 0

        #response = self.__getSensor("Line", direction)
        #return int(response)

    @classmethod
    def encoder(self, device, side):
        """Read the value of the right or left encoder ('R' or 'L').
        Values are returned in rotations."""

        encoder_options = {}
        encoder_options['min_response'] = float(self.DEFAULT_UNLIMITED_MIN_RESPONSE)
        encoder_options['max_response'] = float(self.DEFAULT_UNLIMITED_MAX_RESPONSE)
        encoder_options['type_method'] = 'float'

        return round(self.sensor(device, 'Encoder', BirdbrainRequest.calculate_left_or_right(side), encoder_options), 2)

    # The following methods override those within the Microbit
    # class to return values within the Finch reference frame.
    @classmethod
    def acceleration(self, device):
        """Gives the acceleration of X,Y,Z in m/sec2, relative
        to the Finch's position."""

        return BirdbrainMicrobitInput.acceleration(device, "finchAccel")

    @classmethod
    def compass(self, device):
        """Returns values 0-359 indicating the orentation of the Earth's
        magnetic field, relative to the Finch's position."""

        encoder_options = {}
        encoder_options['min_response'] = self.DEFAULT_DEGREES_MIN_RESPONSE
        encoder_options['max_response'] = self.DEFAULT_DEGREES_MAX_RESPONSE

        return self.sensor(device, 'finchCompass', 'static', encoder_options)

    @classmethod
    def magnetometer(self, device):
        """Return the values of X,Y,Z of a magnetommeter, relative to the Finch's position."""

        return self.xyz_response(device, "finchMag")

    @classmethod
    def orientation(self, device):
        """Return the orentation of the Finch. Options include:
        "Beak up", "Beak down", "Tilt left", "Tilt right", "Level",
        "Upside down", and "In between"."""

        # check for orientation of each orientation
        for index, target_orientation in enumerate(self.ORIENTATIONS):
            response = self.response("hummingbird", "in", "finchOrientation", target_orientation, device)

            if (response == "true"): return self.ORIENTATION_RESULTS[index]

        # if we are in a state in which none of the above seven states are true
        return self.ORIENTATION_IN_BETWEEN
