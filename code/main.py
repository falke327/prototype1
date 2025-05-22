from Motor import Motor
from MotorDriver import MotorDriver
try:
    import RPi.GPIO as GPIO
    print("[INFO] <main> Echtbetrieb: RPi.GPIO wurde importiert.")
except ModuleNotFoundError:
    import RPi_Mock as GPIO
    print("[INFO] <main> Testbetrieb: RPi_Mock wurde importiert.")

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

# TODO: implement keyboard control
# TODO: implement logger that prints in Mock mode to the console and into a file /var/log/falk in RPi mode
# TODO: every input should be formatted with: Timestamp - LogLevel - Classname - Message