# 소수를 판별하는 프로그램 만들기
# 소수면 YES 소수가 아니면 NO

number = int(input())

# n 소수 판별하기 -> 2 부터 n-1까지 나눠봐야함

for count in range(2, number):
    if number % count == 0:
        print(False)
        break
    else:
        print(True)
        break

# 시간 복잡도가 O(n)으로 n의 크기가 커질 수록 비효율적이다. 

# 제곱근을 이용하여 소수를 판별해보자.
# 16 의 약수는 1, 2, 4, 8, 16 으로 가운데 4를 기준으로 1*16, 2*8 로 표현이 가능하다.
# 이를 이용해 소수의 절반에 해당하는 제곱근까지만 살펴보면 소수 판별이 가능하다는 것을 알 수 있다.
# a = math.sqrt(10) ==> 3.16 이기에 int와 함께 +1로 3을 포함하여 반복할 수 있도록 해준다.

# 제곱근까지만 보고 소수를 판별해보자
# 2**(1/2)로도 가능하기는 하다.

import math

for count in range(2, int(math.sqrt(number))+1):
    if number % count == 0:
        print(False)
        break
    else:
        print(True)
        break

# 이때 시간 복잡도는 O(n^(1/2)) 이기도 하다.
# 추가로 소수를 판별하는 알고리즘으로 많은 소수를 구하거나 or 소수의 범위를 구할때 유용한 에라토스테네스의 체 알고리즘이 있다.

# 에라토스테네스의 체
# 1은 제거
# 지워지지 않은 수 중 제일 작은 2를 소수로 채택하고, 2의 배수를 모두 제거
# 지워지지 않은 수 중 제일 작은 3를 소수로 채택하고, 3의 배수를 모두 제거
# 지워지지 않은 수 중 제일 작은 5를 소수로 채택하고, 5의 배수를 모두 제거
# 위 과정을 반복하여 남은 수는 소수다 라는 것이 결론이다.
# 이는 해당 수 보다 작은 모든 수로 나누어 보아 소수를 판별하는 무식하지만 가장 강력한 방법이다.
import math

def isPrime(number):
    # 2부터 number까지의 모든 수에 대하여 소수 판별
    # 처음엔 모든 수가 소수(True)로 초기화 0과 1은 제외
    check_list = [True for i in range(number+1)]

    # 에라토스테네스의 체
    # 2부터 number의 제곱근까지 모든 수를 확인
    for check_number in range(2, int(math.sqrt(number))+1):
        if check_list[check_number] == True: # check_number 가 소수인 경우 (남은 수 인경우)
            j = 2 # check_number를 제외한 모든 배수를 지운다.
            while check_number * j <= number:
                check_list[check_number * j] = False
                j += 1
    
    return [ prime for prime in range(2, number+1) if check_list[prime]]
# 1,000,000 이내로 주어지는 경우 활용할 것을 권장!
# 시간 복잡도 O(N loglogN) 으로 선형그래프에 가까움


# # 에라토스테네스의 체 2
n=1000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
print(primes)
