from birdbrain_constant import BirdbrainConstant
from birdbrain_exception import BirdbrainException
from birdbrain_request import BirdbrainRequest
from birdbrain_state import BirdbrainState

class BirdbrainDevice:
    def __init__(self, device = "A", raise_exception_if_no_connection = True):
        self.state = BirdbrainState()
        self.device = BirdbrainDevice.remap_device(device)
        self.connected = False

    @classmethod
    def connect(self, device = "A", raise_exception_if_no_connection = True):
        device_object = BirdbrainDevice(device)

        self.state = device_object.state
        self.device = device_object.device
        self.connected = device_object.connected

        if device is None:
            raise BirdbrainException("Missing device name")
        if not device in BirdbrainConstant.VALID_DEVICES:
            raise BirdbrainException("Invalid device name: " + device)

        self.connected = device_object.connect_device()

        if raise_exception_if_no_connection and not device_object.connected:
            raise BirdbrainException("No connection: " + device)

        return device_object

    def is_connected(self):
        """Determine if the device is connected"""

        return self.connected

    def __is_device(self, operator):
        response = BirdbrainRequest.response("hummingbird", "in", operator, "static", self.device)

        return (response == 'true')

    def is_microbit(self):
        """Determine if the device is a Microbit"""

        return self.__is_device("isMicrobit")

    def is_hummingbird(self):
        """Determine if the device is a hummingbird."""
        return self.__is_device("isHummingbird")

    def is_finch(self):
        """Determine if the device is a Finch"""

        return self.__is_device("isFinch")

    def is_valid(self, validate, valid_range):
        if validate is None: return False

        return str(validate) in valid_range

    def is_connected_and_valid(self, validate, valid_range):
        return self.is_valid(validate, valid_range) and self.is_connected()

    def remap_device(device):
        return device

    def connect_device(self):
        self.connected = BirdbrainRequest.is_connected(self.device)

        return self.connected
