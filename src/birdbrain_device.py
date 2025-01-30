from birdbrain_exception import BirdbrainException
from birdbrain_request import BirdbrainRequest
from birdbrain_state import BirdbrainState


class BirdbrainDevice:
    VALID_DEVICES = "ABC"

    def __init__(self, device="A"):
        self.state = BirdbrainState()
        self.device = BirdbrainDevice.remap_device(device)
        self.connected = False

    @classmethod
    def connect(self, device = "A", raise_exception_if_no_connection = False):
        device_object = BirdbrainDevice(device)

        if device is None:
            raise BirdbrainException("Missing device name")
        if not device in BirdbrainDevice.VALID_DEVICES:
            raise BirdbrainException("Invalid device name: " + device)

        device_object.connect_device()

        if raise_exception_if_no_connection and not device_object.connected:
            raise BirdbrainException("No connection: " + device)

        return device_object

    def is_device(self, operator):
        response = BirdbrainRequest.response("hummingbird", "in", operator, "static", self.device)

        return (response == 'true')

    def is_microbit(self):
        """Determine if the device is a Microbit"""

        return self.is_device("isMicrobit")

    def is_hummingbird(self):
        """Determine if the device is a hummingbird."""

        return self.is_device("isHummingbird")

    def is_finch(self):
        """Determine if the device is a Finch"""

        return self.is_device("isFinch")

    def remap_device(device):
        return device

    def connect_device(self):
        self.connected = BirdbrainRequest.is_connected(self.device)
