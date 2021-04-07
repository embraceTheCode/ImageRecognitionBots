#06/04/2021 
#Carlos Astengo Macias

#Designed for Magic Paino Tiles on full screen in a 1920*1080 resolution
#Magic Piano Tiles: https://kizi.com/games/magic-piano-tiles

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

#Checks the 4 pixels to see if any of them is black
#In the case the program detects a black pixel it calls the click function
while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(803,829)[0] == 0:
        click(803,829)
    if pyautogui.pixel(920,829)[0] == 0:
        click(920,829)
    if pyautogui.pixel(1006,829)[0] == 0:
        click(1006,829)
    if pyautogui.pixel(1094,829)[0] == 0:
        click(1094,829)