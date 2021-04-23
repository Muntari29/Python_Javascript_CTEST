# 프로그래머스 스택/ 큐 문제 1번
# 다리를 지나는 트럭

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque([0] * bridge_length)

    while queue:
        answer += 1
        queue.popleft()
        print(f"1 : {queue}, {answer}")
        if truck_weights:
            print(f"1: {truck_weights}")
            if sum(queue) + truck_weights[0] <= weight:
                queue.append(truck_weights[0])
                truck_weights.pop(0)
                print(f" if : {truck_weights}")
            else:
                queue.append(0)
                print(f" else: {truck_weights}")
        print(f"2 : {queue}, {answer}")

    return answer

print(solution(2, 10, [7, 4, 5, 6]))


# 시간복잡도 해결!!!!! 효율 O(n^2) = O(2n^2)으로 예상되는 첫번째 로직을
# O(n)으로 줄임 

def solution2(bridge_length, weight, truck_weights):
    answer = 0
    sum_weights = 0
    queue = deque([0] * bridge_length)
    truck_weights_list = truck_weights[::-1]
    

    while queue:
        answer += 1
        tr = queue.popleft()
        print(f"1 : {queue}, {answer}, {sum_weights}")
        sum_weights -= tr
        if truck_weights_list:
            if sum_weights + truck_weights_list[-1] <= weight:
                queue.append(truck_weights_list[-1])
                t = truck_weights_list.pop()
                sum_weights += t
            else:
                queue.append(0)
        print(f"2 : {queue}, {answer}, {sum_weights}")

    return answer