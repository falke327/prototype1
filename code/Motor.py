try:
    import RPi.GPIO as GPIO
    print("[INFO] <Motor> Echtbetrieb: RPi.GPIO wurde importiert.")
except ModuleNotFoundError:
    import RPi_Mock as GPIO
    print("[INFO] <Motor> Testbetrieb: RPi_Mock wurde importiert.")


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
