# Creating a dictionary from key values (2 values)

keys = input().split()
values = map(int, input().split())


student_score = dict(zip(keys, values))

print(keys) 
# ['승희', '희승']
print(values)
# <map object at 0x7fe6f18696d0> 맵 객체
print(student_score)
# {'승희': 10, '희승': 20}

# Python zip 내장함수 문제!
# zip()은 동일한 개수로 이루어진 자료형을 튜플로 묶어주는 역할을 하는 함수이다.