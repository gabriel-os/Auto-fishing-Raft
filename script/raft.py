import pyautogui as pg
import time

while True:
    pescou = pg.locateOnScreen("lmb.png", confidence=0.9)
    if pescou != None:
        pg.click()
        time.sleep(1)
        pg.click()
        continue
    else:
        continue