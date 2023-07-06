national_anthem = '''
<!DOCTYPE html>
<html lang="en">
<head>
<title>애국가</title>
</head>
<body>
    <div>
        <p id="title">애국가</p>
        <p class="content">
            동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>

        </p>
        <p class="content">
        남산 위에 저 소나무 철갑을 두른 듯 바람서리 불변함은 우리 기상일세.<br>
        무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>

        </p>
        <p class="content">
        가을 하늘 공활한데 높고 구름 없이 밝은 달은 우리 가슴 일편단심일세.<br>
        무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>

        </p>
        <p class="content"> 이 기상과 이 맘으로 충성을 다하여 괴로우나 즐거우나 나라 사랑하세.<br>
        무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>

        </p>
    </div>
</body>
</html>
'''

from bs4 import BeautifulSoup

soup = BeautifulSoup(national_anthem, 'html.parser')
print(soup.select_one('p#title').text)

contents = soup.select('p.content')
for content in contents:
    print(content.text)



html = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Title</title>
</head>
<body>
<div class="question">
<div id="stats1">
<span class="item_number">0</span>
<span class="item_unit">votes</span>
</div>
<div id="stats2">
<span class="item_number">10</span>
<span class="item_unit">answer</span>
</div>
<div id="stats3">
<span class="item_number">15</span>
<span class="item_unit">views</span>
</div>
</div>
</body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')
# class 이름이 item_unit인 항목 모두 검색
# select 사용
item_units = soup.select('.item_unit')
print('select item units : \n', item_units)
print('='*50)

# find_all() 사용
find_item_units = soup('span', {'class':'item_unit'})

