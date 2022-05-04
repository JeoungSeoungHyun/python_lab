# 함수 (클래스 내부에 있는 것이 아닌 것들을 함수)

def add():
    print("더하기")


def minus():
    return 1


add()

print(minus())

# 디폴트 값은 앞에 오지 못한다.
# 오버로딩 하는 방법 1,2,3


def multi(n1, n2=3):
    print(f"곱하기 {n1}*{n2}")


multi(3, 2)
multi(2)


def my_dict(**data):  # **는 여러가지 인수를 하나로 합쳐주는 문법 dict 변환 문법(이 때 키값이 있어야 한다는 점에 주의하자)
    print(data)
    pass  # 메서드에서 아무것도 하고싶지 않을 때 pass를 사용


my_dict(id=1, username="ssar")

n1 = 1


def vartest():
    global n1  # 타입이 없어서 선언인지 재사용인지 알 수 없기 때문에 재사용한다는 의미로 global을 사용한다
    n1 = 2


print(n1)

vartest()

print(n1)
