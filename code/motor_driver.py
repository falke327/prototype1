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
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.leftMotor = Motor(*left_motor_pins)
        self.rightMotor = Motor(*right_motor_pins)

    def forward(self):
        log.info("Drive forward.")
        self.leftMotor.forward()
        self.rightMotor.forward()

    def backward(self):
        log.info("Drive backward.")
        self.leftMotor.backward()
        self.rightMotor.backward()

    def rotate_left(self):
        log.info("Rotate left.")
        self.leftMotor.backward()
        self.rightMotor.forward()

    def rotate_right(self):
        log.info("Rotate right.")
        self.leftMotor.forward()
        self.rightMotor.backward()

    def stop(self):
        log.info("Stop.")
        self.leftMotor.stop()
        self.rightMotor.stop()

    def cleanup(self):
        self.stop()
        GPIO.cleanup()