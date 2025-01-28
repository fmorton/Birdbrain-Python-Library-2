class BirdbrainState:
    def __init__(self):
        self.microbit_display_map = BirdbrainState.microbit_empty_display_map()

    def microbit_display_map_clear(self):
        self.microbit_display_map = BirdbrainState.microbit_empty_display_map

    #DEBUG: index calculation may be wrong
    def set_pixel(self, x, y, value):
        self.microbit_display_map[((x * 5) + y - 6)] = value

    def microbit_display_map_as_strings(self):
        return(["true" if pixel == 1 else "false" for pixel in self.microbit_display_map])
    
    @classmethod
    def microbit_empty_display_map(self):
        return([0] * 25)