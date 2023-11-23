from machine import Pin
import time

pin = Pin(20,Pin.OUT)

def pulse(kort,lang):
    pin.value(0)
    time.sleep(kort)
    pin.value(1)
    time.sleep(lang)

while True:
    for x in range(3):
        pulse(0.3, 0.75)
    pulse(1, 2)