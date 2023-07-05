#구글에 검색어 전달
#Submit()

from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('C:\\Users\\USER\\_chrome\\chromedriver.exe')
driver.get('https://google.com')

driver.implicitly_wait(1)

serch_box = driver.find_element_by_name('q')
serch_box.send_keys('ott 개인맞춤 알고리즘')    #검색어 전달
serch_box.submit()


#목표url설정 (빅데이터와 인공지능 활용..디지털농업 혁명이 시작됐다.)
target2 = driver.find_elements_by_class_name('iUh30.qLRx3b.tjvcx')
target2
target2[2].click()
print('-' * 20)

gisa2 = driver.find_elements_by_class_name('ctsType1')
# for idx in gisa2:
#     print(idx.text)
# driver.back()


#기사 2번
# gisa2 = driver.find_elements_by_class_name('ctsType1')
# for idx in gisa2:
#     print(idx.text)
# driver.back()