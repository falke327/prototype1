import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main')))

import unittest
from unittest.mock import patch
from src.main.motor import Motor

class TestMotor(unittest.TestCase):
    @patch("src.main.motor.GPIO")
    def test_forward_calls_gpio_correctly(self, mock_gpio):
        motor = Motor(15, 16)
        motor.forward()
        mock_gpio.output.assert_any_call(15, mock_gpio.HIGH)
        mock_gpio.output.assert_any_call(16, mock_gpio.LOW)

    @patch("src.main.motor.GPIO")
    def test_backward_calls_gpio_correctly(self, mock_gpio):
        motor = Motor(15, 16)
        motor.backward()
        mock_gpio.output.assert_any_call(15, mock_gpio.LOW)
        mock_gpio.output.assert_any_call(16, mock_gpio.HIGH)

    @patch("src.main.motor.GPIO")
    def test_stop_calls_gpio_correctly(self, mock_gpio):
        motor = Motor(15, 16)
        motor.stop()
        mock_gpio.output.assert_any_call(15, mock_gpio.LOW)
        mock_gpio.output.assert_any_call(16, mock_gpio.LOW)

if __name__ == "__main__":
    unittest.main()