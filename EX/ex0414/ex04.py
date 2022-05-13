import pyautogui
import time
import sys

office_file_image = None
while office_file_image is None:
    office_file_image = pyautogui.locateOnScreen('./EX/ex0414/office.png')
    print(office_file_image)