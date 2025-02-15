from birdbrain_constant import BirdbrainConstant
from birdbrain_finch_input import BirdbrainFinchInput
from birdbrain_finch_output import BirdbrainFinchOutput
from birdbrain_microbit import BirdbrainMicrobit

class BirdbrainFinch(BirdbrainMicrobit):
    """The Finch class includes the control of the outputs and inputs present
    in the Finch robot. When creating an instance, specify which robot by the
    device letter used in the BlueBirdConnector device list (A, B, or C)."""

    def __init__(self, device='A', raise_exception_if_no_connection = True):
        """Class initializer. """
        self.device_object = BirdbrainFinch.connect(device, raise_exception_if_no_connection)

        if not self.is_finch():
            raise BirdbrainException("Error: Device " + device + " is not a Finch")

    def beak(self, r_intensity, g_intensity, b_intensity):
        return BirdbrainFinchOutput.beak(self.device, r_intensity, g_intensity, b_intensity)

    def tail(self, port, r_intensity, g_intensity, b_intensity):
        return BirdbrainFinchOutput.tail(self.device, port, r_intensity, g_intensity, b_intensity)

    def move(self, direction, distance, speed, wait_to_finish_movement = True):
        return BirdbrainFinchOutput.move(self.device, direction, distance, speed, wait_to_finish_movement)

    def turn(self, direction, angle, speed, wait_to_finish_movement = True):
        return BirdbrainFinchOutput.turn(self.device, direction, angle, speed, wait_to_finish_movement)

    def motors(self, left_speed, right_speed):
        return BirdbrainFinchOutput.motors(self.device, left_speed, right_speed)

    def wait(self, device):
        return BirdbrainFinchOutput.wait(self.device)

    def stop(self):
        return BirdbrainFinchOutput.stop(self.device)

    def reset_encoders(self):
        return BirdbrainFinchOutput.reset_encoders(self.device)

    def is_moving(self):
        return BirdbrainFinchInput.is_moving(self.device)

    #  aliases
    #acceleration = getAcceleration
    setBeak = beak
    #compass = getCompass
    #distance = getDistance
    #encoder = getEncoder
    #light = getLight
    #line = getLine
    #magnetometer = getMagnetometer
    setMotors = motors
    setMove = move
    #orientation = getOrientation
    resetEncoders = reset_encoders
    setTail = tail
    setTurn = turn
