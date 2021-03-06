# 버블정렬 구현하기

# 버블 정렬 : 두 인전합 원소를 검사하여 정렬하는 방법
# 시간복잡도는 느리지만 코드가 단순하여 자주 사용된다.
# 아래 빈칸을 채워넣자


# def bublle(n, data):
#     for i in range(n-1):
#         for j in range('빈칸'):
#             if data[j] > data[j+1]:
#                 '빈칸'
#     for i in range(n):
#         print(data[i], end=" ")


# n = int(input())

# data = list(map(int, input().split()))

def bublle(n, data):
    if n != len(data):
        return print('만족하지 않은 조건입니다.')
    for i in range(n-1):
        for j in range(i+1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    for i in range(n):
        print(data[i], end=" ")


n = int(input())

data = list(map(int, input().split()))

bublle(n, data)