# 거꾸로 출력하기
# 한줄에 여러개의 숫자가 입력되면 역순으로 그 숫자들을 하나씩 출력하는 프로그램 만들기
# ex) 1 2 3 4 5
numbers = list(map(int, input().split()))

print(*numbers[::-1])
# 5 4 3 2 1


n = input()

l = list(n.strip().split())
len1 = len(l) - 1
for i in range(len1, -1, -1):
	print(l[i], end=' ')