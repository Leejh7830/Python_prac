import pyautogui
import pyperclip

def opennote():
    # 메모장 열기
    pyautogui.hotkey('win','r')
    pyautogui.write('notepad')
    pyautogui.hotkey('enter')
    pyautogui.sleep(1)
    # 글 작성
    pyautogui.write('12345')
    pyautogui.hotkey('enter')
    pyautogui.write('aaaaa')
    pyautogui.hotkey('enter')


def copyandpaste(str):
    pyperclip.copy(str) # 복 붙
    pyautogui.hotkey('ctrl','v')
    pyautogui.sleep(1)

def exit():
    fw = pyautogui.getActiveWindow() # 활성화된 창
    fw.close()
    pyautogui.sleep(1)
    pyautogui.write('n') # 저장하시겠습니까? N  

def printnotepade():
    print('notepad',__name__)