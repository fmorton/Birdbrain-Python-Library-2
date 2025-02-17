from birdbrain_constant import BirdbrainConstant
from birdbrain_request import BirdbrainRequest
from birdbrain_utility import BirdbrainUtility

class BirdbrainFinchInput(BirdbrainRequest):
    DEFAULT_FACTOR = 1.0
    DEFAULT_MIN_RESPONSE = 0.0
    DEFAULT_MAX_RESPONSE = 100.0
    DEFAULT_TYPE_METHOD = 'int'
    DEFAULT_UNLIMITED_MIN_RESPONSE = -1000000
    DEFAULT_UNLIMITED_MAX_RESPONSE = 1000000
    #ORIENTATIONS = ['Beak%20Up', 'Beak%20Down', 'Tilt%20Left', 'Tilt%20Right', 'Level', 'Upside%20Down']
    #ORIENTATION_RESULTS = ['Beak up', 'Beak down', 'Tilt left', 'Tilt right', 'Level', 'Upside down', 'In between']
    #ORIENTATION_IN_BETWEEN = 'In between'

    @classmethod
    def is_moving(self, device):
        return BirdbrainRequest.request_status(BirdbrainRequest.response('hummingbird', 'in', 'finchIsMoving', 'static', device))

    @classmethod
    def light(self, device, side):
        """Read the value of the right or left light sensor ('R' or 'L')."""

        return self.__sensor(device, 'Light', BirdbrainRequest.calculate_left_or_right(side))

    @classmethod
    def distance(self, device):
        """Read the value of the distance sensor"""

        distance_options = {}
        distance_options['factor'] = BirdbrainConstant.DISTANCE_FACTOR  # was 0.0919
        distance_options['min_response'] = self.DEFAULT_UNLIMITED_MIN_RESPONSE
        distance_options['max_response'] = self.DEFAULT_UNLIMITED_MAX_RESPONSE

        return self.__sensor(device, 'Distance', 'static', distance_options)

    @classmethod
    def line(self, device, side):
        """Read the value of the right or left line sensor ('R' or 'L').
        Returns brightness as a value 0-100 where a larger number
        represents more reflected light."""

        return self.__sensor(device, 'Line', BirdbrainRequest.calculate_left_or_right(side))

        #direction = self.__formatRightLeft(direction)
        #if direction is None:
        #    return 0

        #response = self.__getSensor("Line", direction)
        #return int(response)

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

    @classmethod
    def __sensor(self, device, sensor, other = None, options = {}):
        if other is False: return False   # for invalid directions

        factor = options["factor"] if "factor" in options else self.DEFAULT_FACTOR
        min_response = options["min_response"] if "min_response" in options else self.DEFAULT_MIN_RESPONSE
        max_response = options["max_response"] if "max_response" in options else self.DEFAULT_MAX_RESPONSE
        type_method = options["type_method"] if "type_method" in options else self.DEFAULT_TYPE_METHOD

        request = ['hummingbird', 'in', sensor]
        if other is not None: request.append(other)
        request.append(device)

        response = (float(BirdbrainRequest.response(request)) * factor)

        response = BirdbrainUtility.decimal_bounds(response, min_response, max_response)

        if type_method == 'int': return int(response)

        return response
