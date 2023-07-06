from selenium import webdriver
from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
import platform
import sys
from PIL import Image
import numpy as np

driver = webdriver.Chrome('C:\\Users\\USER\\_chrome\\chromedriver.exe')
driver.get('https://www.google.com')
search_box = driver.find_element_by_name('q')
search_box.send_keys('ott 개인 추천 알고리즘')
search_box.submit() #   검색어를 전달

a=driver.find_elements_by_class_name('dyjrff.qzEoUe')
for i in range(0,10,2):
    if a[2].text=='› news › articleView':




okt = Okt() # Open Korean Text 객체 생성

google_urls = []

for i in search_urls:
    driver.get(i)
    time.sleep(1)  # 대기시간 변경 가능

    # 네이버 기사가 있는 기사 css selector 모아오기
    a = driver.find_elements(By.CSS_SELECTOR, 'a.info')

    # 위에서 생성한 css selector list 하나씩 클릭하여 본문 url얻기
    for i in a:
        i.click()

# #목표url설정 (빅데이터와 인공지능 활용..디지털농업 혁명이 시작됐다.)
target1 = driver.find_elements_by_class_name('iUh30.qLRx3b.tjvcx')
target1
target1[2].click() #0번 인덱스 
# print('-' * 20)

#     #기사 2번

# news_list_1, news_list_2, news_list_3, news_list_4, news_list_5 = [], [], [], [], []
article-body
gisa2 = driver.find_elements_by_class_name('article-body')
for   idx in   gisa2:
    value_1 = idx.text
    # news_list_1.append(value[:])

# print(value_1)
# print('\n' * 3)
driver.back()



target2 = driver.find_elements_by_class_name('iUh30.qLRx3b.tjvcx')
target2
target2[6].click() #8번 인덱스 
# print('-' * 20)

gisa2 = driver.find_elements_by_class_name('article-body')
for   idx in   gisa2:
    value_2 = idx.text
    # news_list_2.append(value[:])

# print(value_2)
# print('\n' * 3)
driver.back()


target3 = driver.find_elements_by_class_name('iUh30.qLRx3b.tjvcx')
target3
target3[8].click() #8번 인덱스 
# print('-' * 20)

gisa3 = driver.find_elements_by_class_name('article-body')
for   idx in   gisa3:
    value_3 = idx.text
    # news_list_3.append(value[:])

# print(value_3)
# print('\n' * 3)
driver.back()

target4 = driver.find_elements_by_class_name('iUh30.qLRx3b.tjvcx')
target4
target4[12].click() #8번 인덱스 
# print('-' * 20)

gisa4 = driver.find_elements_by_class_name('_3EPBy')
for   idx in   gisa4:
    value_4 = idx.text
    # news_list_4.append(value[:])

# print(value_4)
# print('\n' * 3)
driver.back()

target5 = driver.find_elements_by_class_name('iUh30.qLRx3b.tjvcx')
target5
target5[18].click() #8번 인덱스 
# print('-' * 20)

gisa5 = driver.find_elements_by_class_name('tagdiv-type')
for   idx in   gisa5:
    value_5 = idx.text
    # news_list_5.append(value[:])

# print(value_5)
# print('\n' * 3)
driver.back()


value_sum = value_1, value_2, value_3, value_4, value_5

with open('texts.txt','w', encoding='UTF-8') as f:
    for name in value_sum:
        f.write(name+'\n')




#리스트 합치기
# list_sum = news_list_1 + news_list_2 + news_list_3 + news_list_4 + news_list_5
# print(list_sum)

#워드 클라우드

from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
import platform
text = open('texts.txt', encoding='utf-8').read()
okt = Okt() # Open Korean Text 객체 생성

# okt함수를 통해 읽어들인 내용의 형태소를 분석한다.
sentences_tag = []
sentences_tag = okt.pos(text)
noun_adj_list = []

nouns = okt.nouns(text)

# tag가 명사이거나 형용사인 단어들만 noun_adj_list에 넣어준다.
for word, tag in sentences_tag:
    if tag in ['Noun' , 'Adjective']:
        noun_adj_list.append(word)

print(noun_adj_list)

noun_adj_list = [n for n in nouns if len(n) > 1]

counts = Counter(noun_adj_list)

# 가장 많이 나온 단어부터 60개를 저장한다.
tags = counts.most_common(60)
print(tags)

# WordCloud를 생성
# 한글을 분석하기위해 font를 한글로 지정해주어야 된다.
# macOS는 .otf , window는 .ttf 파일의 위치를 지정 (ex. '/Font/GodoM.otf')
if platform.system() == 'Windows':
    path = r'c:\Windows\Fonts\malgun.ttf'
elif platform.system() == 'Darwin': # Mac OS
    path = r'/System/Library/Fonts/AppleGothic'
else:
    path = r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'

wc = WordCloud(font_path=path, background_color="white", width=400, height=400, scale=2.0, max_font_size=250)
cloud = wc.generate_from_frequencies(dict(tags))
# 생성된 WordCloud를 test.jpg로 보낸다.
#cloud.to_file('test.jpg')
plt.figure(figsize=(10, 8))
plt.axis('off')
plt.imshow(cloud)
plt.show()