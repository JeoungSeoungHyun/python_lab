f = open("C:/users/green/hello.txt", 'r')

for line in f.readlines():
    print(line)
# while(True):
#     line = f.readline()
#     print(line)
#     # null이 아니라 공백이다
#     if line == "":
#         break
