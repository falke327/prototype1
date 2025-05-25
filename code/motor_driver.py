from motor import Motor

try:
    import RPi.GPIO as GPIO
    print("[INFO] <MotorDriver> Live operation: imported RPi.GPIO")
except ModuleNotFoundError:
    import rpi_mock as GPIO
    print("[INFO] <MotorDriver> Testrun: imported RPi_Mock")

class MotorDriver:
    def __init__(self, left_motor_pins, right_motor_pins):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.leftMotor = Motor(*left_motor_pins)
        self.rightMotor = Motor(*right_motor_pins)

    def forward(self):
        print("[INFO] <MotorDriver> Drive forward.")
        self.leftMotor.forward()
        self.rightMotor.forward()

    def backward(self):
        print("[INFO] <MotorDriver> Drive backward.")
        self.leftMotor.backward()
        self.rightMotor.backward()

    def rotate_left(self):
        print("[INFO] <MotorDriver> Rotate left.")
        self.leftMotor.backward()
        self.rightMotor.forward()

    def rotate_right(self):
        print("[INFO] <MotorDriver> Rotate right.")
        self.leftMotor.forward()
        self.rightMotor.backward()

    def stop(self):
        print("[INFO] <MotorDriver> Stop.")
        self.leftMotor.stop()
        self.rightMotor.stop()

    def cleanup(self):
        self.stop()
        GPIO.cleanup()