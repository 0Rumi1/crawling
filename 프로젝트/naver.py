from bs4 import BeautifulSoup
import requests
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# 페이지 넘버 함수
def makePgNum(num):
    if num == 1:
        return num
    elif num == 0:
        return num + 1
    else:
        return num + 9*(num - 1)

# 검색어, 시작 페이지, 끝 페이지
def makeUrl(search, start_pg, end_pg):
    if start_pg == end_pg:                      # 시작 페이지와 종료 페이지 숫자가 같으면 url 리턴
        start_page = makePgNum(start_pg)
        url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&start=" + str(start_page)
        #print("생성url: ", url)
        return url
    else:
        urls = []
        for i in range(start_pg, end_pg + 1):   # 각 url 을 urls 리스트에 담기
            page = makePgNum(i)
            url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&start=" + str(page)
            urls.append(url)
        #print("생성url: ", urls)
        return urls

# 검색 키워드/시작/종료 페이지 input 입력
search = input("검색 키워드 입력")
page = int(input("\n시작 페이지 입력"))  
page2 = int(input("\n종료 페이지 입력")) 
search_urls = makeUrl(search, page, page2)

driver = webdriver.Chrome('C:\\Users\\USER\\_chrome\\chromedriver.exe')
driver.implicitly_wait(3)

# selenium으로 검색 페이지 불러오기
naver_urls = []

for i in search_urls:
    driver.get(i)
    time.sleep(1)

    # 네이버 기사가 있는 기사 css selector 모아오기 => 구글 뉴스기사 뽑을 때도 이러한 방식으로 활용해봐야겠음,,,,
    a = driver.find_elements(By.CSS_SELECTOR, 'a.info')

    # 위에서 생성한 css selector list 하나씩 클릭하여 본문 url얻기
    for i in a:
        i.click()
        # driver.switch_to.window 함수는 탭 변경해줌, 인덱스 1 설정
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1)  # 대기시간 변경 가능

        url = driver.current_url                        
        print(url)

        if "news.naver.com" in url:                         # nws.naver.com 네이버 뉴스 url만 가져오기
            naver_urls.append(url)
        else:
            pass
        driver.close()
        driver.switch_to.window(driver.window_handles[0])   # 이전 탭으로 돌아가기

print(naver_urls)

###naver 기사 본문 및 제목 가져오기###
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/98.0.4758.102"}          # ConnectionError방지

titles = []
contents = []
for i in naver_urls:
    original_html = requests.get(i, headers=headers)
    html = BeautifulSoup(original_html.text, "html.parser")

    # 뉴스 제목 가져오기
    title = html.select("div#ct > div.media_end_head.go_trans > div.media_end_head_title > h2")
    title = ''.join(str(title))
    # html태그제거
    pattern1 = '<[^>]*>'
    title = re.sub(pattern=pattern1, repl='', string=title)
    titles.append(title)
    content = html.select("div#dic_area")

    # 기사 텍스트만 가져오기
    content = ''.join(str(content))     # list합치기

    # html태그제거 및 텍스트 다듬기,  해당 코드는 참고
    content = re.sub(pattern=pattern1, repl='', string=content)
    pattern2 = """[\n\n\n\n\n// flash 오류를 우회하기 위한 함수 추가\nfunction _flash_removeCallback() {}"""
    content = content.replace(pattern2, '')

    contents.append(content)

print(titles)
print(contents)



# 데이터프레임 형태로 가공 (titles,url,contents)
import pandas as pd
news_df = pd.DataFrame({'title': titles, 'link': naver_urls, 'content': contents})



#===================워드 클라우드 생성 ===============================
from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
import platform
text = open('NaverNews_ott 개인추천 알고리즘.csv', encoding='utf-8').read()
okt = Okt() # Open Korean Text 객체 생성

sentences_tag = []
sentences_tag = okt.pos(text)
noun_adj_list = []

nouns = okt.nouns(text)

for word, tag in sentences_tag:
    if tag in ['Noun' , 'Adjective']:
        noun_adj_list.append(word)

print(noun_adj_list)

# 워드 클라우드 전처리 nouns 길이가 1개보다 크면 list 에 담기
noun_adj_list = [n for n in nouns if len(n) > 1]    

counts = Counter(noun_adj_list)

# 가장 많이 나온 단어부터 60개를 저장한다.
tags = counts.most_common(60)
print(tags)

### 단어의 빈도수 csv 파일로 저장
col = ['단어', '빈도수']

#데이터프레임 형태로 가공
df = pd.DataFrame(tags, columns=col)

#csv 파일 저장, utf-8 인코딩 해줘야함
df.to_csv('naver_news_ott.csv', encoding='utf-8', mode='w')

# WordCloud 생성
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
