# from 뒤에는 폴더나 파일이 올수있다.
# from 뒤에 파일이면 import는 그 파일 내부의 함수나 변수 등등
# from 뒤에 폴더면 import는 그 폴더내부의 파일

# from cos import add, minus
from cos import add as a, minus as m

a.add()

m.minus()
