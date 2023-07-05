from konlpy.tag import Okt

okt = Okt() #Open Korean Text (과거 트위터 형태소 분석기)
text = "마음에 꽂힌 칼한자루 보다 마음에 꽂힌 꽃한송이가 더 아파서 잠이 오지 않는다"

# pos(text): 문자의 각 품사를 태깅
# norm = True: 문자를 정규화, stem = True: 어간을 추출

okt_tag = okt.pos(text, norm=True, stem=True)
print(okt_tag)

# nouns(text): 명사만 리턴
okt_nouns = okt.nouns(text)
print(okt_nouns)


text = '나랏말이 중국과 달라 한자와 서로 통하지 아니하므로, \
우매한 백성들이 말하고 싶은 것이 있어도 마침내 제 뜻을 잘 표현하지 못하는 사람이 많다.\
내 이를 딱하게 여기어 새로 스물여덟 자를 만들었으니, \
사람들로 하여금 쉬 익히어 날마다 쓰는 데 편하게 할 뿐이다.'

okt = Okt()

# morphs(text): 텍스트를 형태소 단위로 나눔
okt_morphs = okt.morphs(text)
print('morphs():\n', okt_morphs)

# 명사만 추출
okt_nouns = okt.nouns(text)
print('nouns():\n', okt_nouns)

# phrases(text): 어절 추출
okt_phrases = okt.nouns(text)
print('nouns():\n', okt_phrases)

# pos(text): 품사를 태깅
okt_pos = okt.pos(text)
print('pos():\n', okt_pos)


