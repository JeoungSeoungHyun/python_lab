import os
import time

os.system("dir")  # 폴더검색
os.system("mkdir hello")  # 폴더생성
os.system("mv post.py ./hello/")  # 파일이동

workDir = os.path.abspath("./")
print(workDir)

while True:
    time.sleep(1000)
    workDir = os.path.abspath("./")
    workDir += "a.txt"
    f = open(workDir, "r")
