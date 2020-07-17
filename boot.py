# This file is executed on every boot (including wake-boot from deepsleep)
import gc
import sys
from os import listdir
from os.path import isfile

import esp
import machine
import network
import uos
import webrepl

# Check for updated files in the main directory and auto-move them to their correct folders, then restart
files_structure = {
    'bike.py': 'glowingbike/bike.py',
    'driving_animation.py': 'glowingbike/functions/driving_animation.py',
    'fadeout_animation.py': 'glowingbike/functions/fadeout_animation.py',
    'turn_animation.py': 'glowingbike/functions/turn_animation.py'
}
files = [f for f in listdir() if isfile(f)]
for filename in files:
    if filename != 'boot.py' and filename != 'main.py' and filename in files_structure:
        os.rename(filename, files_structure[filename])
        machine.reset()


esp.osdebug(None)
# uos.dupterm(None, 1) # disable REPL on UART(0)


ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='🚲The Glowing Bike Project',
          authmode=network.AUTH_WPA_WPA2_PSK,
          # change the default password here if you want to secure your bike wifi even more
          password='glowingbike')

webrepl.start()
gc.collect()
