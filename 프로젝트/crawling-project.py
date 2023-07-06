from bs4 import BeautifulSoup
import requests
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import time
import re
import platform


def get_titles(start_num, end_num, search_word, title_list):
    #star_num ~ end_num 까지 크롤링

    while 1:
        if start_num > end_num:
            break
    url = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={}}&start={}'.format(search_word, start_num)
    req = requests.get(url)
    time.sleep(0.5)

    if req.ok:
        soup = BeautifulSoup(req.text, 'html.parser')
        #뉴스 제목 뽑기
        list_news = soup.find('ul', {'class' : 'list_news'})
        li_bxs = list_news.find_all('li', {'class': 'bx'})

        for li_bx in li_bxs:
            news_title = li_bx.find('a', {'class':'news_tit'})
            title_list.append(news_title['title'])

    start_num += 10
    print(title_list)


def make_wordcloud(word_count, title_list):
    okt = Okt()

    sentences_tag = []

    for sentence in title_list:
        morph = okt.pos(sentence)
        sentences_tag.append(morph)
        print(morph)
        print('-' * 30)
    print(sentences_tag)
    print('\n' * 3)
    noun_adj_list = []
    # 명사와 형용사만 구분하여 이스트에 넣기
    for sentence1 in sentences_tag:
        for word, tag in sentence1:
            if tag in ['Noun', 'Adjective']:
                noun_adj_list.append(word)

    # 형태소별 count
    counts = Counter(noun_adj_list)
    tags = counts.most_common(word_count)
    print(tags)


# wordCloud생성
# 한글꺠지는 문제 해결하기위해 font_path 지정
    if platform.system() == 'Windows':
        path = r'c:\Windows\Fonts\malgun.ttf'
    elif platform.system() == 'Darwin': # Mac OS
        path = r'/System/Library/Fonts/AppleGothic'
    else:
        path = r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'

    wc = WordCloud(font_path=path, background_color='white', width=800, height=600)
    print(dict(tags))
    cloud = wc.generate_from_frequencies(dict(tags))
    plt.figure(figsize=(10, 8))
    plt.axis('off')
    plt.imshow(cloud)
    plt.show()

if __name__ == '__main__':
    search_word = "빅데이터" # 검색어 지정
    title_list = []
    # 1~200번게시글 까지 크롤링
    get_titles(1, 20, search_word, title_list)
    # 단어 30개까지 wordcloud로 출력
    make_wordcloud(20, title_list)

