from machine import Pin
import time

pin = Pin(20,Pin.OUT)
kort = 0.3
lang = 0.75

while True:
    pin.value(0)
    time.sleep(kort)
    pin.value(1)
    time.sleep(kort)
    pin.value(0)
    time.sleep(kort)
    pin.value(1)
    time.sleep(kort)
    pin.value(0)
    time.sleep(kort)
    pin.value(1)
    time.sleep(kort)
    pin.value(0)
    time.sleep(kort)
    pin.value(1)
    time.sleep(lang)