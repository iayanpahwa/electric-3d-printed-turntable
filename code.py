import board
from analogio import AnalogIn
import simpleio
from time import sleep
from adafruit_motorkit import MotorKit


kit = MotorKit(i2c=board.I2C())


trimpot = AnalogIn(board.A5)  # pot pin for servo control


while True:

    angle = simpleio.map_range(trimpot.value, 256, 65535, 0.02, 1)
    print(angle)
    kit.motor3.throttle = angle
    sleep(1)

