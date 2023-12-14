from machine import Pin, PWM
from time import sleep

pwm = PWM(Pin(21))

pwm.freq(50)

def servo_pulse(position):
    """
    Send a servo pulse on the specified gpio pin
    that causes the servo to turn to the specified position, and
    then waits 20 ms.

    The position must be in the range 0 .. 100.
    For this range, the pulse must be in the range 0.5 ms .. 2.5 ms

    Before this function is called,
    the gpio pin must be configured as output.
    """
    pulse_width = 1000 + 80*position
    pwm.duty_u16(pulse_width)
    print(pulse_width)
    sleep(0.2)

while True:
    for i in range(0, 100, 1):
        servo_pulse(i)
    for i in range(100, 0, -1):
        servo_pulse(i)
