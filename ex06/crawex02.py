# 크롤링

# maven repository처럼 pip에서 찾아서 설치
# python -m pip install beautifulsoup4
# python -m pip install bs4

import requests
from bs4 import BeautifulSoup

# aid = 1
# aid = ["0000000001", "0000000002", "1000000003"]

# for a in aid:
#     try:
#         html = requests.get(
#             f"https://n.news.naver.com/mnews/article/005/{a}?sid=100")
#         print(html.status_code)
#         if(html.status_code == 200):
#             list.append(html.text)
#     except Exception as e:
#         pass

# print(len(list))

# 파이썬 자릿수 포맷 하는 방법
# print(format(aid, '010'))
# print('{0:010d}'.format(aid))


# 리스트
list = []

# 기사번호
number = 1

aid = format(number, '010')

# catch 횟수 체크
count = 0

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


# 테스트 2
# for number in range(1, 11):
#     aid = format(number, '010')
#     print(aid)
#     try:
#         html = requests.get(
#             f"https://n.news.naver.com/mnews/article/005/{aid}?sid=100")
#         if(html.status_code == 200):
#             print(html)
#             list.append(html.text)
#             aid = aid + 1
#             count = 0
#             print(len(list))
#     except Exception as e:
#         count = count+1
#         pass


# 테스트
# for number in range(1, 11):
#     aid = format(number, '010')
#     print(aid)
#     html = requests.get(
#         f"https://n.news.naver.com/mnews/article/005/{aid}?sid=100")
#     print(html)
