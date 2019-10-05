# Random lighting for home made desk lamp with wroom-esp32

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
    for i in range (1,10**100):
        r=random.randint(0,1)
        sleep(0.1);led.value(r)
 
 
# We have a cool lamp
