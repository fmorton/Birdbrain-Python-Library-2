from birdbrain_exception import BirdbrainException
from birdbrain_utility import BirdbrainUtility

import time
import urllib.request

class BirdbrainRequest:
    BIRDBRAIN_TEST = True

    @classmethod
    def uri(self, *args):
        return("http://127.0.0.1:30061/" + BirdbrainUtility.flatten_string(args[0]))

    @classmethod
    def is_not_connected_response(self, response):
        return((response.lower() == "not connected"))

    @classmethod
    def response(self, *args):
        if "false" in args: return False

        try:
            if BirdbrainRequest.BIRDBRAIN_TEST: print("Test:", self.uri(args))

            response_request = urllib.request.urlopen(self.uri(args))
        except (ConnectionError, urllib.error.URLError):
            raise(BirdbrainException("Error: Request to device failed"))

        response = response_request.read().decode('utf-8').lower()

        if (self.is_not_connected_response(response)): raise(BirdbrainException("Error: The device is not connected"))

        time.sleep(0.01)  # Hack to prevent http requests from overloading the BlueBird Connector

        return response

    @classmethod
    def is_connected(self, device):
        try:
            response = self.response('hummingbird', 'in', 'orientation', 'Shake', device)
        except BirdbrainException:
            return False

        return True

    @classmethod
    def is_not_connected(self, device):
        return(not self.is_connected(device))

    @classmethod
    def stop_all(self, device):
        return(self.request_status(self.response('hummingbird', 'out', 'stopall', device)))

    @classmethod
    def request_status(self, status):
     if BirdbrainRequest.BIRDBRAIN_TEST: print("Test: request status is", status)

     if status is None: return None

     if status == 'true': return(True)
     if status == 'led set': return(True)
     if status == 'triled set': return(True)
     if status == 'servo set': return(True)
     if status == 'buzzer set': return(True)
     if status == 'symbol set': return(True)
     if status == 'print set': return(True)
     if status == 'all stopped': return(True)

     if status == 'finch moved': return(True)
     if status == 'finch turned': return(True)
     if status == 'finch wheels started': return(True)
     if status == 'finch wheels stopped': return(True)
     if status == 'finch encoders reset': return(True)

     if status == 'false': return(False)
     if status == 'not connected': return(False)
     if status == 'invalid orientation': return(False)

     return(None)
