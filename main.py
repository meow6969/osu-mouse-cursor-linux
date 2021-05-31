import os
import time
from Xlib import display

d = display.Display()
root = d.screen().root

while True:
    window = os.popen('xdotool getactivewindow').read()

    osu = os.popen(f"xdotool getwindowname {window}").read()

    if str(osu).strip() == 'osu!':
        root.warp_pointer(4000, 1000)
        d.sync()
    time.sleep(2)
