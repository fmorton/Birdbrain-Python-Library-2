import sys
import time

import urllib.request

from birdbrain_exception import BirdbrainException
from birdbrain_microbit import BirdbrainMicrobit
from birdbrain_request import BirdbrainRequest

class BirdbrainHummingbirdOutput(BirdbrainRequest):
    @classmethod
    def led(self, device, port, intensity):
        self.validate_port(port)

        """Set led  of a certain port requested to a valid intensity."""
        calculated_intensity = BirdbrainRequest.bounds(BirdbrainRequest.calculate_intensity(intensity), 0, 255)

        return BirdbrainRequest.response_status('hummingbird', 'out', 'led', port, calculated_intensity, device)

    @classmethod
    def tri_led(self, device, port, r_intensity, g_intensity, b_intensity):
        """Set TriLED  of a certain port requested to a valid intensity."""
        self.validate_port(port)

        # Check the intensity value lies with in the range of RGB LED limits
        calc_r = BirdbrainRequest.bounds(r_intensity, 0, 100)
        calc_g = BirdbrainRequest.bounds(g_intensity, 0, 100)
        calc_b = BirdbrainRequest.bounds(b_intensity, 0, 100)

        return BirdbrainRequest.response_status('hummingbird', 'out', 'triled', port, calc_r, calc_g, calc_b, device)

    def setPositionServo(self, port, angle):
        """Set Position servo of a certain port requested to a valid angle."""

        # Early return if we can't execute the command because the port is invalid
        if not self.isPortValid(port, 4):
            return

        # Check the angle lies within servo limits
        angle = self.clampParametersToBounds(angle, 0, 180)

        angle_c = self.calculate_servo_p(angle)
        # Send HTTP request
        response = self.send_httprequest("servo", port, angle_c)
        return response

    def setRotationServo(self, port, speed):
        """Set Rotation servo of a certain port requested to a valid speed."""

        # Early return if we can't execute the command because the port is invalid
        if not self.isPortValid(port, 4):
            return

        # Check the speed lies within servo limits
        speed = self.clampParametersToBounds(speed, -100, 100)

        speed_c = self.calculate_servo_r(speed)
        # Send HTTP request
        response = self.send_httprequest("rotation", port, speed_c)
        return response


