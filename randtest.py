# 만약 배민에서 음식을 고를려고 하는데
# 선택하기 힘들어 메뉴를 추천 기능을 이용
# 치킨, 피자, 분식, 중식
# 무작위(랜덤)
import random
print(random.random())

menu = ['치킨', '피자', '분식', '중식']
print(random.choice(menu))

import requests
from bs4 import BeautifulSoup
 
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get("https://m2.melon.com",headers=headers)
r = requests.get("https://m2.melon.com")
print(r)
soup = BeautifulSoup(data.text, 'html.parser')
#print(soup)

title = soup.select_one('#conts > div.chart > div > ul > li.on.nth1 > div > ul > li:nth-child(1) > div.rank_cntt > div.rank_info > p > a')
print(title.text)
title = soup.select_one('#conts > div.chart > div > ul > li.on.nth1 > div > ul > li:nth-child(2) > div.rank_cntt > div.rank_info > p > a')
print(title.text)
title = soup.select_one('#conts > div.chart > div > ul > li.on.nth1 > div > ul > li:nth-child(3) > div.rank_cntt > div.rank_info > p > a')
print(title.text)
title = soup.select_one('#conts > div.chart > div > ul > li.on.nth1 > div > ul > li:nth-child(4) > div.rank_cntt > div.rank_info > p > a')
print(title.text)
title = soup.select_one('#conts > div.chart > div > ul > li.on.nth1 > div > ul > li:nth-child(5) > div.rank_cntt > div.rank_info > p > a')
print(title.text)
title = soup.select_one('#conts > div.chart > div > ul > li.on.nth1 > div > ul > li:nth-child(5) > div.rank_cntt > div.rank_info > p > a')
print(title.text)
title = soup.select_one('#conts > div.chart > div > ul > li.on.nth1 > div > ul > li:nth-child(6) > div.rank_cntt > div.rank_info > p > a')
print(title.text)
title = soup.select_one('#conts > div.chart > div > ul > li.on.nth1 > div > ul > li:nth-child(7) > div.rank_cntt > div.rank_info > p > a')
print(title.text)
title = soup.select_one('#conts > div.chart > div > ul > li.on.nth1 > div > ul > li:nth-child(8) > div.rank_cntt > div.rank_info > p > a')
print(title.text)
title = soup.select_one('#conts > div.chart > div > ul > li.on.nth1 > div > ul > li:nth-child(9) > div.rank_cntt > div.rank_info > p > a')
print(title.text)
title = soup.select_one('#conts > div.chart > div > ul > li.on.nth1 > div > ul > li:nth-child(10) > div.rank_cntt > div.rank_info > p > a')
print(title.text)
