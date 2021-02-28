# 각 자리수의 합
# ex) 1234 =>  1 + 2 + 3 + 4 = 10

number_str = input()

sum_number = 0

for number in number_str:
    sum_number += int(number)

print(sum_number)


n = list(map(int,input()))
result = 0
for i in n:
	result += i
	
print(result)


result = 0
for i in input():
    result += int(i)

print(result)