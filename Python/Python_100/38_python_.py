# 호준이의 아르바이트
# 학생 점수는 공백으로 구분하여 입력한다.
# 1 ~ 3위 학생에게는 사탕을 주며 1~ 3위는 중복될 수 있으며 중복된 사람도 포함하여 사탕을 줘야한다.
# 사탕을 몇개 사면 되는지 프로그램으로 만들기
# ex) 97 86 75 66 55 97 85 97 97 95


# socres = list(map(int, input().split()))
scores = [97, 86, 75, 66, 55, 97, 85, 97, 97, 95]

set_scores = set(scores)
# {97, 66, 75, 85, 86, 55, 95}
count = 0

for i in range(3):
    max_value = max(set_scores) # 97
    count += scores.count(max_value)
    set_scores.remove(max_value)

print(count)


user_input = input()

l = list(user_input.strip().split())
l = [int (i) for i in l]

count = 3
#3개는 무조건 구매, 배열 정렬 후 1~3위 중 중복되는 숫자까지 포함

data_sorted = sorted(list(l))

print(data_sorted)
for i in range(len(l)-1, 0, -1):
	if data_sorted[-3] == l[i]:
		count += 1
print(count)