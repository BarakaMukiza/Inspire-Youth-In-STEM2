#print("Hello, Pi Pico!")
from machine import Pin
import time

# Define the GPIO pins used for the LEDs and switches
led1 = Pin(10, Pin.OUT)
led2 = Pin(11, Pin.OUT)

switch1 = Pin(12, Pin.IN, Pin.PULL_UP)
switch2 = Pin(13, Pin.IN, Pin.PULL_UP)

# Define a function to toggle the state of an LED
def toggle_led(led_pin):
    led_pin.value(not led_pin.value())

# Create a loop that will continuously check the state of the switches and turn on or off the LEDs accordingly
while True:
    if switch1.value() == 0:
        toggle_led(led1)
        time.sleep(0.2) # debounce the switch

    if switch2.value() == 0:
        toggle_led(led2)
        time.sleep(0.2) # debounce the switch