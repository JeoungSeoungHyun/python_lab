# 크롤링

# maven repository처럼 pip에서 찾아서 설치
# python -m pip install beautifulsoup4
# python -m pip install bs4

import requests
from bs4 import BeautifulSoup

# 리스트
list = []

# 기사번호
number = 1

aid = format(number, '010')

# catch 횟수 체크
count = 0

# 객체
article = {
    sid: ""
}

while count < 31:
    try:
        html = requests.get(
            f"https://n.news.naver.com/mnews/article/005/{aid}?sid=100")
        if(html.status_code == 200):
            list.append(html.text)
            number = number + 1
            count = 0
            print(len(list))
    except Exception as e:
        count = count+1
        pass
