from ssl import AlertDescription
from selenium import webdriver
import time
import pyautogui
import pyperclip

web = webdriver.Chrome() # 크롬켜기
web.get('http://www.instagram.com') # 인스타 이동
time.sleep(1)

site = pyautogui.getActiveWindow()
if site.isMaximized == False:
    site.maximize() # 최대화

pyautogui.moveTo(1064,362) 
pyautogui.click()
pyperclip.copy('rabbit_adorable2') ########### ID 입력부분
pyautogui.hotkey('ctrl','v')
pyautogui.moveTo(1040,404)
pyautogui.click()
pyperclip.copy('tkfkd1199') ########### PW 입력부분
pyautogui.hotkey('ctrl','v')
pyautogui.hotkey('enter') # 로그인
time.sleep(5)
pyautogui.moveTo(518,151,duration=1)
pyautogui.click() # 메인으로 이동

pyautogui.moveTo(956,721,duration=1)
pyautogui.click() # 알림 닫기
pyautogui.moveTo(1314,146,duration=1)
pyautogui.click() # 탐색 이동
time.sleep(3)
web.refresh() # 게시물 갱신
time.sleep(3)
pyautogui.moveTo(621,339,duration=1)
pyautogui.click() # 첫번째 게시물 이동
time.sleep(1)
for i in range(10): ############# 반복횟수 = n * 10
    for j in range(10): # 10개로 고정(게시물갱신해야함)
        Like = pyautogui.locateOnScreen('./Instagram/images/heart.PNG')
        pyautogui.click(Like) # 좋아요
        Next = pyautogui.locateOnScreen('./Instagram/images/next.PNG')
        pyautogui.click(Next) # 다음
        time.sleep(1)
    pyautogui.moveTo(1796,381) # 빈공백클릭
    pyautogui.click()
    web.refresh() # 게시물 갱신
    time.sleep(3)
    pyautogui.moveTo(621,339,duration=1)
    pyautogui.click() # 다시 첫번째 게시물 이동
    time.sleep(30) # 휴식이 필요한것으로 보임.. 좋아요 빨리 누르면 리밋

web.close()
pyautogui.alert('실행 완료!')
# 중간종료 ctrl + alt + del.