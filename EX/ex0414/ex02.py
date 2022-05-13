import pyautogui as pyg

img = pyg.screenshot()
img.save('ss.png')

# print(pyg.mouseInfo())



result = pyg.pixelMatchesColor(285,300,(139,184,139))
print(result)