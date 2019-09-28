import network
from machine import Pin
from time import sleep
import random

ap= network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='ScaryBug')

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect("AndroidAP", "xjnn4112")
sleep(3)

if sta.isconnected()==True:
    led = Pin(2, Pin.OUT)
    for i in range (1,10**100):
        r=random.randint(0,1)
        sleep(0.1);led.value(r)

    
    
    
    
    
    
    
      
      

      
