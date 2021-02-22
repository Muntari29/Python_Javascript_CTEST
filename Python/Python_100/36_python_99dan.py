# Multiplication table / 구구단 출력하기
# ex) 2
# 1 ~ 9까지의 숫자 중 하나를 입력 구구단 결과가 한 줄에 출력되어야 한다.

number = int(input())

for count in range(1, 10):
    print(number * count, end=' ')
    

n = int(input())
for i in range(1, 10):
	print(n*i, end = ' ')
