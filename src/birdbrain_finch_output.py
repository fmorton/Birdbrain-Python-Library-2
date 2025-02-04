from birdbrain_constant import BirdbrainConstant
from birdbrain_request import BirdbrainRequest

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

    def __moveFinchAndWait(self, motion, direction, length, speed):
        """Send a command to move the finch and wait until the finch has finished
        its motion to return. Used by setMove and setTurn."""

        isMoving = self.__send_httprequest_in("finchIsMoving", "static")
        wasMoving = isMoving
        commandSendTime = time.time()
        done = False

        # Send HTTP request
        response = self.__send_httprequest_move(motion, direction, length, speed)

        while (not (done) and not (isMoving == "Not Connected")):
            wasMoving = isMoving
            time.sleep(0.01)
            isMoving = self.__send_httprequest_in("finchIsMoving", "static")
            done = ((time.time() > commandSendTime + 0.5) or (wasMoving == "true")) and (isMoving == "false")

        return response

    def setMove(self, direction, distance, speed):
        """Move the Finch forward or backward for a given distance at a given speed.
        Direction should be specified as 'F' or 'B'."""

        direction = self.__formatForwardBackward(direction)
        if direction is None:
            return 0

        distance = self.clampParametersToBounds(distance, -10000, 10000)
        speed = self.clampParametersToBounds(speed, 0, 100)

        response = self.__moveFinchAndWait("move", direction, distance, speed)

        return response

    def setTurn(self, direction, angle, speed):
        """Turn the Finch right or left to a given angle at a given speed.
        Direction should be specified as 'R' or 'L'."""

        direction = self.__formatRightLeft(direction)
        if direction is None:
            return 0

        angle = self.clampParametersToBounds(angle, -360000, 360000)
        speed = self.clampParametersToBounds(speed, 0, 100)

        response = self.__moveFinchAndWait("turn", direction, angle, speed)

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
