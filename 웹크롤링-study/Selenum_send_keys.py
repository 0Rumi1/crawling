#====Selenum 사용=====

from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\USER\\_chrome\\chromedriver.exe') # Windows 사용자
#driver = webdriver.Chrome('C:/Users/USER/_chrome')

driver.get('https://www.google.com')

print(driver.current_url)
print(driver.title)
print(driver.page_source) # HTML 소스 가져오기

driver.implicitly_wait(time_to_wait=5)
#driver.close() # 하나의 탭만 종료
#driver.quit() # webdriver 전체 종료



#====element 접근 예제=====
from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\USER\\_chrome\\chromedriver.exe')
#driver = webdriver.Chrome('C:\\workspace\\chromedriver')
driver.get('http://www.pythonscraping.com/pages/warandpeace.html')
driver.implicitly_wait(5)

# find_element_by_class_name('클래스이름'): 하나의 클래스 이름 검색
name = driver.find_element_by_class_name('green')
print(name.text)
print('-' * 20)

# find_elements_by_class_name('클래스이름'): 해당 클래스 이름을 모두 검색
nameList = driver.find_elements_by_class_name('green')
for name in nameList:
    print(name.text)

#driver.quit()




#====네이버 로그인=====
from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\USER\\_chrome\\chromedriver.exe')
driver.get('https://nid.naver.com/nidlogin.login')

driver.implicitly_wait(3)
#id, 비밀번호 전달
#<input>의 이름이 id를 검색

driver.find_element_by_name('id').send_keys('dldkfma1202')
driver.find_element_by_name('pw').send_keys('adkfmaa12!')

driver.find_element_by_xpath('//*[@id="log.login"]').click()


# 