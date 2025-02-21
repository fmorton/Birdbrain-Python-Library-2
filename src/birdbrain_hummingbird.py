from birdbrain_hummingbird_input import BirdbrainHummingbirdInput
from birdbrain_hummingbird_output import BirdbrainHummingbirdOutput
from birdbrain_microbit import BirdbrainMicrobit
from birdbrain_microbit_input import BirdbrainMicrobitInput
from birdbrain_request import BirdbrainRequest

class BirdbrainHummingbird(BirdbrainMicrobit):
    """Hummingbird Bit Class includes the control of the outputs and inputs
        present on the Hummingbird Bit."""

    def __init__(self, device = 'A', raise_exception_if_no_connection = True):
        device_object = BirdbrainHummingbird.connect(device, raise_exception_if_no_connection)

        if not self.is_hummingbird():
            raise BirdbrainException("Device " + device + " is not a Hummingbird")

    def led(self, port, intensity):
        return BirdbrainHummingbirdOutput.led(self.device, port, intensity)

    def tri_led(self, port, r_int, g_int, b_int, valid_range):
        return BirdbrainHummingbirdOutput.tri_led(self.device, port, r_int, g_int, b_int, valid_range)

    def position_servo(self, port, angle):
        return BirdbrainHummingbirdOutput.position_servo(self.device, port, angle)

    def rotation_servo(self, port, speed):
        return BirdbrainHummingbirdOutput.rotation_servo(self.device, port, speed)

    def distance(self, port):
        return BirdbrainHummingbirdInput.distance(self.device, port)

    def stop_all(self):
        BirdbrainRequest.stop_all(self.device)

    #dial = getDial
    getDistance = distance
    setLED = led
    #light = getLight
    setPositionServo = position_servo
    setRotationServo = rotation_servo
    #sound
    #sensor = getSensor
    stopAll = stop_all
    setTriLED = tri_led
    #voltage = getVoltage
