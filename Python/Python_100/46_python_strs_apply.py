# str 자료형 응용하기
# 1 ~ 20까지의 모든 숫자로 일렬로 놓고 각 자리수의 모든 합을 구해보자
# ex) 10 ~ 15 까지면 ==> 101112131415  것들의 합은 21이다.

a , b = map(int, input().split())

strs = ''
result = 0

for char in range(a, b+1):
    strs += str(char)

for number in strs:
    result += int(number)

print(strs)
print(result)