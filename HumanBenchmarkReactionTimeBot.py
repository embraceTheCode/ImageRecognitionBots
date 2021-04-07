#06/04/2021 
#Carlos Astengo Macias

#Designed for the Reaction Time Test of the Human Benchmark on full screen in a 1920*1080 resolution
#Human Benchmark Reaction Time Test: https://humanbenchmark.com/tests/reactiontime

import pyautogui
import time
import keyboard
import win32api, win32con

time.sleep(0.3)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

#Checks the specified pixel to see if it turns green
#In the case where the program detects a green pixel it calls the click function
while keyboard.is_pressed('q') == False:
    pic = pyautogui.pixel(810,340)[0]

    if pic != 206:
        click(810, 340)
        time.sleep(0.1)