import os
import re
import time
from Xlib import X, display

d = display.Display()
root = d.screen().root

while True:
    window = os.popen('xdotool getactivewindow').read()

    osu = os.popen(f"xdotool getwindowname {window}").read()

    for m in re.finditer("osu!", osu, re.IGNORECASE):
        root.warp_pointer(4000, 1000)
        d.sync()
    time.sleep(2)
