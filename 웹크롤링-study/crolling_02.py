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

print(soup.title) # <title> 태그 전체를 가져옴
print(soup.title.text) #<title> 태그의 텍스트만 return
print(soup.title.get_text()) #.text 와 동일한 기능

print(soup.title.parent) # <title> 을 포함하는 부모 태그 출력

# 태그를 사용해 직접 접근
#<body> 태그 접근
print(soup.boby)

#<h1> 태그 접근
print(soup.h1)
print(soup.h1.text)

#<a> 태그 접근
# 첫번째 <a> 태그 요소 추출
print(soup.a)
print(soup.a.text)
print(soup.a['href'])
print(soup.a.get('href'))

#find() 함수
# 해당 조건에 맞는 맨 처음 검색 결과를 추출
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_example, 'html.parser')
print(soup.find('div'))
print('-'*20)
#여러 <div> 태그 중 특정 속성을 가지는 항목 추출
print(soup.find('div', {'id':'text_id2'}))

#text 또는 get_text()
#추출된 요소에서 텍스트만 가져옴
#find(태그명, 속성: id 속성의 값)
print('-'*20)

div_text = soup.find('div', {'id':'text_id2'})
print(div_text.get_text())

#find() 함수 활용
#<a> 태그 및 <a> 태그의 href 속성 추출
print('-'*20)

href_link = soup.find('a', {'class':'internal_link'}) #딕셔너리 형태 
href_link = soup.find('a', class_ = 'internal_link') #class_ 파이썬 예약어

print(href_link)
print(href_link['href'])
print(href_link.get('href'))
print(href_link.text)


#find() 함수 활용
# 태그 내부의 모든 속성 (attrs)  inerenal_link 리스트 형태로 가져오기 
print('-'*20)

print('href_link.attrs: ', href_link.attrs)
print('values():', href_link.attrs.values())
values = list(href_link.attrs.values())
print('values[0]: {0}, values[1]: {1}'.format(values[0], values[1]))



print('-'*20)
#class 속성은 여러개의 값을 가질 수 있음
# list 형태로 리턴함
from bs4 import BeautifulSoup
tr = '''
<table>
<tr class="passed a b c" id="row1 example"><td>t1</td></tr>
<tr class="failed" id="row2"><td>t2</td></tr>
</table>
'''
table = BeautifulSoup(tr, 'html.parser')
for row in table.find_all('tr'):
    print(row.attrs)


# attrs 추가해도 되고, 빼도 되고 상관없음
href_value = soup.find(attrs={'href':'www.google.com'})
# href_value = soup.find({'href':'www.google.com'})

print(href_value)
print(href_value['href'])
print(href_value.text)

span_tag = soup.find('span')
print('span tag:', span_tag)
print('attrs:', span_tag.attrs) # 딕셔너리 형태로 출력
print('value:', span_tag.attrs['class'])
print('text:', span_tag.text)


#검색된 모든 태그를 list 형태로 리턴
#find_all()

#bs.find_all('span', {'class':{'green','red'}}) # attrs: 속성, 파이썬 딕셔너리르 받음 (or 속성)
