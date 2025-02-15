from birdbrain_device import BirdbrainDevice
from birdbrain_exception import BirdbrainException
from birdbrain_microbit_output import BirdbrainMicrobitOutput

class BirdbrainMicrobit(BirdbrainDevice):
    def __init__(self, device = 'A', raise_exception_if_no_connection = True):
        self.device_object = BirdbrainMicrobit.connect(device, raise_exception_if_no_connection)

        if not self.is_microbit():
            raise BirdbrainException("Error: Device " + device + " is not a Microbit")

    def microbit_display(self, list):
        return BirdbrainMicrobitOutput.microbit_display(self.state, self.device, list)

    def microbit_clear_display(self):
        return BirdbrainMicrobitOutput.microbit_clear_display(self.state, self.device)

    def microbit_point(self, x, y, value):
        return BirdbrainMicrobitOutput.microbit_point(self.state, self.device, x, y, value)

    def microbit_print(self, message):
        return BirdbrainMicrobitOutput.microbit_print(self.state, self.device, message)

    def microbit_play_note(self, note, beats):
        return BirdbrainMicrobitOutput.microbit_play_note(self.device, note, beats)

    def beep(self):
        return BirdbrainMicrobitOutput.microbit_play_note(self.device, 80, 0.333)

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

    #  aliases
    #acceleration = getAcceleration
    #button = getButton
    #compass = getCompass
    setDisplay = microbit_display
    #isMicrobit = is_microbit
    #is_shaking = isShaking
    #magnetometer = getMagnetometer
    #orientation = getOrientation
    playNote = microbit_play_note
    setPoint = microbit_point
    #sound = getSound
    #stop_all = stopAll
    #temperature = getTemperature
