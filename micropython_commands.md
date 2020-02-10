## Keyboard commands
- Ctrl-C cancels any input, or interrupts the currently running code.
- Ctrl-D on a blank line will do a soft reset.
- Ctrl-E special paste mode.
- Ctrl-X to exit.

## Show installed modules
```help('modules')```

## import modules
```
import webrepl
import webrepl_setup
```
## Show function within module

```dir(webrepl_setup)```

## Create, write and read files

f = open('myfile.txt', 'w')
f.write('Hola MicroPython')
f = open('myfile.txt')
f.close()

# List and make directories and files

import os
os.mkdir('ro')
os.listdir()

# Show ip

import network
ap_if = network.WLAN(network.AP_IF)
ap_if.active(True)
ap_if.ifconfig()
