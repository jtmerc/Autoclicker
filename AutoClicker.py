# import modules
import time
import pyautogui

# Auto clicker
time.sleep(3)
# use print(pyautogui.position()) to find where to position mouse and where you want it to click
# Run it twice to find both

# range is for many times you want it to click
# change inputs
for i in range(10):
    pyautogui.moveTo(0, 0)
    time.sleep(2)
    pyautogui.doubleClick()
    time.sleep(2)
    pyautogui.moveTo(0, 0)
    time.sleep(1)
    pyautogui.leftClick()

# For instagram or tiktok or for app that has scrolling
# pyautogui.moveTo(550, 520)
# for i in range(5):
#    time.sleep(0.5)
#    pyautogui.doubleClick()
#    time.sleep(0.5)
#    pyautogui.scroll(-16)
