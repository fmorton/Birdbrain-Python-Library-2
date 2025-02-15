from birdbrain_constant import BirdbrainConstant
from birdbrain_finch_input import BirdbrainFinchInput
from birdbrain_request import BirdbrainRequest

import time

class BirdbrainFinchOutput(BirdbrainRequest):
    @classmethod
    def beak(self, device, r_intensity, g_intensity, b_intensity):
        """Set beak to a valid intensity. Each intensity should be an integer from 0 to 100."""
        return self.tri_led_response(device, 1, r_intensity, g_intensity, b_intensity, BirdbrainConstant.VALID_BEAK_PORTS)

    @classmethod
    def tail(self, device, port, r_intensity, g_intensity, b_intensity):
        """Set tail to a valid intensity. Port can be specified as 1, 2, 3, 4, or all.
        Each intensity should be an integer from 0 to 100."""

        if not port == "all":
            port = int(port) + 1  # tail starts counting at 2

        return self.tri_led_response(device, port, r_intensity, g_intensity, b_intensity, BirdbrainConstant.VALID_TAIL_PORTS, True)

    @classmethod
    def wait(self, device):
        timeout_time = time.time() + BirdbrainConstant.MOVE_TIMEOUT_SECONDS

        time.sleep(BirdbrainConstant.MOVE_START_WAIT_SECONDS)  # hack to give move/turn time to start before waiting

        while (timeout_time > time.time()) and (BirdbrainFinchInput.is_moving(device)):
            time.sleep(BirdbrainConstant.MOVE_CHECK_MOVING_DELAY)


    @classmethod
    def move(self, device, direction, distance, speed):
        """Move the Finch forward or backward for a given distance at a given speed.
        Direction should be specified as 'F' or 'B'."""
        calc_direction = None

        if direction == BirdbrainConstant.FORWARD: calc_direction = 'Forward'
        if direction == BirdbrainConstant.BACKWARD: calc_direction = 'Backward'

        calc_distance = BirdbrainRequest.bounds(distance, -10000, 10000)
        calc_speed = BirdbrainRequest.bounds(speed, 0, 100)

        response = BirdbrainRequest.response_status('hummingbird', 'out', 'move', device, calc_direction, calc_distance, calc_speed)

        return response

    @classmethod
    def turn(self, device, direction, angle, speed):
        """Turn the Finch right or left to a given angle at a given speed.
        Direction should be specified as 'R' or 'L'."""
        calc_direction = BirdbrainRequest.calculate_left_or_right(direction)
        calc_angle = BirdbrainRequest.bounds(angle, 0, 360)
        calc_speed = BirdbrainRequest.bounds(speed, 0, 100)

        response = BirdbrainRequest.response_status('hummingbird', 'out', 'turn', device, calc_direction, calc_angle, calc_speed)

        self.wait(device)

        return response

    def setMotors(self, leftSpeed, rightSpeed):
        """Set the speed of each motor individually. Speed should be in
        the range of -100 to 100."""

        leftSpeed = self.clampParametersToBounds(leftSpeed, -100, 100)
        rightSpeed = self.clampParametersToBounds(rightSpeed, -100, 100)

        # Send HTTP request
        response = self.__send_httprequest_move("wheels", leftSpeed, rightSpeed, None)
        return response

    def stop(self):
        """Stop the Finch motors."""

        # Send HTTP request
        response = self.__send_httprequest_out("stopFinch", None, None)
        return response

    def resetEncoders(self):
        """Reset both encoder values to 0."""
        response = self.__send_httprequest_out("resetEncoders", None, None)

        # The finch needs a chance to actually reset
        time.sleep(0.2)

        return response
