
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

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_example, 'html.parser')
head = soup.select_one('head')
print(head.text)
print(head.text.strip()                                                                                                                                                                                                                                                                                                                                                                                                  )

h1 = soup.select_one('h1')
print(h1)

footer = soup.select_one('h1#footer')
print(footer)

class_link = soup.select_one('a.interal_link')
print(class_link)
#print(class_link.text)
#print(class_link['href'])


# 계층적 하위 태그 접근
# 상위 > 하위 태그
link1 = soup.select_one('div#link > a.external_link')
print(link1)

#find 함수와 비교
link_find = soup.find('div', {'id':'link'})
external_link = link_find.find('a', {'class': 'external_link'})
print('find external_link: ', external_link)

link2 = soup.select_one('div#class1 p#second')
print(link2)

#select() 함수
# 모든 <h1> 태그 검색
h1_all = soup.select('h1')
print(h1_all)

# 모든 url 링크 검색
url_links = soup.select('a')
for link in url_links:
    print(link['href'])


# <div id=“class1”> 내부의 모든 url 검색
div_urls = soup.select('div#class1 > a')
print(div_urls)
print(div_urls[0]['href'])
print(div_urls[1]['href'])


# 여러 항목 검색하기 
# <h1> 태그의 id 가 'heading'과 'footer' 모두 검색
# , 로 나열

h1 = soup.select('#heading, #footer')
print(h1)

url_links = soup.select('a.external_link, a.internal_link')
print(url_links)

