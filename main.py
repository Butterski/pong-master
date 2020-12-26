from pyautogui import *
import pyautogui
import time
import keyboard
import win32gui
import math
import win32api, win32con

dc = win32gui.GetDC(0)
red = win32api.RGB(255, 0, 0)
blue = win32api.RGB(0, 0, 255)

def moveMouse(x, y):
    win32api.SetCursorPos((x, y))
"""
pic = pyautogui.screenshot(region=(1470, 175, 825, 745))ąąąą
pic.save(r"savedimage.png")
"""

while keyboard.is_pressed('q') == False:
    pic = pyautogui.screenshot(region=(1430, 175, 750, 815))
    width, height = pic.size

    for x in range(0, width, 20):
        for y in range(0, height, 15):

            r, g, b = pic.getpixel((x, y))
            boxA = 100
            mouseX, mouseY = pyautogui.position()

            if b == 85:
                for i in range(boxA):
                    win32gui.SetPixel(dc, x + i + 1380, y + 125, red)
                    win32gui.SetPixel(dc, x + 1380, y + i + 125, red)
                    win32gui.SetPixel(dc, x + boxA + 1380, y + i + 125, red)
                    win32gui.SetPixel(dc, x + i + 1380, y + boxA + 125, red)


                d = mouseY - y
                for j in range(d):
                    win32gui.SetPixel(dc, mouseX + j, mouseY, blue)
                moveMouse(1430, y + 175)
                break

#file:///G:/Projekty/pong-master/DHTMLPong.html