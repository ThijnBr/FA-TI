from machine import Pin
import time

gpio_pin = Pin(20, Pin.OUT)


def pulse(pin, high_time, low_time):
    """
    Geef een puls op de pin:
    Maak de pin pin hoog, wacht high_time,
    maak de pin laag, en wacht nog low_time
    """
    pin.value(1)
    time.sleep(high_time)
    pin.value(0)
    time.sleep(low_time)
    # Kopier hier je implementatie van pulse

def morse(pin, dot_length, text):
    """
    Laat de text horen als morse code.
    De pin is de pin die gebruikt wordt.
    De text mag de volgende characters bevatten: spatie, streepje, punt.
    De dot_length is de lengte van een punt (dot).
    De lengte van de andere characters wordt daar van afgeleid.
    """

    # implementeer deze functie
    for x in text:
        if x == '.':
            pin.value(1)
            time.sleep(dot_length)
            pin.value(0)
        elif x == '-':
            pin.value(1)
            time.sleep(dot_length*3)
            pin.value(0)
        else:
            time.sleep(1)
        


morse(gpio_pin, 0.2, ".--. -.-- - .... --- -.")
