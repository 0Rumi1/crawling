from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

#find_all 하면 list 형태로 가져오기 때문에 for 문에 넣을 때 각각 필요한 정보만 인덱스에 넣으면 됨

#리스트
store, lo, addr, number = [], [], [], []


#for 문으로 페이지에 접근
for page_num in range(54):
        url = urlopen(f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page_num+1}&sido=&gugun=&store=')

        #html 정보 파싱
        soup = BeautifulSoup(url.read(), 'html.parser')

        #할리스 매장 테이블 정보 가져오기 및 텍스트 추출
        # string.split('나누는 문자열') => a.split('/t')
        tbody_tagg = soup.select('tbody > tr')
        for i in tbody_tagg:
            value = i.text.split('\n')
           # print(value)

            store.append(value[3])
            lo.append(value[2])
            addr.append(value[5])
            number.append(value[-2])

        # #list 묶기
        list_sum = list(zip(store,lo, addr, number))

        #데이터프레임 컬럼명 지정
        col = ['매장이름', '위치(시,구)', '주소', '전화번호']

        #데이터프레임 형태로 가공
        df = pd.DataFrame(list_sum, columns=col)

        #csv 파일 저장, utf-8 인코딩 해줘야함
        df.to_csv('hollys_branches.csv', encoding='utf-8', mode='w')

        # for j in list_sum:
        #     j_list = list(j)
        #     print(j_list)
            
        #     print ('매장 이름: {1}, 지역: {2}'.format(j_list, j_list))



        #     #contains 검색어 > 특정 검색어만 입력했을 때, 데이터 값 검색이 됨