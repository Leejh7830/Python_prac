from ssl import AlertDescription
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui
import pyperclip

web = webdriver.Chrome()

web.get('http://www.danawa.com')
time.sleep(1)
site = pyautogui.getActiveWindow()
if site.isMaximized == False:
    site.maximize()
time.sleep(1)
pyautogui.moveTo(736,158) #검색창이동
time.sleep(1)
pyautogui.click() #검색창클릭
time.sleep(1)
pyperclip.copy('이엠텍 지포스')
pyautogui.hotkey('ctrl','v')
time.sleep(1)
pyautogui.moveTo(828,219) #검색결과이동
time.sleep(1)
pyautogui.click() #검색결과클릭
time.sleep(3)
pyautogui.moveTo(581,599) #이엠텍지포스클릭
time.sleep(1)
pyautogui.click()
time.sleep(3)
# ele = web.find_element(by=By.LINK_TEXT,value='최저가 구매하기')
# ele.click()
pyautogui.moveTo(1110,448) #최저가구매하기
pyautogui.click()
time.sleep(8)

web.quit() #종료