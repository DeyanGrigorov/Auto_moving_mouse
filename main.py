import time

import pyautogui

print('Press ctrl+c if in console or simply stop the script to quit')

try:
    pyautogui.FAILSAFE = False
    while True:
        pyautogui.moveTo(960, 540, 2)
        time.sleep(10)
        pyautogui.moveTo(1060, 640, 2)
        pyautogui.click(button='right')
except KeyboardInterrupt:
    print('\n')
