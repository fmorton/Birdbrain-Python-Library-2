import inspect

from birdbrain_constant import BirdbrainConstant
from birdbrain_request import BirdbrainRequest

class BirdbrainMicrobitInput(BirdbrainRequest):
    @classmethod
    def acceleration(self, device, sensor = "Accelerometer"):
        """Gives the acceleration of X,Y,Z in m/sec2."""

        return self.xyz_response(device, sensor, "float")

    @classmethod
    def compass(self, device, sensor = 'Compass'):
        """Returns values 0-359 indicating the orentation of the Earth's
        magnetic field."""

        encoder_options = {}
        encoder_options['min_response'] = BirdbrainConstant.DEFAULT_DEGREES_MIN_RESPONSE
        encoder_options['max_response'] = BirdbrainConstant.DEFAULT_DEGREES_MAX_RESPONSE

        sensor_option = None if sensor == 'Compass' else 'static'

        return self.sensor_response(device, sensor, sensor_option, encoder_options)

    @classmethod
    def magnetometer(self, device, sensor = "Magnetometer"):
        """Return the values of X,Y,Z of a magnetommeter."""
        return self.xyz_response(device, sensor, "int")

    @classmethod
    def button(self, device, button):
        """Return the status of the button asked. Specify button 'A', 'B', or
        'Logo'. Logo available for V2 micro:bit only."""

        return self.request_status(self.response('hummingbird', 'in', 'button', button.capitalize(), device))

    @classmethod
    def sound(self, device):
        """Return the current sound level as an integer between 1 and 100.
        Available for V2 micro:bit only."""

        response = self.response('hummingbird', 'in', "V2sensor", "Sound", device)

        if response == 'micro:bit v2 required': return 0

        return int(response)

    @classmethod
    def temperature(self, device):
        """Return the current temperature as an integer in degrees Celcius.
        Available for V2 micro:bit only."""

        response = self.response('hummingbird', 'in', "V2sensor", "Temperature", device)

        if response == 'micro:bit v2 required': return 0

        return int(response)

    def isShaking(self):
        """Return true if the device is shaking, false otherwise."""

        # Send HTTP request
        response = self.send_httprequest_micro_in("Shake", None)
        if (response == "true"):  # convert to boolean
            shake = True
        else:
            shake = False

        return shake

    def getOrientation(self):
        """Return the orentation of the micro:bit. Options include:
        "Screen up", "Screen down", "Tilt left", "Tilt right", "Logo up",
        "Logo down", and "In between"."""

        orientations = ["Screen%20Up", "Screen%20Down", "Tilt%20Left", "Tilt%20Right", "Logo%20Up", "Logo%20Down"]
        orientation_result = ["Screen up", "Screen down", "Tilt left", "Tilt right", "Logo up", "Logo down"]

        # Check for orientation of each device and if true return that state
        for targetOrientation in orientations:
            response = self.send_httprequest_micro_in(targetOrientation, None)
            if (response == "true"):
                return orientation_result[orientations.index(targetOrientation)]

        # If we are in a state in which none of the above seven states are true
        return "In between"

    def stopAll(self):
        """Stop all device outputs (ie. Servos, LEDs, LED Array, Motors, etc.)."""

        time.sleep(0.1)  # hack to give stopAll() time to act before the end of a program

        response = self.send_httprequest_stopAll()
        self.symbolvalue = [0]*25
        return response

    #def send_httprequest_micro_in(self, peri, value):
    #    """Utility function to arrange and send the http request for microbit input functions."""
    #    if (peri == "Accelerometer"):
    #        http_request = self.base_request_in + "/" + peri + "/" + str(value) + "/" + str(self.device_s_no)
    #    elif (peri == "Compass"):
    #        http_request = self.base_request_in + "/" + peri + "/" + str(self.device_s_no)
    #    elif (peri == "Magnetometer"):
    #        http_request = self.base_request_in + "/" + peri + "/" + str(value) + "/" + str(self.device_s_no)
    #    elif (peri == "button"):
    #        http_request = self.base_request_in + "/" + peri + "/" + str(value) + "/" + str(self.device_s_no)
    #    elif (peri == "Shake"):
    #        http_request = self.base_request_in + "/" + "orientation" + "/" + peri + "/" + str(self.device_s_no)
    #    elif (peri == "Screen%20Up"):
    #        http_request = self.base_request_in + "/" + "orientation" + "/" + peri + "/" + str(self.device_s_no)
    #    elif (peri == "Screen%20Down"):
    #        http_request = self.base_request_in + "/" + "orientation" + "/" + peri + "/" + str(self.device_s_no)
    #    elif (peri == "Tilt%20Right"):
    #        http_request = self.base_request_in + "/" + "orientation" + "/" + peri + "/" + str(self.device_s_no)
    #    elif (peri == "Tilt%20Left"):
    #        http_request = self.base_request_in + "/" + "orientation" + "/" + peri + "/" + str(self.device_s_no)
    #    elif (peri == "Logo%20Up"):
    #        http_request = self.base_request_in + "/" + "orientation" + "/" + peri + "/" + str(self.device_s_no)
    #    elif (peri == "Logo%20Down"):
    #        http_request = self.base_request_in + "/" + "orientation" + "/" + peri + "/" + str(self.device_s_no)
    #    else:
    #        http_request = self.base_request_in + "/" + peri + "/" + str(value) + "/" + str(self.device_s_no)
    #    try:
    #        response_request = urllib.request.urlopen(http_request)
    #    except (ConnectionError, urllib.error.URLError):
    #        print(CONNECTION_SERVER_CLOSED)
    #        sys.exit()
    #    response = response_request.read().decode('utf-8')
    #    if (response == "Not Connected"):
    #        print(NO_CONNECTION)
    #        sys.exit()
    #    time.sleep(0.01)  # hack to prevent http requests from overloading the BlueBird Connector
    #    return response
