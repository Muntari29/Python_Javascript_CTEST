# 프로그래머스 스택/큐 2번 문제
# 주식가격 

# 큐를 이용한 풀이 
# Solution_1

from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)

    while len(q) > 0:
        pop_price = q.popleft()
        time = 0
        for price in q:
            # 가격이 떨어지는 경우
            if pop_price > price:
                time += 1
                break
            else:
                time += 1

        answer.append(time)

    return answer

# [1,2,3,2,3]
def solution2(prices):
    # 인덱스 에러가 발생하지 않도록 인덱스 초기화를 해준다!
    answer = [0] * len(prices)
    stack = [0]
    for i in range(1, len(prices)):
        if prices[i] < prices[stack[-1]]:
            for j in stack[::-1]:
                if prices[i] < prices[j]:
                    answer[j] = i-j
                    stack.remove(j)
                else:
                    break
        stack.append(i)
    for i in range(0, len(stack)-1):
        answer[stack[i]] = len(prices) - stack[i] - 1
    return answer
