from birdbrain_exception import BirdbrainException
from birdbrain_request import BirdbrainRequest
from birdbrain_state import BirdbrainState

class BirdbrainDevice:
    VALID_DEVICES = 'ABC'

    def __init__(self, device = 'A'):
        self.state = BirdbrainState()
        self.device = BirdbrainDevice.remap_device(device)
        self.connected = False

    @classmethod
    def connect(self, device = "A", raise_exception_if_no_connection = False):
        if device is None: raise BirdbrainException("Missing device name")
        if (not device in BirdbrainDevice.VALID_DEVICES): raise BirdbrainException("Invalid device name: " + device)

        device_object = BirdbrainDevice(device)

        device_object.connect_device()

        if raise_exception_if_no_connection and not device_object.connected:
            raise BirdbrainException("No connection: " + device)

        return device_object

    def remap_device(device):
        return device

    def connect_device(self):
        self.connected = BirdbrainRequest.is_connected(self.device)
