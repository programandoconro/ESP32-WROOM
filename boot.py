from index import html
import network
from machine import Pin
from time import sleep
import random

ap= network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='ScaryBug')

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect("xxxx", "xxxxxx")
sleep(5)

import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)

if sta.isconnected()==True:
    led = Pin(2, Pin.OUT)
    for i in range (1,10**100):
        r=random.randint(0,1)
        s.listen(1)
        cl, addr = s.accept()
        cl.send(html)
        sleep(0.1);led.value(r)
        cl.close()
