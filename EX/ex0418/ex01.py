from selenium import webdriver
from selenium.webdriver.common.by import By
import time

web = webdriver.Chrome()
web.get('http://www.naver.com')

ele = web.find_element(by=By.LINK_TEXT,value='카페')
print(ele)

ele.click()
time.sleep(1)
# web.find_element(by=By.XPATH,value='/html/body/div/div/div[2]/div[2]/div/ul/li[5]/a')

web.back()
time.sleep(1)

web.forward() # 앞으로
time.sleep(1)

web.refresh()
time.sleep(1)

# 3초뒤
time.sleep(3)

# 탭닫기
web.close()

# 크롬종료
web.quit()