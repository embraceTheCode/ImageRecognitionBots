#06/04/2021 
#Carlos Astengo Macias

#Designed for AimBooster on full screen in a 1920*1080 resolution
#AimBooster: http://www.aimbooster.com/

import pyautogui
import time
import keyboard
import win32api, win32con

time.sleep(0.6)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:
    #Takes a screenshot of the screen with the given size 
    pic = pyautogui.screenshot(region=(650,360,625,450))
    width, height = pic.size

    #Goes every 8 pixels searching for the center target by checking the pixels color
    #In the case where the program detects the center target it calls the click function
    for x in range (0,width,8):
        for y in range (0,height,8):
            r,g,b = pic.getpixel((x,y))

            if b == 195:
                click(x+650, y+360)
                time.sleep(0.1)
                break