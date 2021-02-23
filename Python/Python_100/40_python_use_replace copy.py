# 놀이동산에 가자
# 모든 놀이기구는 한번에 타는 인원수 제한은 없다.
# 하지만 제한 무게를 넘으면 무조건 다음 기구를 타야 한다.
# 친구들이 총 몇 명 탈 수 있는지 알 수 있는 프로그램 만들기
'''
ex)
50 첫번째 줄은 제한 무게
5 함께한 친구들의 수
20 탑승할 몸무게1 (몸무게는 무작위)
20 탑승할 몸무게2
20 탑승할 몸무게3
20 탑승할 몸무게4
20 탑승할 몸무게5
'''

limit_weight = int(input())
how_many_friends = int(input())
weight_list = list(map(int, input().split()))
total_weight = 0
count = 0

for number in range(how_many_friends):
    total_weight += weight_list[number]
    if total_weight <= limit_weight:
        count += 1
    else:
        break

print(count)


total = 0
count = 0
limit = int(input())
n = int(input())
 
for i in range(n):
    if total <= limit:
        total += int(input())
        count = i
print(count)

## 두 코드의 차이점은 무엇일까요?

제한무게 = int(input())
친구수 = int(input())
친구몸무게 = []
for i in range(친구수):
    친구몸무게.append(int(input()))

전체몸무게 = 0
for i in range(len(친구몸무게)):
    전체몸무게 += 친구몸무게[i]
    print(전체몸무게, 제한무게)
    if 전체몸무게 > 제한무게:
        print(i)
        break