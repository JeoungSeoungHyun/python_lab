# 크롤링

# maven repository처럼 pip에서 찾아서 설치
# python -m pip install beautifulsoup4
# python -m pip install bs4

import requests
from bs4 import BeautifulSoup

html = requests.get(
    "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8")

# json이 아닌 html이기 때문에 text로 찾는다
# print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')

weather_el = soup.select_one(".weather_graphic .temperature_text > strong")

print(weather_el.get_text())
