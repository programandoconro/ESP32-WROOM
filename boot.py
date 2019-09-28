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

import socket

def http_get(url):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()
    
    import machine
pins = [machine.Pin(i, machine.Pin.IN) for i in (0, 2, 4, 5, 12, 13, 14, 15)]

html = """<!DOCTYPE html>
<html>
    <head> <title>ESP8266 Pins</title> </head>
    <body> <h1>ESP8266 Pins</h1>
        <table border="1"> <tr><th>Pin</th><th>Value</th></tr> %s </table>
    </body>
</html>
"""


#servidor

import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break
    rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins]
    response = html % '\n'.join(rows)
    cl.send(response)
    cl.close()
    
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
      
      
      
