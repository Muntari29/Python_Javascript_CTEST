# Factory 함수 만들기
# 2 제곱, 3 제곱, 4 제곱을 할 수 있는 함수를 만들자

def one(number):
    def two(value):
        return value ** number
    return two

a = one(2)
print(a)
# <function one.<locals>.two at 0x7fde3c25e670>
'''
a 는 결국 아래와 같은 two 함수가 된다.
def two(value):
    return value ** 2
number = 2인 two 함수 왜냐하면 return이 two 함수이기때문이다.
'''

b = one(3)
print(b)
# <function one.<locals>.two at 0x7fde3c25e700>
'''
마찬가지로 b 도
number = 3인 two 함수가 된다.
'''
c = one(4)
print(c)
# <function one.<locals>.two at 0x7fde3c25e790>
'''
마찬가지로 c 도
number = 4인 two 함수가 된다.
'''
print(a(10)) # 100
print(b(10)) # 1000
print(c(10)) # 10000
'''
따라서, a(10) => 10 ** 2 / b(10) => 10 ** 3 / b(10) => 10 ** 4가 되는 것이다.
'''
## one(2)를 a에 할당 / one(3) b에 할당 / one(4)를 c에 할당
## a는 one 함수에 인자로 2를 넣고 리턴하는 two 함수를 받는다! 이는 a = one(2)아래의 주석과도 같은 의미이다.

'''
권장 답안

def one(n):
    def two(value):
        sq = value ** n
        return sq
    return two

a = one(2)
b = one(3)
c = one(4)
print(a(10))
print(b(10))
print(c(10))
'''