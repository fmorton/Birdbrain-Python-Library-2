from birdbrain_state import BirdbrainState

def test_state():
    state = BirdbrainState()

    for pixel in state.microbit_display_map:
        assert pixel == 0

    assert state.microbit_display_map[0] == 0
    assert state.microbit_display_map[18] == 0

    state.set_pixel(1, 1, 1)
    state.set_pixel(4, 4, 1)
    
    assert state.microbit_display_map[0] == 1
    assert state.microbit_display_map[18] == 1
    assert state.microbit_display_map[1] == 0
    assert state.microbit_display_map[19] == 0

    s = state.microbit_display_map_as_strings()

    assert s[0] == "true"
    assert s[18] == "true"
    assert s[1] == "false"
    assert s[19] == "false"
