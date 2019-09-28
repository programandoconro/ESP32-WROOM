import network

ap= network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='ScaryBug')

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect("AndroidAP", "xjnn4112")
sta.isconnected()
sta.ifconfig()

#('192.168.43.175', '255.255.255.0', '192.168.43.1', '192.168.43.1')

##### random blinking #######


while True:
  sta.active(True)
  from machine import Pin
  from time import sleep
  import random

  led = Pin(2, Pin.OUT)
  for i in range (1,10**100):
      r=random.randint(0,1)
      sleep(0.1);led.value(r)
      
      
      
