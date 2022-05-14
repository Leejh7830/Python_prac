from pyparsing import Word
from selenium import webdriver
import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import pyautogui
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("./crawling/CrawlingGui.ui")[0]
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setEvent()

    def setEvent(self):
        self.ok_btn.clicked.connect(self.inputfunc)
        self.cancel_btn.clicked.connect(self.exitfunc)

    def inputfunc(self):
        word = self.textBox_input.text()
        count = self.textBox_count.text()

    def exitfunc(self):



word = input("무엇을 검색할까요? : ")
count=int(input("몇 개 저장할까요? : "))

driver = webdriver.Chrome()
driver.get('http://www.google.co.kr/imghp?hl=ko')
window = pyautogui.getActiveWindow() # 활성화된 창
try:
    pyautogui.getWindowsWithTitle('Google 이미지')[0]
    if window.isActive == False :
        window.activate()

    if window.isMaximized == False:
        window.maximize()

    pyautogui.sleep(1)

except Exception as e:
    print(e)

browser = driver.find_element(By.NAME, value='q') #검색창(name='q')에 커서 이동
# browser = driver.find_element_by_name("q")
driver.implicitly_wait(3)
browser.send_keys(word)
browser.send_keys(Keys.RETURN)
time.sleep(5)

def selenium_scroll_option():
  # 스크롤 높이 가져옴
  last_height = driver.execute_script("return document.body.scrollHeight")
  
  while True:
    # 끝까지 스크롤 다운
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    # 스크롤 다운 후 스크롤 높이 다시 가져옴
    new_height = driver.execute_script("return document.body.scrollHeight")
  
    if new_height == last_height:
        break
    last_height = new_height

selenium_scroll_option()
driver.find_element(By.CLASS_NAME,'mye4qd').click()
selenium_scroll_option()


'''이미지 src요소를 리스트업해서 이미지 url 저장'''
images = driver.find_elements(By.CSS_SELECTOR,'.rg_i.Q4LuWd') # 구글이미지 css선택자, 공백은 .
images_url = []
for i in images: 
   if i.get_attribute('src')!= None :
        images_url.append(i.get_attribute('src'))
   else :
       images_url.append(i.get_attribute('data-src')) # 종종있음
driver.close()

for i, url in enumerate(images_url, 1):
    urllib.request.urlretrieve(url, 'C:\\Users\\Lee\\Desktop\\DEV\\Python\\python_work\\crawling\\img\\'+word+'_'+str(i)+'.jpg')
    if i >= count:
        pyautogui.alert('다운로드 완료!')
        # print('다운로드 완료!')
        driver.close()
