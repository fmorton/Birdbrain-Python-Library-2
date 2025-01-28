from birdbrain_exception import BirdbrainException
from birdbrain_utility import BirdbrainUtility

import time
import urllib.request

class BirdbrainRequest:
    BIRDBRAIN_TEST = False

    @classmethod
    def uri(self, *args):
        return("http://127.0.0.1:30061/hummingbird/" + BirdbrainUtility.flatten_string(args[0]))

    @classmethod
    def response(self, *args):
        if "false" in args: return False

        try:
            response_request = urllib.request.urlopen(self.uri(args))
        except (ConnectionError, urllib.error.URLError):
            raise(BirdbrainException("Error: Request to device failed"))

        response = response_request.read().decode('utf-8')

        if (response == "Not Connected"): raise(BirdbrainException("Error: The device is not connected"))

        time.sleep(0.01)  # Hack to prevent http requests from overloading the BlueBird Connector

        return response
