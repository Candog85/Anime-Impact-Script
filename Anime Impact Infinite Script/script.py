import pyautogui as py
import time
import cv2
import autoit
import math
py.FAILSAFE=True


counter=0

def locate():
    while True:

        global counter
        counter=counter+1

        try:

            print(py.locateOnScreen('wave20.png', confidence=0.95))

        except py.ImageNotFoundException:

            print(counter)

        else:
           
           autoit.mouse_click("left", 299, 157)
           print("Run took " + str(math.floor(counter/60)) + ":" + str((counter%60)*20))
           counter=0
        
        try:
            print(py.locateOnScreen('replay.png', confidence=0.95))
        
        except py.ImageNotFoundException:

            pass
        
        else:

            autoit.mouse_click("left", 909, 792)
            
        time.sleep(1)

locate()
    