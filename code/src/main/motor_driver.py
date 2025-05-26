from motor import Motor
from logger import setup_logger
# try:
import RPi.GPIO as GPIO
log = setup_logger(__name__, True)
log.info("Live operation: imported RPi.GPIO")
log.info("Initializing MotorDriver")
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


# except ModuleNotFoundError:
#     import rpi_mock as GPIO
#     log = setup_logger(__name__, False)
#     log.info("Testrun: imported RPi_Mock")

class MotorDriver:
    def __init__(self, left_motor_pins, right_motor_pins):
        self.log = log.getChild("MotorDriver")

        self.log.debug(f"Left Motor Pins: {left_motor_pins}")
        self.log.debug(f"Right Motor Pins: {right_motor_pins}")

        try:
            self.left_motor = Motor(*left_motor_pins)
            self.right_motor = Motor(*right_motor_pins)
            self.log.info("Motors initialized successfully.")
        except Exception as e:
            self.log.error(f"Motor initialization failed: {e}")
            raise

    def forward(self):
        self.log.info("Drive forward.")
        self.left_motor.forward()
        self.right_motor.forward()

    def backward(self):
        self.log.info("Drive backward.")
        self.left_motor.backward()
        self.right_motor.backward()

    def rotate_left(self):
        self.log.info("Rotate left.")
        self.left_motor.backward()
        self.right_motor.forward()

    def rotate_right(self):
        self.log.info("Rotate right.")
        self.left_motor.forward()
        self.right_motor.backward()

    def stop(self):
        self.log.info("Stop.")
        self.left_motor.stop()
        self.right_motor.stop()

    def cleanup(self):
        self.log.info("Cleanup GPIO")
        self.stop()
        GPIO.cleanup()