import pyautogui

fw = pyautogui.getActiveWindow() # 활성화된 창
print(fw)
print(fw.title)
print(fw.left,fw.top,fw.right,fw.bottom)

pyautogui.click(fw.left+25, fw.top+20)
pyautogui.click(fw.left+25, fw.top+20)

for i in pyautogui.getActiveWindow():
    print(i)

try:
    pyautogui.getWindowsWithTitle('제목없음')[0] # 0번째의 '제목없음'이름의 윈도우
    if fw.isActive == False :
        fw.activate()

    if fw.isMaximized == False:
        fw.maximize()

    pyautogui.sleep(1) # 1초 멈춤

    fw.restore()
    fw.close()
except Exception as e:
    print(e)