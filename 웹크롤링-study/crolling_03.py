#모든 div 태그 검색
# find_all() 함수
from bs4 import BeautifulSoup

html_example = '''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BeautifulSoup 활용</title>
</head>
<body>
    <h1 id="heading">Heading 1</h1>
    <p>Paragraph</p>
    <div id="link">
        <a class="external_link", href="www.google.com">google</a>

        <div id="class1">
            <p id="first">class1's first paragraph</p>
            <a class="exteranl_link", href="www.naver.com">naver</a>

            <p id="second">class1's second paragraph</p>
            <a class="internal_link", href="/pages/page1.html">Page1</a>
            <p id="third">class1's third paragraph</p>
        </div>
    </div>
    <div id="text_id2">
        Example page
        <p>g</p>
    </div>
    <h1 id="footer">Footer</h1>
</body>
</html>
'''

soup = BeautifulSoup(html_example, 'html.parser') # 전체 div 태그를 모두 검색 (리스트 형태로 반환)
div_tags = soup.find_all('div')

print('div_tag length: ', len(div_tags))
for div in div_tags:
    print('------------------------------------------------------')
    print(div)



#<a> 모든 a 태그 검색 및 속성 보기

links = soup.find_all('a')

for alink in links:
    print(alink)
    print('url:{0}, text:{1}'.format(alink['href'], alink.get_text()))
    print()
    print('------------------------------------------------------')

# 특정 태그 중 여러 속성값을 한 번에 검색
# 여러 <a> 태그에서 2개의 class 속성값 검색

link_tags = soup.find_all('a', {'class':['external_link', 'internal_link']}) # 리스트 형태
print(link_tags)


p_tags = soup.find_all('p', {id: ['first', 'third']})
for p in p_tags:
    print(p)
    print('------------------------------------------------------')


#select() 함수 ==> find_all()
#select() 함수는 find_all() 와 유사
#조건에 맞는 모든 태그를 리턴


#select_one() 함수 ==> find()
#조건에 맞는 첫번째 태그만 리턴
#find() 와 유사
 
