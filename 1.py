import time, pyautogui
from datetime import datetime
from mss import mss
from PIL import Image
import os

#print(pyautogui.position())
#print(pix[pyautogui.position()][0])

while True:
    time.sleep(55) #55
    pyautogui.click(x=93,y=113)
    time.sleep(5)

    with mss() as sct: sct.shot(output = 'l.png')
    with Image.open('l.png') as im: pix = im.load()

    tnow = datetime.strftime(datetime.now(), "%H:%M")
    if pix[90,264][0] == 255:
        print('Working time', tnow)
        pyautogui.click(x=180,y=250)
        time.sleep(60*2)
    else: print("Nothing to do here", tnow)
