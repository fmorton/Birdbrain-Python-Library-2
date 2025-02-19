from birdbrain_microbit_input import BirdbrainMicrobitInput

def test_acceleration():
    response = BirdbrainMicrobitInput.acceleration("A", "Accelerometer")
    response = BirdbrainMicrobitInput.acceleration("A")

    assert (-100.0 <= response[0] <= 100.0)
    assert (-100.0 <= response[1] <= 100.0)
    assert (-100.0 <= response[2] <= 100.0)

    assert isinstance(response[0], float)
    assert isinstance(response[1], float)
    assert isinstance(response[2], float)
