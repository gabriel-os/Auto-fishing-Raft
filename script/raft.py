import pyautogui as pg
import time
import os

# get actual path
script_path = path_script = os.path.abspath(__file__)

#move to img folder 'n get
os.chdir('img')

img_path = os.getcwd()

while True:
    #region caught in variable pescou without region
    pescou = pg.locateOnScreen(os.path.join(img_path,  'lmb.png') , confidence=0.8299, region=(1250, 441, 59, 41))

    print(type(pescou))

    if pescou != None:
        pg.click()
        time.sleep(1)
        pg.click()
        time.sleep(0.125)
        continue
    else:
        continue