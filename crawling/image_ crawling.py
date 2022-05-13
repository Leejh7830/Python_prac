from selenium import webdriver
import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import pyautogui

driver = webdriver.Chrome()
driver.get('http://www.google.co.kr/imghp?hl=ko')

word = input("무엇을 검색할까요? : ")
count=int(input("몇 개 저장할까요? : "))

browser = driver.find_element(By.NAME, value='q') #검색창(name='q')에 커서 이동
# browser = driver.find_element_by_name("q")
driver.implicitly_wait(3)
browser.send_keys(word)
browser.send_keys(Keys.RETURN)
time.sleep(5)

'''이미지 src요소를 리스트업해서 이미지 url 저장'''
images = driver.find_elements(By.CSS_SELECTOR,'.rg_i.Q4LuWd') # 구글이미지 css선택자, 공백은 .
images_url = []
for i in images: 
   if i.get_attribute('src')!= None :
        images_url.append(i.get_attribute('src'))
   else :
       images_url.append(i.get_attribute('data-src')) # 종종있음
driver.close()

# def selenium_scroll_option():
#   SCROLL_PAUSE_SEC = 3
  
#   # 스크롤 높이 가져옴
#   last_height = driver.execute_script("return document.body.scrollHeight")
  
#   while True:
#     # 끝까지 스크롤 다운
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     # 1초 대기
#     time.sleep(SCROLL_PAUSE_SEC)
#     # 스크롤 다운 후 스크롤 높이 다시 가져옴
#     new_height = driver.execute_script("return document.body.scrollHeight")
  
#     if new_height == last_height:
#         break
#     last_height = new_height



# url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwCARoLY3opNP8zi65sn58_xnxa-OfJ46ssg&usqp=CAU"
# urllib.request.urlretrieve(url, image_name)
# driver.close()

# if image_name == 'shark' :   
for i, url in enumerate(images_url, 1):
    urllib.request.urlretrieve(url, 'C:\src\\'+word+'_'+str(i)+'.jpg')
    if i >= count:
        pyautogui.alert(i+' 개 '+'다운로드 완료!')
        driver.close()

