

#csv 파일 읽기 read_csv, pandas 
#입력한 도시 정보 검색 > input 
#무한반복 while 문 사용 
# input, if == quit 입력 시, while 문 종료 break
# 만약 검색된 매장이 없으면, 검색된 ㄷ매장이 없습닏. 문구 출력

import pandas as pd
 
# csv 파일 내 한글이 있으므로 encoding utf-8 
df = pd.read_csv('Bigdata_calss\크롤링\hollys_branches.csv', encoding='utf-8')
#print(df)




while True:
    a = input(f'검색할 매장의 도시를 입력하세요: ')
    if a == 'quit':
        print('종료')
        break
    # else: 
    #     str.contains("", na = False)
    #     print('-'*20)
    #     print(f'검색된 매장 수 : {input}')


