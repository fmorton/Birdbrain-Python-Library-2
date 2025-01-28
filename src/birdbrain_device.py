from birdbrain_exception import BirdbrainException
from birdbrain_state import BirdbrainState

class BirdbrainDevice:
    VALID_DEVICES = 'ABC'

    ##########device = None

    def __init__(self, device = 'A'):
        self.state = BirdbrainState()
        self.device = BirdbrainDevice.remap_device(device)
        self.device = device
        self.connected = False

    @classmethod
    def connect(self, device, raise_exception_if_no_connection = False):
        device_object = BirdbrainDevice(device)

        ###device_object.device = device

        if device is None: raise BirdbrainException("Missing device name")
        if (not device in BirdbrainDevice.VALID_DEVICES): raise BirdbrainException("Invalid device name: " + device)

        return device_object


    def remap_device(device):
        return device