from birdbrain_constant import BirdbrainConstant
from birdbrain_finch_input import BirdbrainFinchInput
from birdbrain_finch_output import BirdbrainFinchOutput
from birdbrain_microbit import BirdbrainMicrobit

class BirdbrainFinch(BirdbrainMicrobit):
    """The Finch class includes the control of the outputs and inputs present
    in the Finch robot. When creating an instance, specify which robot by the
    device letter used in the BlueBirdConnector device list (A, B, or C)."""
    #attr_accessor :move_start_wait_seconds
    #attr_accessor :move_start_time
    #attr_accessor :move_timeout_seconds

    def __init__(self, device='A', raise_exception_if_no_connection = True):
        """Class initializer. """
        #self.move_start_wait_seconds = BirdbrainConstant.MOVE_START_WAIT_SECONDS # seconds to allow finch to start moving
        #self.move_timeout_seconds = BirdbrainConstant.MOVE_TIMEOUT_SECONDS # maximum number of seconds to wait for finch moving
        #self.move_start_time = 0 # after move records how long it took the startup to complete for tuning
        self.device_object = BirdbrainFinch.connect(device, raise_exception_if_no_connection)

        if not self.is_finch():
            raise BirdbrainException("Error: Device " + device + " is not a Finch")

    def beak(self, r_intensity, g_intensity, b_intensity):
        return BirdbrainFinchOutput.beak(self.device, r_intensity, g_intensity, b_intensity)

    def tail(self, port, r_intensity, g_intensity, b_intensity):
        return BirdbrainFinchOutput.tail(self.device, port, r_intensity, g_intensity, b_intensity)

    def move(self, direction, distance, speed):
        return BirdbrainFinchOutput.move(self.device, direction, distance, speed)

    def turn(self, direction, angle, speed):
        return BirdbrainFinchOutput.turn(self.device, direction, angle, speed)

    def is_moving(self):
        return BirdbrainFinchInput.is_moving(self.device)

    # Finch Aliases
    #acceleration = getAcceleration
    setBeak = beak
    #compass = getCompass
    #distance = getDistance
    #encoder = getEncoder
    #light = getLight
    #line = getLine
    #magnetometer = getMagnetometer
    #motors = setMotors
    setMove = move
    #orientation = getOrientation
    #reset_encoders = resetEncoders
    setTail = tail
    setTurn = turn
