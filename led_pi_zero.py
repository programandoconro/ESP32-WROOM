## Raspberrypi zero GPIO LED blink

import gpiozero as io
from time import sleep
import random 

led=io.LED(17)

for i in range(1,1000000):
      r=random.randint(0,9)*0.1
      led.on()
      sleep(0.1*r)
      led.off()
      sleep(0.2*r)
      led.off()
      sleep(0.3*r)
      led.on()
      
