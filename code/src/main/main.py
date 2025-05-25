from motor_driver import MotorDriver
from logger import setup_logger
from keyboard_control import keyboard_loop

try:
    import RPi.GPIO as GPIO
    log = setup_logger(__name__, True)
    log.info("Live operation: imported RPi.GPIO")
except ModuleNotFoundError:
    import rpi_mock as GPIO
    log = setup_logger(__name__, False)
    log.info("Testrun: imported RPi_Mock")

if __name__ == "__main__":
    motor_driver = MotorDriver(left_motor_pins=(15,16), right_motor_pins=(18,22))

    try:
        keyboard_loop(motor_driver, log)
    finally:
        motor_driver.cleanup()
        log.info("Cleaned up GPIO and exited.")
