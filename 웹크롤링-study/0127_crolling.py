
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
soup = bs(html, 'html.parser')
for link in soup.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])



print('='*50)


#패턴파악이 우선
#전방부정 탐색을 통해 케빈과 관련된 기사만 검색
#위키백과와 연관된 기사 내용만 뽑기 

#<div id = 'bodyContent' class = "vector-body">




from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import re

#random.seed(None)

def getLinks(articleUrl):

    html = urlopen('https://en.wikipedia.org' + articleUrl)
    bs = BeautifulSoup(html, 'html.parser')
    body_content = bs.find('div', {'id': 'bodyContent'})
    wikiUrl = body_content.find_all('a', href = re.compile('^(/wiki/)((?!:).)*$'))
    return wikiUrl

links = getLinks('/wiki/Kebink_Bacon')
print('link 길이: ', len(links))
while(len(links)) > 0:
    newArticle = link[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)



#getLinks() 함수 set 사용: 동일한 페이지를 두번 크롤링 방지
#>> 디버깅이 어렵고, 메모리를 많이 차지한다.(스택이 많이 쌓임) 대신, 구현이 쉽다.
#재귀 함수 > 스택 해당 함수가 끄탄ㄹ 때까지 호출 이후의 명령문 수행 안됨, 반드시 종료 조건이 포함되어야함 (무한 루프 방지)
#stack 에 저장되기 떄문에 종료 조건이 없으면 stack overflow 발생 :: 메모리에 쌓임

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set() #세트 선언
count = 0

def getLinks(pageUrl):
    global pages
    html = urlopen('https://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a', href = re.compile('^(/wiki/)')):
        if link.attrs['href'] not in pages:
            newPage = link.attrs['href']

            count += 1
            print('[{0}]: {1}'.format(count, newPage))
            pages.add(newPage)
            getLinks(newPage)

getLinks('')

