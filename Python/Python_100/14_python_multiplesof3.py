# 3의 배수라면 짝 , 3의 배수가 아니라면 n 그대로 출력

n = int(input())

if n % 3 == 0:
    print("짝")
else:
    print(n)