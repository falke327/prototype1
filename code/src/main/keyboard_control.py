import curses
from logger import setup_logger

log = setup_logger(__name__, True)

KEY_MAP = {
    ord('w'): 'forward',
    ord('s'): 'backward',
    ord('a'): 'rotate_left',
    ord('d'): 'rotate_right',
    curses.KEY_UP: 'forward',
    curses.KEY_DOWN: 'backward',
    curses.KEY_LEFT: 'rotate_left',
    curses.KEY_RIGHT: 'rotate_right',
    ord(' '): 'stop',
    27: 'exit',  # ESC
}


def run_keyboard_control(stdscr, driver):
    curses.cbreak()
    stdscr.nodelay(True)
    stdscr.keypad(True)

    stdscr.clear()
    stdscr.addstr("Controls:\n")
    stdscr.addstr("W / ↑ = Forward\nS / ↓ = Backward\nA / ← = Rotate Left\nD / → = Rotate Right\n")
    stdscr.addstr("Space = Stop\nESC = Quit\n")

    log.info("Started Keyboard control.")

    try:
        while True:
            key = stdscr.getch()
            action = KEY_MAP.get(key)

            if action:
                log.debug(f"Key pressed: {key} → Action: {action}")

            if action == 'forward':
                driver.forward()
            elif action == 'backward':
                driver.backward()
            elif action == 'rotate_left':
                driver.rotate_left()
            elif action == 'rotate_right':
                driver.rotate_right()
            elif action == 'stop':
                driver.stop()
            elif action == 'exit':
                log.info("ESC pressed – Control has ended.")
                break

            curses.napms(100)  # 100 ms Sleep

    finally:
        driver.cleanup()
        log.info("Driver cleanup completed.")
        stdscr.addstr("Ended.\n")
        stdscr.refresh()
        curses.napms(1000)