import pyautogui

file_menu = pyautogui.locateOnScreen('./ex0414/bogi.png')
print(file_menu)

pyautogui.click(file_menu,duration=2)