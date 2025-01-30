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

    def is_hummingbird(self):
        """Determine if the device is a hummingbird."""

        response = BirdbrainRequest.response("hummingbird", "in", "isHummingbird", "static" + self.device)

        # old versions of bluebird connector don't support this request
        if response != "true": return True

        # try to read sensor 4. the value will be 255 for a micro:bit (there is no sensor 4)
        # and some other value for the hummingbird
        response = BirdbrainRequest.response("hummingbird", "in", "sensor", "4", self.device)

        return response != "255"

    def is_finch(self):
        """Determine if the device is a Finch"""

        response = BirdbrainRequest.response("hummingbird", "in", "isFinch", "static", self.device)

        return (response == 'true')

    def remap_device(device):
        return device

    def connect_device(self):
        self.connected = BirdbrainRequest.is_connected(self.device)
