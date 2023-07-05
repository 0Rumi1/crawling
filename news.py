from bs4 import BeautifulSoup
import datetime
import json
import requests

random_url = 'https://hooks.slack.com/services/T6NH7FZLG/B74J31P0V'
res = requests.get('http://www.drapt.com/e_sale/index.htm?page_name=esale_news&menu_key=34')
soup = BeautifulSoup(res.content, 'html.parser')

link_titles = soup.find_all('a', class_='c0000000')
link_dates = soup.find_all('span', class_='ffth fs11 c807f7f')
today_date = datetime.date.today()
today_message = '오늘의 부동산 뉴스 [%s]' % str(today_date)
payload = {'text': today_message}
estate_info_message = json.dumps(payload)
requests.post(random_url, data=estate_info_message)

for num, link_title in enumerate(link_titles):
    if str(today_date) == link_dates[num].get_text():
        # estate_info = '<a herf=\"http://www.drapt.com/e_sale/%s\">%s</a>' % (link_title['href'], link_title.get_text())
        # Reference for creating a link: https://api.slack.com/incoming-webhooks
        estate_info = '%d] <http://www.drapt.com/e_sale/%s|%s>' % (num + 1, link_title['href'], link_title.get_text())
        payload = {'text': estate_info}
        estate_info_message = json.dumps(payload)
        requests.post(random_url, data=estate_info_message)