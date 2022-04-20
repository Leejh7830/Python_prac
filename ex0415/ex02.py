import pyautogui
from notepad import copyandpaste, opennote, exit


# notefw = pyautogui.getWindowsWithTitle('제목 없음')[0]
# notefw.activate()

def start():
    opennote() # 메모장 열기
    copyandpaste('이클립스') # 복사 붙여넣기
    pyautogui.sleep(1)
    exit()

    # print('ex02py',_n_name__)





    
