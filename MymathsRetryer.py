from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con
import random

#mark button (1654,987)

#q1 (460,630)

#reload (124,46)

#retry (891,650)

time.sleep(10)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

counter=0

while 1:
    if keyboard.is_pressed("space"):
        click(460,630)
        time.sleep(0.1)
        pyautogui.keyDown("1")
        time.sleep(0.1)
        pyautogui.keyUp
        time.sleep(0.1)
        click(1654,987)
        time.sleep(0.1)
        click(259,488)
        time.sleep(0.1)
        click(1654,987)
        time.sleep(0.1)
        click(1262,562)
        time.sleep(0.1)
        click(124,46)
        time.sleep(0.5)
        click(891,650)
        time.sleep(0.1)
        counter= counter +1
        print (counter)
        




