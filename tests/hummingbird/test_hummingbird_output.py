import pytest
import time

from birdbrain_exception import BirdbrainException
from birdbrain_microbit import BirdbrainMicrobit
from birdbrain_hummingbird_output import BirdbrainHummingbirdOutput
from BirdBrain import BirdbrainHummingbird

def test_led():
    hummingbird = BirdbrainHummingbird("A")

    BirdbrainHummingbirdOutput.led(hummingbird.device, 1, 50)
    time.sleep(0.25)

    BirdbrainHummingbirdOutput.led(hummingbird.device, 1, "0")

def test_triled():
    hummingbird = BirdbrainHummingbird("A")

    BirdbrainHummingbirdOutput.tri_led(hummingbird.device, 1, 50, "50", 0)
    time.sleep(0.25)

    BirdbrainHummingbirdOutput.tri_led(hummingbird.device, 1, 0, 0, 0)
