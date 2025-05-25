try:
    import RPi.GPIO as GPIO
    print("[INFO] <Motor> Live operation: imported RPi.GPIO")
except ModuleNotFoundError:
    import rpi_mock as GPIO
    print("[INFO] <Motor> Testrun: imported RPi_Mock")


class Motor:
    def __init__(self, pin_forward, pin_backward):
        self.pin_forward = pin_forward
        self.pin_backward = pin_backward
        self.setup()

    def setup(self):
        GPIO.setup(self.pin_forward, GPIO.OUT)
        GPIO.setup(self.pin_backward, GPIO.OUT)

    def forward(self):
        GPIO.output(self.pin_forward, GPIO.HIGH)
        GPIO.output(self.pin_backward, GPIO.LOW)

    def backward(self):
        GPIO.output(self.pin_forward, GPIO.LOW)
        GPIO.output(self.pin_backward, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.pin_forward, GPIO.LOW)
        GPIO.output(self.pin_backward, GPIO.LOW)
