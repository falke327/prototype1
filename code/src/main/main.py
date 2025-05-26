from motor_driver import MotorDriver
from logger import setup_logger
import time
# from keyboard_control import keyboard_loop

log = setup_logger(__name__, False)

if __name__ == "__main__":
    motor_driver = MotorDriver(left_motor_pins=(22,23), right_motor_pins=(24,25))

    try:
        # keyboard_loop(motor_driver, log)
        print("Vorwärts")
        motor_driver.forward()
        time.sleep(5)
        print("Rückwärts")
        motor_driver.backward()
        time.sleep(5)
        print("drehe links")
        motor_driver.rotate_left()
        time.sleep(5)
        print("drehe rechts")
        motor_driver.rotate_right()
        time.sleep(5)
        motor_driver.stop()
    finally:
        motor_driver.cleanup()
        log.info("Cleaned up GPIO and exited.")
