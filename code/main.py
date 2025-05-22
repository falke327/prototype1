from Motor import Motor
from MotorDriver import MotorDriver
try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    import RPi_Mock as GPIO

import time

if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    try:
        left_motor = Motor(pin_forward=15, pin_backward=16)
        right_motor = Motor(pin_forward=18, pin_backward=22)
        driver = MotorDriver(left_motor, right_motor)

        print("Vorwärtsfahrt")
        driver.forward()
        time.sleep(2)

        print("Rechtsdrehung")
        driver.rotate_right()
        time.sleep(1)

        print("Stopp")
        driver.stop()

    finally:
        GPIO.cleanup()
