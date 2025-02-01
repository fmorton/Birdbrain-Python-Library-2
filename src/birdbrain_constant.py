class BirdbrainConstant:
    BACKWARD = 'B'
    BIRDBRAIN_TEST = False
    DEFAULT_DEVICE = 'A'
    FORWARD = 'F'
    LEFT = 'L'
    MOVE_START_WAIT_SECONDS = 0.15
    MOVE_TIMEOUT_SECONDS = 60.0
    RIGHT = 'R'
    VALID_DEVICES = 'ABC'
    VALID_LED_PORTS = '123'
    VALID_MOVE_DIRECTION = 'FB'
    VALID_SENSOR_PORTS = '123'
    VALID_SERVO_PORTS = '1234'
    VALID_TAIL_PORTS = '1234all'
    VALID_TRILED_PORTS = '1234'
    VALID_TURN_DIRECTION = 'LR'


    #DEBUG: TBD if these are needed
    CHAR_FLASH_TIME = 0.3  # Character Flash time

    # Error strings
    CONNECTION_SERVER_CLOSED = "Error: Request to device failed"
    NO_CONNECTION = "Error: The device is not connected"

    # Calculations after receveing the raw values for Hummingbird
    DISTANCE_FACTOR = 117/100
    SOUND_FACTOR = 200/255
    DIAL_FACTOR = 100/230
    LIGHT_FACTOR = 100/255
    VOLTAGE_FACTOR = 3.3/255

    # Scaling factors for Finch
    BATTERY_FACTOR = 0.0406

    TEMPO = 60
