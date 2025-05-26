import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# Projektpfad einbinden
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main')))

from src.main.motor import Motor

class TestMotor(unittest.TestCase):

    @patch("motor.lgpio")
    def test_forward_calls_lgpio_correctly(self, mock_lgpio):
        mock_lgpio.gpiochip_open.return_value = 1  # Mock-Handle
        motor = Motor(15, 16)
        motor.forward()
        mock_lgpio.gpio_write.assert_any_call(1, 15, 1)
        mock_lgpio.gpio_write.assert_any_call(1, 16, 0)

    @patch("motor.lgpio")
    def test_backward_calls_lgpio_correctly(self, mock_lgpio):
        mock_lgpio.gpiochip_open.return_value = 1
        motor = Motor(15, 16)
        motor.backward()
        mock_lgpio.gpio_write.assert_any_call(1, 15, 0)
        mock_lgpio.gpio_write.assert_any_call(1, 16, 1)

    @patch("motor.lgpio")
    def test_stop_calls_lgpio_correctly(self, mock_lgpio):
        mock_lgpio.gpiochip_open.return_value = 1
        motor = Motor(15, 16)
        motor.stop()
        mock_lgpio.gpio_write.assert_any_call(1, 15, 0)
        mock_lgpio.gpio_write.assert_any_call(1, 16, 0)

    @patch("motor.lgpio")
    def test_cleanup_closes_chip(self, mock_lgpio):
        mock_lgpio.gpiochip_open.return_value = 42
        motor = Motor(23, 24)
        motor.cleanup()
        mock_lgpio.gpiochip_close.assert_called_once_with(42)


if __name__ == "__main__":
    unittest.main()