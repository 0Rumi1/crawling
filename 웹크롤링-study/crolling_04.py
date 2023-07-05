from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html, 'html.parser')

html_text = '<span class ="red">Heavens! what a virulent attack!</span>'

object_tag = soup.find('span')
print('object_tag:', object_tag)
print('attrs: ', object_tag.attrs)
print('valueL', object_tag.attrs['class'])
print('text:', object_tag.text)



# 등장인물의 이름: 녹색
nameList = soup.find_all('span', {'class':'green'})
for name in nameList:
    print(name.get_text())

#breakpoint 설정
#F5: 디버깅 시작
#사용키:
# - Step over(F10):한 라인씩 실행
# - Step info(F11):함수 내부로 이동
#continue:
# - 다음 번 breakpoint에서 멈춤 (breakpoint가 더 있는 경우)
# - 프로그램 실행(breakpoint가 없는 경우)


from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

princeList = soup.find_all(text = 'the prince')
print(princeList)
print('the prince count: ', len(princeList))

table_tag = soup.find('table', {'id': 'giftList'})
print('children 개수: ', len(list(table_tag)))
for child in table_tag.children:
    print(child)
    print('-'*30)

desc = soup.find('table', {'id':'giftList'}).descendants
print('descendants 개수: ', len(list(desc)))

for child in soup.find('table', {'id':'giftList'}).descendants:
    print(child)


for sibling in soup.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling)

for sibling in soup.find('tr', {'id':'gift2'}).previous_siblings:
    print(sibling)


# next_sibling, previous_sibling
#ord 문자의 Unicode 정수를 리턴
sibling1 = soup.find('tr', {'id':'gift3'}).next_sibling
print(ord(sibling1)) # ord(문자): 문자의 Unicode 정수를 리턴
sibling1

#next_sibling.next_sibling 이용
sibling2 = soup.find('tr', {'id':'gift3'}).next_sibling.next_sibling
print(sibling2)

#트리 이동: 부모다루기
#parent

style_tag = soup.style
print(style_tag.parent)

img1 = soup.find('img', {'src':'../img/gifts/img1.jpg'})
text = img1.parent.previous_sibling.get_text()
print(text)


#정규표현식 
# 문자열 유효성 검사
# 이메일 주소, 전화번호, 웹사이트 주소 등등
# 회사 내에서 정한 규칙, 조건에 맞는지 확인 (ex. 몇자리, 영어, 숫자 등등)



#############################################
# complil() 사용
#############################################

# [a-z]+ : 알파벳 소문자 

#complie 사용 안함
import re
m = re.match('[a-z]+', 'Python')
print(m)
print(re.search('apple', 'I like apple!')) # 매번 패턴 입력 #7번째부터 apple 이 시작


#comple() 사용
p = re.compile('[a-z]+') # 알파벳 소문자 패턴 #정규식 객체(p) 생성
m = p.match('python')
print(m)
print(p.search('I like apple '))


#findall() 함수
#일치하는 모든 문자열을 리스트로 리턴

p = re.compile('[a-z]+')
print(p.findall('life is too short'))


#search() 함수
#일치하는 첫번째 문자열만 리턴
result = p.search('I like apple 123')
print(result)
print(result.group()) # group(): 일치하는 전체 문자열 리턴

result = p.findall('I like aplle 123')
print(result)



from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

#정규식: ('img.*\.jpg'): img 다음에 임의의 한 문자가 0회 이상: img.jpg, img1.jpg, imga.jpg 등
img_tag = re.compile('/img/gifts/img.*.jpg') #여러개의 이미지를 뽑아올 수 있다.

#find_all()에서 img의 src 속성값에 정규식 사용
images = soup.find_all('img', {'src':img_tag})

for image in images:
    print(image, end=" -> ['src' 속성: ")
    print(image['src'])

    