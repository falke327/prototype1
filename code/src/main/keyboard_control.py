import keyboard
import time

def keyboard_loop(motor_driver, log):
    direction = None

    while True:
        if keyboard.is_pressed('w') or keyboard.is_pressed('up'):
            if direction != 'forward':
                log.debug("Command: forward")
                motor_driver.forward()
                direction = 'forward'

        elif keyboard.is_pressed('s') or keyboard.is_pressed('down'):
            if direction != 'backward':
                log.debug("Command: backward")
                motor_driver.backward()
                direction = 'backward'

        elif keyboard.is_pressed('a') or keyboard.is_pressed('left'):
            if direction != 'left':
                log.debug("Command: rotate_left")
                motor_driver.rotate_left()
                direction = 'left'

        elif keyboard.is_pressed('d') or keyboard.is_pressed('right'):
            if direction != 'right':
                log.debug("Command: rotate_right")
                motor_driver.rotate_right()
                direction = 'right'

        else:
            if direction is not None:
                log.debug("Command: stop")
                motor_driver.stop()
                direction = None

        if keyboard.is_pressed('esc'):
            log.info("Escape pressed. Exiting control loop.")
            break

        time.sleep(0.05)
