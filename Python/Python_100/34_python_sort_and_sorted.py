# sort 구현하기
# 키가 주어지면 순서대로 제대로 섰는지 확인하는 프로그램 만들기
# ex) 176 156 155 165 166 169
# YES or NO
# list.sort() 와 sorted(list)차이가 핵심!!

hegiht_data = list(map(int, input().split()))
sorted_hegiht_data = sorted(hegiht_data)

if hegiht_data == sorted_hegiht_data:
    print('YES')
else:
    print('NO')

# list.sort() -> 원본 리스트를 정렬하되 None을 반환한다. (원본리스트 변경됨)
# sorted(list) -> 정렬된 새로운 리스트를 반환함 (원본리스트 영향 없음), 모든 반복가능한 객체(iterable)에 동작함
## list.sort()는 새로운 복사본을 만들지 않기 때문에 sorted(list)보다 빠르다.


user_input = input()

l = list(user_input.strip().split())
l = [int (i) for i in l]

if l != sorted(l):
	print("NO")
	
else:
	print("YES")