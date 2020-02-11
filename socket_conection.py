
import socket
import network
from time import sleep

sta = network.WLAN(network.STA_IF)
sta.connect("xxxx", "xxxxxx")
sleep(5)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
HOST='192.168.1.35'
PORT=3333
s.bind((HOST,PORT))
