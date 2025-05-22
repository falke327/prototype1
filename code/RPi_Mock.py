# RPi_Mock.py

# Dieses Modul emuliert die RPi.GPIO-Schnittstelle für Nicht-Raspberry-Umgebungen

BCM = 'BCM'
BOARD = 'BOARD'
OUT = 'OUT'
IN = 'IN'
HIGH = 1
LOW = 0

def setmode(mode):
    print(f"[MOCK] GPIO setmode({mode})")

def setwarnings(flag):
    print(f"[MOCK] GPIO setwarnings({flag})")

def setup(pin, mode):
    print(f"[MOCK] GPIO setup(pin={pin}, mode={mode})")

def output(pin, state):
    print(f"[MOCK] GPIO output(pin={pin}, state={state})")

def cleanup():
    print(f"[MOCK] GPIO cleanup()")

