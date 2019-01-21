import pyautogui
import random
import time
print(pyautogui.size() )
while True:
    x = random.randint( (pyautogui.size()[0] / 2 ) , (pyautogui.size()[0] / 2 ) + 50 )
    y = random.randint( (pyautogui.size()[1] / 2 ) , (pyautogui.size()[1] / 2 ) + 50 ) 
    pyautogui.click(  x , y )
    pyautogui.doubleClick(  x , y )
    print('clicked:' + str(x) + ',' + str(y) )
    time.sleep(random.randint(10,25))


