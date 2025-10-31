from birdbrain.exception import Exception
from birdbrain.hummingbird_input import HummingbirdInput
from birdbrain.hummingbird_output import HummingbirdOutput
from birdbrain.microbit import Microbit
from birdbrain.request import Request


class Hummingbird(Microbit):
    """Hummingbird Bit Class includes the control of the outputs and inputs
    present on the Hummingbird Bit."""

    def __init__(self, device='A', raise_exception_if_no_connection=True):
        self.device_object = Hummingbird.connect(device, raise_exception_if_no_connection)

        if not self.device_object.is_hummingbird():
            raise Exception("Device " + device + " is not a Hummingbird")

    def led(self, port, intensity):
        return HummingbirdOutput.led(self.device, port, intensity)

    def tri_led(self, port, r_int, g_int, b_int):
        return HummingbirdOutput.tri_led(self.device, port, r_int, g_int, b_int)

    def position_servo(self, port, angle):
        return HummingbirdOutput.position_servo(self.device, port, angle)

    def rotation_servo(self, port, speed):
        return HummingbirdOutput.rotation_servo(self.device, port, speed)

    def sensor(self, port):
        return HummingbirdInput.sensor(self.device, port)

    def light(self, port):
        return HummingbirdInput.light(self.device, port)

    def sound(self, port):
        return HummingbirdInput.sound(self.device, port)

    def distance(self, port):
        return HummingbirdInput.distance(self.device, port)

    def dial(self, port):
        return HummingbirdInput.dial(self.device, port)

    def voltage(self, port):
        return HummingbirdInput.voltage(self.device, port)

    def stop_all(self):
        Request.stop_all(self.device)

    getDial = dial
    getDistance = distance
    setLED = led
    getLight = light
    setPositionServo = position_servo
    setRotationServo = rotation_servo
    getSound = sound
    getSensor = sensor
    stopAll = stop_all
    setTriLED = tri_led
    getVoltage = voltage
