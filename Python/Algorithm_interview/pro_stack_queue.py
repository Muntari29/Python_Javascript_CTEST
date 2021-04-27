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

    