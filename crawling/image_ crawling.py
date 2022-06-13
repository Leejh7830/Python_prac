from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
import pyautogui
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

form_class = uic.loadUiType("./crawling/CrawlingGui.ui")[0] # UI 불러오기
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self) # UI 화면출력
        self.setWindowTitle('First Application(Image Crawling v0.1)')
        self.setClickEvent()
        self.initUI()

    def initUI(self):
        saveAction = QAction('저장(Save)', self)
        loadAction = QAction('불러오기(Load)', self)
        exitAction = QAction(QIcon('crawling/src/exit.png'), '종료(Exit)', self)
        exitAction.setShortcut('Ctrl+C') # Ctrl+C 로 종료가능
        exitAction.setStatusTip('프로그램을 종료합니다.') # 마우스 올렸을 때 도움말(화면아래쪽표시)
        exitAction.triggered.connect(qApp.quit)
        randImg = QAction('랜덤이미지 뽑기',self)
        help = QAction('도움말(Help)',self)
        

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File') # & : F에 단축키 설정 (Alt+F)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(loadAction)
        fileMenu.addAction(exitAction)
        insertMenu = menubar.addMenu('&Insert')
        insertMenu.addAction(randImg)
        helpMenu = menubar.addMenu('&Help')
        helpMenu.addAction(help)

    def setClickEvent(self):
        self.ok_btn.clicked.connect(self.startFunc) # 확인버튼 클릭 시 연결
        self.clear_btn.clicked.connect(self.clearFunc)
          
    def startFunc(self):
        word = self.wordBox.toPlainText() # toPlain : 값 가져오기
        count = int(self.countBox.toPlainText())
        
        # driver = webdriver.Chrome()
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
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

        print("검색 단어 : " + word)
        print("검색 횟수 : " + str(count))

        browser = driver.find_element(By.NAME, value='q') #검색창(name='q')에 커서 이동
        # browser = driver.find_element_by_name("q")
        driver.implicitly_wait(3)
        browser.send_keys(word)
        browser.send_keys(Keys.RETURN)
        time.sleep(5)

        print('검색어입력, 리턴')

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
            
            print('스크롤 완료')

        def image_download():
            '''이미지 src요소를 리스트업해서 이미지 url 저장'''
            images = driver.find_elements(By.CSS_SELECTOR,'.rg_i.Q4LuWd') # 구글이미지 css선택자, 공백은 .
            images_url = []
            n = 1
            for i in images: 
                if i.get_attribute('src')!= None :
                    images_url.append(i.get_attribute('src'))
                else :
                    images_url.append(i.get_attribute('data-src')) # 종종있음
                n += 1
                if n > count:
                    break

            print('리스트에 저장 완료')

            for i, url in enumerate(images_url, 1):
                # urllib.request.urlretrieve(url, 'C:\\Users\\Lee\\Desktop\\DEV\\Python\\python_work\\crawling\\download_img\\'+word+'_'+str(i)+'.jpg')
                urllib.request.urlretrieve(url, 'crawling\\download_img\\'+word+'_'+str(i)+'.jpg')

            print('다운로드 완료')
           
                    

        if count >= 50:
            selenium_scroll_option()
            driver.find_element(By.CLASS_NAME,'mye4qd').click()
            print('스크롤 더보기 클릭')
            selenium_scroll_option()
            image_download()
        else :
            image_download()
        
        driver.quit() # 드라이버까지 완전 종료
        
        


        
    def clearFunc(self):
        self.wordBox.clear()
        self.countBox.clear()
        
if __name__ == "__main__" : # 인터프리터에서 실행 할 경우
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    print('프로그램 시작')
    app.exec_() # app 닫으면 -> return 0 -> exec_(0) -> app 종료, 닫기전까진 대기상태
    print('프로그램 종료')






