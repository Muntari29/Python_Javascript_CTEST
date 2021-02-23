# count 사용하기
# 뽑은 후보를 입력하면 당선자와 득표수를 출력하는 프로그램 만들기
# ex) 원영 원영 은비 은비 은비 은비 채연 체연

candidates = input().split()

for mentor in candidates:
    if candidates.count(mentor) >= len(candidates)/2:
        print(f'{mentor}(이)가 총 {candidates.count(mentor)}표로 반장이 되었습니다.')
        break
    else:
        continue


data = list(map(str, input().split()))
count = 0
for i in range(len(data)):
	if data.count(data[i-1]) < data.count(data[i]):
		count = i
print("{}(이)가 총 {}표로 반장이 되었습니다.".format(data[count], data.count(data[count])))