# from selenium import webdriver
# from wordcloud import WordCloud
# from konlpy.tag import Okt
# from collections import Counter
# import matplotlib.pyplot as plt
# import platform
import pandas as pd
# import sys


# driver = webdriver.Chrome('C:\\Users\\USER\\_chrome\\chromedriver.exe')
# driver.get('https://www.google.com')
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ott 개인 추천 알고리즘')
# search_box.submit() #   검색어를 전달

# okt = Okt() # Open Korean Text 객체 생성

# # 1번 기사 클릭
# target1 = driver.find_elements_by_class_name('iUh30.qLRx3b.tjvcx')
# target1
# target1[2].click() #2번 인덱스 
# # print('-' * 20)

# # 1번 기사 본문 내용 스크래핑
# gisa2 = driver.find_elements_by_class_name('smartOutput')
# for   idx in   gisa2:
#     value_1 = idx.text
# driver.back()

# #2번 기사
# target2 = driver.find_elements_by_class_name('iUh30.qLRx3b.tjvcx')
# target2
# target2[6].click() 

# gisa2 = driver.find_elements_by_class_name('se-main-container')
# for   idx in   gisa2:
#     value_2 = idx.text
# driver.back()

# #3번 기사
# target3 = driver.find_elements_by_class_name('iUh30.qLRx3b.tjvcx')
# target3
# target3[8].click()  
# # print('-' * 20)

# gisa3 = driver.find_elements_by_class_name('article-body')
# for   idx in   gisa3:
#     value_3 = idx.text

# driver.back()

# #4번 기사
# target4 = driver.find_elements_by_class_name('iUh30.qLRx3b.tjvcx')
# target4
# target4[12].click()

# gisa4 = driver.find_elements_by_class_name('_3EPBy')
# for   idx in   gisa4:
#     value_4 = idx.text
# driver.back()

# #5번 기사
# target5 = driver.find_elements_by_class_name('iUh30.qLRx3b.tjvcx')
# target5
# target5[14].click() 

# gisa5 = driver.find_elements_by_class_name('tagdiv-type')
# for   idx in   gisa5:
#     value_5 = idx.text
# driver.back()


# # 문자열 합치기
# value_sum = value_1, value_2, value_3, value_4, value_5

# # 텍스트 파일로 저장 > 워드 클라우드 생성을 위한 과정
# with open('texts.txt','w', encoding='UTF-8') as f:
#     for name in value_sum:
#         f.write(name+'\n')


#워드 클라우드

from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
import platform
text = open('texts.txt', encoding='utf-8').read()
okt = Okt() # Open Korean Text 객체 생성

# okt함수를 통해 읽어들인 내용의 형태소 분석
sentences_tag = []
sentences_tag = okt.pos(text)
noun_adj_list = []

nouns = okt.nouns(text)

# tag가 명사이거나 형용사인 단어들만 noun_adj_list에 넣음
for word, tag in sentences_tag:
    if tag in ['Noun' , 'Adjective']:
        noun_adj_list.append(word)

print(noun_adj_list)

# 워드 클라우드 전처리 과정
# nouns 길이가 1개보다 크면 list 에 담기
noun_adj_list = [n for n in nouns if len(n) > 1]

counts = Counter(noun_adj_list)

# 가장 많이 나온 단어부터 60개를 저장
tags = counts.most_common(60)
print(tags)

### 단어의 빈도수 csv 파일로 저장
col = ['단어', '빈도수']

# 데이터프레임 형태로 가공
df = pd.DataFrame(tags, columns=col)

# csv 파일 저장, utf-8 인코딩 해줘야함
df.to_csv('hollys_branches.csv', encoding='utf-8', mode='w')

if platform.system() == 'Windows':
    path = r'c:\Windows\Fonts\malgun.ttf'
elif platform.system() == 'Darwin': # Mac OS
    path = r'/System/Library/Fonts/AppleGothic'
else:
    path = r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'

wc = WordCloud(font_path=path, background_color="white", width=400, height=400, scale=2.0, max_font_size=250)
cloud = wc.generate_from_frequencies(dict(tags))

plt.figure(figsize=(10, 8))
plt.axis('off')
plt.imshow(cloud)
plt.show()