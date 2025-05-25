from motor import Motor
from logger import setup_logger
try:
    import RPi.GPIO as GPIO
    log = setup_logger(__name__, True)
    log.info("Live operation: imported RPi.GPIO")
except ModuleNotFoundError:
    import rpi_mock as GPIO
    log = setup_logger(__name__, False)
    log.info("Testrun: imported RPi_Mock")

class MotorDriver:
    def __init__(self, left_motor_pins, right_motor_pins):
        self.log = log.getChild("MotorDriver")
        self.log.info("Initializing MotorDriver")
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

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
        self.log.debug("Drive forward.")
        self.leftMotor.forward()
        self.rightMotor.forward()

    def backward(self):
        self.log.debug("Drive backward.")
        self.leftMotor.backward()
        self.rightMotor.backward()

    def rotate_left(self):
        self.log.debug("Rotate left.")
        self.leftMotor.backward()
        self.rightMotor.forward()

    def rotate_right(self):
        self.log.debug("Rotate right.")
        self.leftMotor.forward()
        self.rightMotor.backward()

    def stop(self):
        self.log.debug("Stop.")
        self.leftMotor.stop()
        self.rightMotor.stop()

    def cleanup(self):
        self.log.info("Cleanup GPIO")
        self.stop()
        GPIO.cleanup()