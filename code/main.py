from motor_driver import MotorDriver
from logger import setup_logger
try:
    import RPi.GPIO as GPIO
    log = setup_logger(__name__, True)
    log.info("Live operation: imported RPi.GPIO")
except ModuleNotFoundError:
    import rpi_mock as GPIO
    log = setup_logger(__name__, False)
    log.info("Testrun: imported RPi_Mock")

import keyboard
import time

if __name__ == "__main__":
    motor_driver = MotorDriver(left_motor_pins=(15,16), right_motor_pins=(18,22))

    try:
        while True:
            if keyboard.is_pressed('w') or keyboard.is_pressed('up'):
                motor_driver.forward()
            elif keyboard.is_pressed('s') or keyboard.is_pressed('down'):
                motor_driver.backward()
            elif keyboard.is_pressed('a') or keyboard.is_pressed('left'):
                motor_driver.rotate_left()
            elif keyboard.is_pressed('d') or keyboard.is_pressed('right'):
                motor_driver.rotate_right()
            else:
                motor_driver.stop()

            if keyboard.is_pressed('esc'):
                motor_driver.stop()
                break

            time.sleep(0.1)
    finally:
        motor_driver.cleanup()
