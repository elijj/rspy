import pyautogui
import random
import time
dimensions = pyautogui.size()
i = 0
while True:
    i = i + 1
    pyautogui.click(1117 + random.randint(1,51) ,873 + random.randint(1,51) ) 
    if i % 2 == 0:
        pyautogui.click(1330,784)
    time.sleep(10)


