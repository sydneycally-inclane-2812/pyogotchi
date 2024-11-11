from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)
print('Blinking LED Example')

while True:
  led.value(not led.value())
  sleep(0.5)