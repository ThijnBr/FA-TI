import time

import machine
import neopixel

np = neopixel.NeoPixel(machine.Pin(13), 8)

while True:
    lst = [0,0,0]
    value = 255
    for x in range(3):
        lst2 = lst.copy()
        lst2[x] = value
        for x in range(8):
            np[x] = lst2
            np.write()
            time.sleep(0.1)
