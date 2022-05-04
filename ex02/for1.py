# for 문 연습

for i in range(1, 11, 2):
    print(i)

list = [1, 2, 3, 4]

for i in list:
    print(i)

tuple = (1, 2, 3, 4)

for i in tuple:
    print(i)

for i in tuple:
    for j in tuple:
        print(i*j)
