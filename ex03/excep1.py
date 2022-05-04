
try:
    print(2/0)
except Exception as e:  # catch가 except이다 파이썬에서는
    print(e)
finally:
    print("무조건 실행됨")
