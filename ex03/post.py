
class Post:
    # self에는 메모리에 띄운 클래스의 주소가 자동 바인딩 되게 된다.
    def __init__(self, username, password):
        self.username = username
        self.password = password


p = Post("ssar", "1234")

print(p)
print(p.__dict__)
