import sys
import time

import urllib.request

from birdbrain_exception import BirdbrainException
from birdbrain_microbit import BirdbrainMicrobit

class BirdbrainHummingbirdOutput(BirdbrainRequest):
    # -------------------------------------------------------------------------
    # HUMMINGBIRD BIT OUTPUT
    # -------------------------------------------------------------------------
    def setLED(self, port, intensity):
        """Set LED  of a certain port requested to a valid intensity."""

        # Early return if we can't execute the command because the port is invalid
        if not self.isPortValid(port, 3):
            return

        # Check the intensity value lies with in the range of LED limits
        intensity = self.clampParametersToBounds(intensity, 0, 100)

        # Change the range from 0-100 to 0-255
        intensity_c = self.calculate_LED(intensity)
        # Send HTTP request
        response = self.send_httprequest("led", port, intensity_c)
        return response

    def setTriLED(self, port, redIntensity, greenIntensity, blueIntensity):
        """Set TriLED  of a certain port requested to a valid intensity."""

        # Early return if we can't execute the command because the port is invalid
        if not self.isPortValid(port, 2):
            return

        # Check the intensity value lies with in the range of RGB LED limits
        red = self.clampParametersToBounds(redIntensity, 0, 100)
        green = self.clampParametersToBounds(greenIntensity, 0, 100)
        blue = self.clampParametersToBounds(blueIntensity, 0, 100)

        # Change the range from 0-100 to 0-255
        (r_intensity_c, g_intensity_c, b_intensity_c) = self.calculate_RGB(red, green, blue)
        # Send HTTP request
        response = self.send_httprequest("triled", port, str(r_intensity_c) + "/" + str(g_intensity_c) + "/" + str(b_intensity_c))
        return response

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


