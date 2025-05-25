import unittest
from unittest.mock import patch, MagicMock

from src.main.motor_driver import MotorDriver

class TestMotorDriver(unittest.TestCase):
    @patch("src.main.motor_driver.Motor")
    @patch("src.main.motor_driver.GPIO")
    def setUp(self, mock_gpio, mock_motor):
        self.mock_gpio = mock_gpio
        self.mock_motor = mock_motor

        # simulate motors
        self.left_motor_mock = MagicMock()
        self.right_motor_mock = MagicMock()
        self.mock_motor.side_effect = [self.left_motor_mock, self.right_motor_mock]

        self.driver = MotorDriver(left_motor_pins=(1, 2), right_motor_pins=(3, 4))

    def test_forward_calls_motor_forward(self):
        self.driver.forward()
        self.left_motor_mock.forward.assert_called_once()
        self.right_motor_mock.forward.assert_called_once()

    def test_backward_calls_motor_backward(self):
        self.driver.backward()
        self.left_motor_mock.backward.assert_called_once()
        self.right_motor_mock.backward.assert_called_once()

    def test_rotate_left(self):
        self.driver.rotate_left()
        self.left_motor_mock.backward.assert_called_once()
        self.right_motor_mock.forward.assert_called_once()

    def test_rotate_right(self):
        self.driver.rotate_right()
        self.left_motor_mock.forward.assert_called_once()
        self.right_motor_mock.backward.assert_called_once()

    def test_stop(self):
        self.driver.stop()
        self.left_motor_mock.stop.assert_called_once()
        self.right_motor_mock.stop.assert_called_once()

# This test does not work with my rpi_mock.py for local development gefore deployment to the Raspberry
    # def test_cleanup(self):
    #     self.driver.cleanup()
    #     print(f"Called methods on mock_gpio: {self.mock_gpio.mock_calls}")
    #     self.mock_gpio.cleanup.assert_called_once()

if __name__ == '__main__':
    unittest.main()
