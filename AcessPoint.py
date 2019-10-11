from machine import Pin
from time import sleep
import random
import network
import esp
import gc
try:
  import usocket as socket
except:
  import socket

led = Pin(2, Pin.OUT)
for i in range (1,10**100):
    r=random.randint(0,1)
    sleep(0.1);led.value(r)

esp.osdebug(None)
gc.collect()

ssid = 'MicroPython-AP'
password = '123456789'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

while ap.active() == False:
  pass

def web_page():
  html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
  <body><h1>Hello, Hackers!</h1></body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  print('Content = %s' % str(request))
  response = web_page()
  conn.send(response)
  conn.close()
