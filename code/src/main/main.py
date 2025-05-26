import curses
from motor_driver import MotorDriver
from keyboard_control import run_keyboard_control
from logger import setup_logger
import time
# from keyboard_control import keyboard_loop

log = setup_logger(__name__, False)

LEFT_MOTOR_PINS = (22, 23)
RIGHT_MOTOR_PINS = (24, 25)

def main(stdscr):
    driver = MotorDriver(LEFT_MOTOR_PINS, RIGHT_MOTOR_PINS)
    run_keyboard_control(stdscr, driver)

if __name__ == "__main__":
    curses.wrapper(main)
