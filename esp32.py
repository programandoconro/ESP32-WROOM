######## We are in MicroPython ################

import network

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect("YourNetworkName", "YourNetworkPassword")
station.isconnected()
station.ifconfig()

ap= network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='ScaryBug')

##### random blinking #######

from machine import Pin
from time import sleep
import random

led = Pin(2, Pin.OUT)
for i in range (1,10**100):
      r=random.randint(0,1)
      sleep(0.1);led.value(r)
      
