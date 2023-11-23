from machine import Pin
import time

led_pin = Pin(20, Pin.OUT)
switch_pin = Pin(19, Pin.IN, pull=Pin.PULL_DOWN)
switch_pin2 = Pin(18, Pin.IN, pull=Pin.PULL_DOWN)

switched = False
while True:
    if switch_pin.value():
        led_pin.value(1)
    if switch_pin2.value():
        led_pin.value(0)
