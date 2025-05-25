# rpi_mock.py
from logger import setup_logger

log = setup_logger(__name__, False)

# This Module emulates the RPi.GPIO-Interface for non-Raspberry-systems

BCM = 'BCM'
BOARD = 'BOARD'
OUT = 'OUT'
IN = 'IN'
HIGH = 1
LOW = 0

def setmode(mode):
    log.debug(f"[MOCK] GPIO setmode({mode})")

def setwarnings(flag):
    log.debug(f"[MOCK] GPIO setwarnings({flag})")

def setup(pin, mode):
    log.debug(f"[MOCK] GPIO setup(pin={pin}, mode={mode})")

def output(pin, state):
    log.debug(f"[MOCK] GPIO output(pin={pin}, state={state})")

def cleanup():
    log.debug(f"[MOCK] GPIO cleanup()")

