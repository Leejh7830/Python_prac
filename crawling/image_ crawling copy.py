from selenium import webdriver
import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import pyautogui
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

form_class = uic.loadUiType("./crawling/CrawlingGui.ui")[0] # UI 불러오기
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self) # UI 화면출력
        self.setWindowTitle('First Application(Image Crawling v0.1)')
        self.setClickEvent()

    def setClickEvent(self):
        self.ok_btn.clicked.connect(self.inputfunc) # 확인버튼 클릭 시 연결
        # self.cancel_btn.clicked.connect(QCoreApplication.instance().quit) # 종료

    def inputfunc(self):
        word = self.textBox_word.toPlainText() # toPlain : 값 가져오기
        count = int(self.textBox_count.toPlainText())
        
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
        print('검색어입력, 리턴까지 완료')

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

        print('이미지 저장 전')

        def image_download():
            '''이미지 src요소를 리스트업해서 이미지 url 저장'''
            for i in range(count):
                images = driver.find_elements(By.CSS_SELECTOR,'.rg_i.Q4LuWd') # 구글이미지 css선택자, 공백은 .
                images_url = []
                for i in images: 
                    if i.get_attribute('src')!= None :
                        images_url.append(i.get_attribute('src'))
                    else :
                        images_url.append(i.get_attribute('data-src')) # 종종있음
                # driver.close()

            print('리스트에 저장 완료')

            for i, url in enumerate(images_url, 1):
                urllib.request.urlretrieve(url, 'C:\\Users\\Lee\\Desktop\\DEV\\Python\\python_work\\crawling\\img\\'+word+'_'+str(i)+'.jpg')
                print(i)
            
                    

        # if count >= 50:
        #     selenium_scroll_option()
        #     print('스크롤 완료1')
        #     driver.find_element(By.CLASS_NAME,'mye4qd').click()
        #     print('스크롤 더보기 클릭')
        #     selenium_scroll_option()
        #     print('스크롤 완료2')
        #     image_download()
        #     print('이미지 download 완료')
        # else :
        #     image_download()
        #     print('이미지 download 완료')
        image_download()
        print('이미지 download 완료')


        print('여기까지 오나?!!!')
        
    # def exitfunc(self):
        
if __name__ == "__main__" : # 인터프리터에서 실행 할 경우
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    print('프로그램 시작')
    app.exec_() # app 닫으면 -> return 0 -> exec_(0) -> app 종료, 닫기전까진 대기상태
    print('프로그램 종료')






