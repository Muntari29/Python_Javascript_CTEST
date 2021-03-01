# 10진수를 2진수로 바꾸는 프로그램
# ex) 13 -> 1101

number = int(input())

binary = ''

while number > 0: 
    share = number // 2 
    reminder = number % 2
    binary += str(reminder)
    number = share

print(binary[::-1])
# 1101

print(bin(10))
# 1101 python bin 함수 이용하기 10진수 -> 2진수로 표현해줌