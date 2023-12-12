import pyautogui
import time
import random

while True:
    x = random.randit(900, 1500)
    y = random.randint(400, 800)
    pyautogui.moveTo(x, y, 0.2)
    time.sleep(1)
