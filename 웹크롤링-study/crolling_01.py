from urllib.request import urlopen
from bs4 import BeautifulSoup #객체 형태로 저장 # 특정한 태그에 접근하여 가져올 수 있음 #이렇게 활용하기 위해 사용


#웹 페이지 가져오기
html = urlopen('https://www.daangn.com//hot_articles')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs)
print(bs.h1) #h1 태그만 반환
print(bs.title)

print('spand', {bs.text.h1})

#print(type(html))
#print(html.read())


#에외 처리
from urllib.error import HTTPError
from urllib.error import URLError




def getTitle(url, tag):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser') #특정 url 에서 body 태그 내부에 파라미터로 전달된 tag ('h2'태그 검색)
        value = bsObj.body.find(tag)
    except AttributeError as e:
        return None
    return value

tag = 'h2'
value = getTitle('http://www.pythonscraping.com/pages/page1.html', tag)
if value == None:
    print(f'{tag} could not be found')
else:
    print(value)

