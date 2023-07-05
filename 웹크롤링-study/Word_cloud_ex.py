from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
import platform

text = open('test.txt', encoding='utf-8').read()
okt = Okt()

sentences_tag = []
sentences_tag = okt.pos(text)

noun_adj_list = []

for word, tag in sentences_tag:
    if tag in ['Noun', 'Adjective']:
        noun_adj_list.append(word)

print(noun_adj_list)

counts = Counter(noun_adj_list)
tags = counts.most_common(40)
print(tags)


#WordCloud 생성

if platform.system() == 'Windows':
    path = r'c:\Windows\Fonts\malgun.ttf'
elif platform.system() == 'Darwin': # Mac OS
    path = r'/System/Library/Fonts/AppleGothic' 
else:
    path = r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'

wc = WordCloud(font_path=path, background_color='white', max_font_size=60)
cloud = wc.generate_from_frequencies(dict(tags))

plt.figure(figsize=(10,8))
plt.axis('off')
plt.imshow(cloud)
plt.show()



# 네이버뉴스 타이틀 Word Cloud ex2
