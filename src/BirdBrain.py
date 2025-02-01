# --------------------------------------------------------------
# Author                  Raghunath J, revised by Bambi Brewer
#                         and Kristina Lauwers
# Last Edit Date          11/20/2019
# Description             This python file contains Microbit,
# Hummingbird, and Finch classes.
# The Microbit class controls a micro:bit via bluetooth. It
# includes methods to print on the micro:bit LED array or set
# those LEDs individually. It also contains methods to read the
# values of the micro:bit accelerometer and magnetometer.
# The Hummingbird class extends the Microbit class to incorporate
# functions to control the inputs and outputs of the Hummingbird
# Bit. It includes methods to set the values of motors and LEDs,
# as well as methods to read the values of the sensors.
# The Finch class also extends the Microbit class. This class
# similarly includes function to control the inputs and outputs
# of the Finch robot.
# --------------------------------------------------------------
import sys
import time

import urllib.request

from birdbrain_microbit import BirdbrainMicrobit
from birdbrain_hummingbird import BirdbrainHummingbird
from birdbrain_finch import BirdbrainFinch
