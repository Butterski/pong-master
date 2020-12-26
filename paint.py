import win32gui
import win32api

dc = win32gui.GetDC(0)
red = win32api.RGB(255, 0, 0)
i = 1
boxA = 50

while True:
    for i in range(boxA):
        win32gui.SetPixel(dc, 100 + i, 100, red)
        win32gui.SetPixel(dc, 100, 100 + i, red)
        win32gui.SetPixel(dc, 100 + boxA, 100 + i, red)
        win32gui.SetPixel(dc, 100 + i, 100 + boxA, red)


