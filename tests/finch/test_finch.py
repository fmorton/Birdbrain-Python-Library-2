import time

from BirdBrain import BirdbrainFinch

def test_is():
    finch = BirdbrainFinch.connect("B")

    assert finch.is_connected()
    assert not finch.is_microbit()
    assert not finch.is_hummingbird()
    assert finch.is_finch()

def test_beak_with_alias():
    finch = BirdbrainFinch('B')

    finch.beak(100, 50, 50)
    time.sleep(0.5)
    finch.setBeak(0, 0, 0)

def test_tail_with_alias():
    finch = BirdbrainFinch("B")

    assert finch.tail(1, 10, 0, 50)
    time.sleep(0.5)
    assert finch.tail(1, "50", 0, "0")
    time.sleep(0.5)
    assert finch.tail("2", "50", 0, "0")
    time.sleep(0.5)
    assert finch.tail(3, "50", 0, "0")
    time.sleep(0.5)
    assert finch.tail(4, "50", 0, "0")
    time.sleep(0.5)
    assert finch.tail("all", 100, 0, 100)
    time.sleep(0.5)
    assert finch.setTail("all", 0, 0, 0)
