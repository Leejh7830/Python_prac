import pyautogui
from sqlalchemy import false

pyautogui.hotkey('win','r')
pyautogui.write('mspaint')
pyautogui.hotkey('enter')

print(pyautogui.getActiveWindow())
