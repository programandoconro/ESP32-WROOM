# Random lighting for home made desk lamp and server intruder alarm with MicroPython on a wroom-esp32 WIFI chip

# Install pip3 

    sudo apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev \
    libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev \
    libexpat1-dev liblzma-dev zlib1g-dev libffi-dev

     wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz

    sudo tar zxf Python-3.7.0.tgz
    cd Python-3.7.0
    sudo ./configure
    sudo make -j 4
    sudo make altinstall


    sudo apt install python3-pip
    
# Install tool for communication with ESP32

    sudo pip3 install esptool
    
 # Look for the ubication of ESP32 connected in USB and install microPython on device

    dmesg | grep ttyUSB

    esptool.py --port /dev/ttyUSB0 erase_flash

    wget https://micropython.org/resources/firmware/esp32-20190907-v1.11-291-gc69f58e6b.bin

    esptool.py --port /dev/ttyUSB0 write_flash 0x1000 <path to firmware file>

    sudo pip3 install rshell

    rshell --buffer-size=30 -p /dev/ttyUSB0 
    repl
    
 # We are in, lets code some Python to make random lighting
 
    from machine import Pin
    from time import sleep
    import random

    led = Pin(2, Pin.OUT)

    while True :
        r=random.randint(0,1)
        sleep(0.07);led.value(r)
 
 
# We have a cool lamp with random lighting, we can chang de sleep time for different effects.

Use Crl-x Crl-z to exit, you can close the shell and shoud keep running code on device.

# We can also create a boot.py with the code above and put it on the device for automatic executing on boot when connected to power.

Install ampy and add python code on device

   
    ampy --port /dev/ttyUSB0 put boot.py
    
 
 # Now, we just have to supply power and our cool lamp will work. Hope you enjoy lights when programming. 
 

    ampy --port /dev/ttyUSB0 run boot.py


# Optional idea: make the lamp into an alarm for when someone connects to our server.

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
    sleep(5)

    html = """<!DOCTYPE html>
    <html>
    <head> <title> Hello Hackers !!
    </title> </head>
    <body> <h1>Welcome to my site, please hack it and share me how. </h1> </body>
    </html>
    """

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
