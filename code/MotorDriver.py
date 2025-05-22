import Motor


class MotorDriver:
    def __init__(self, left_motor: Motor, right_motor: Motor):
        self.left = left_motor
        self.right = right_motor

    def forward(self):
        self.left.forward()
        self.right.forward()

    def backward(self):
        self.left.backward()
        self.right.backward()

    def rotate_left(self):
        self.left.backward()
        self.right.forward()

    def rotate_right(self):
        self.left.forward()
        self.right.backward()

    def stop(self):
        self.left.stop()
        self.right.stop()