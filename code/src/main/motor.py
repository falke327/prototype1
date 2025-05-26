import lgpio
from logger import setup_logger

log = setup_logger(__name__, True)
log.info("Live operation: imported lgpio")

class Motor:
    def __init__(self, pin_forward, pin_backward):
        self.log = log.getChild("Motor")
        self.pin_forward = pin_forward
        self.pin_backward = pin_backward
        self.handle = None
        self.setup()

    def setup(self):
        try:
            self.handle = lgpio.gpiochip_open(0)
            lgpio.gpio_claim_output(self.handle, self.pin_forward, 0)
            lgpio.gpio_claim_output(self.handle, self.pin_backward, 0)
            self.log.debug(f"Setup complete for pins {self.pin_forward}/{self.pin_backward}")
        except Exception as e:
            self.log.error(f"GPIO setup failed: {e}")

    def forward(self):
        self.log.debug("Motor forward")
        lgpio.gpio_write(self.handle, self.pin_forward, 1)
        lgpio.gpio_write(self.handle, self.pin_backward, 0)

    def backward(self):
        self.log.debug("Motor backward")
        lgpio.gpio_write(self.handle, self.pin_forward, 0)
        lgpio.gpio_write(self.handle, self.pin_backward, 1)

    def stop(self):
        self.log.debug("Motor stop")
        lgpio.gpio_write(self.handle, self.pin_forward, 0)
        lgpio.gpio_write(self.handle, self.pin_backward, 0)

    def cleanup(self):
        if self.handle is not None:
            lgpio.gpiochip_close(self.handle)
            self.log.info("lgpio handle closed")
