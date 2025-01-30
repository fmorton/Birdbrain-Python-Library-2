import time

from BirdBrain import Finch

def test_no_device():
    finch = Finch('C')

def test_is():
    finch = BirdbrainFinch.connect("B")

    assert not finch.is_microbit()
    assert finch.is_hummingbird()
    assert not finch.is_finch()

def test_beak():
    finch = Finch('B')

    for i in range(0, 10):
        finch.setBeak(100, 100, 100)
        time.sleep(0.1)
        finch.setBeak(0, 0, 0)
        time.sleep(0.1)

        finch.stopAll()
