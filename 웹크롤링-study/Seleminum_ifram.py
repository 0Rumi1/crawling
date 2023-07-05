
# beatiful soup 으로는 iframe 접근이 되지 않아, selenium 을 사용해야한다.
# - 현재 페이지 > 다른 웹 페이지를 불러와 삽입
# 아래 예제는 iframe 내에 html 이 있음 > 해당 html 에 원하는 데이터가 있다.

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\USER\\_chrome\\chromedriver.exe') #본인의 webdriver 경로
driver.get('https://blog.naver.com/swf1004/221631056531')

driver.switch_to.frame('mainFrame') #=> iframe name 이 mianFrame 으로 지정, # (1) 해당 iframe 으로 이동

html = driver.page_source           
soup = BeautifulSoup(html, 'html.parser')   # BeautifulSoup 과 연동하여 내부 html 과 파싱

whole_border = soup.find('div', {'id': 'whole-border'})
results = whole_border.find_all('div', {'class': 'se-module'})

result1=[]
for result in results:
    print(result.text.replace('\n', ''))
    result1.append(result.text)



#동적 웹페이지 크롤링 예제 코드

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\USER\\_chrome\\chromedriver.exe')
driver.get('https://www.coffeebeankorea.com/store/store.asp')


#storePop2(1) 호출
# 팝업 창에 1번 매장인 '학동역 DT점' 나타남

driver.execute_script('storePop2(1)')

# 함수 호출 결과 페이지를 별도로 저장 후 beautifulSoup 과 연동
# page_source 
# - requests.get() 함수를 사용해서 가져온 text 내용과 동일
# - BeautifulSoup 과 연동해서 필요한 정보 크롤링
html = driver.page_source # page_source 해당 웹페이지의 소스가 저장됨
soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify()) #html 소스를 보기 좋게 출력

store_names = soup.select('div.store_txt > p.name > span')
store_names_list = []

for name in store_names:
    store_names_list.append(name.get_text())
#print(store_info)

print('매장 개수: ', len(store_names_list))
print(store_names_list)

store_addresses = soup.select('p.address > span')
store_addresse_list = []

for addr in store_addresses:
    print(addr.get_text())



#for i in store_info:
#    print(i.text)

'''
           <div class="txt_box">
            <p class="name">
             창원상남동점
            </p>
            <p class="addr">
             <span>
              경남 창원시 성산구 중앙대로 104 마이우스오피스텔 123호 207호
             </span>
             <!--span class="lot">서울특별시 강남구 신사동 648-12</span-->
             <span>
              055-211-0737
             </span>
            </p>
           </div> '''




