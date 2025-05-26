from logger import setup_logger
# try:
import RPi.GPIO as GPIO
log = setup_logger(__name__, True)
log.info("Live operation: imported RPi.GPIO")
# except ModuleNotFoundError:
#     import rpi_mock as GPIO
#     log = setup_logger(__name__, False)
#     log.info("Testrun: imported RPi_Mock")


class Motor:
    def __init__(self, pin_forward, pin_backward):
        self.log = log.getChild("Motor")
        self.pin_forward = pin_forward
        self.pin_backward = pin_backward
        self.setup()

    def setup(self):
        try:
            GPIO.setup(self.pin_forward, GPIO.OUT)
            GPIO.setup(self.pin_backward, GPIO.OUT)
            self.log.debug(f"Setup complete for pins {self.pin_forward}/{self.pin_backward}")
        except Exception as e:
            self.log.error(f"GPIO setup failed: {e}")

    def forward(self):
        self.log.debug("Motor forward")
        GPIO.output(self.pin_forward, GPIO.HIGH)
        GPIO.output(self.pin_backward, GPIO.LOW)

    def backward(self):
        self.log.debug("Motor backward")
        GPIO.output(self.pin_forward, GPIO.LOW)
        GPIO.output(self.pin_backward, GPIO.HIGH)

    def stop(self):
        self.log.debug("Motor stop")
        GPIO.output(self.pin_forward, GPIO.LOW)
        GPIO.output(self.pin_backward, GPIO.LOW)