import pyautogui

pyautogui.hotkey('win','r')
pyautogui.write('mspaint')
pyautogui.hotkey('enter')
paint = pyautogui.getActiveWindow()

pyautogui.sleep(1)

try :
    # pyautogui.getActiveWindowTitle('제목 없음')[0]

    if paint.isActive == False :
        paint.activate()

    if paint.isMaximized == False:
            paint.maximize()
except Exception as e:
    print(e)
# pyautogui.click(884,151) # 최대화
# pyautogui.click(884,151) # 최대화
pyautogui.sleep(1)
pyautogui.click(336,73) # 텍스트입력기 클릭
pyautogui.sleep(1)
pyautogui.click(254,349) # 빈화면 클릭

pyautogui.sleep(2)
pyautogui.write('참 잘했어요..')
pyautogui.sleep(2)

paint.close()
pyautogui.sleep(1)
pyautogui.write('n') # 저장하시겠습니까? N