# 리스트

# 빈 리스트 선언
A = []
# 추가

A.append(1)
A.append(20)
'''
A = [1, 20]
'''
# 접근
A[0]
A[1] = 200
'''
A = [1, 200]
'''
# 맨 뒤 삭제
A.pop()
'''
A = [1]
'''
# 길이 확인
len(A)
# 삽입
# index, 값
A.insert(1, 300)
# 삭제
# index
del A[1]
'''
A = [1, 300] => [1]
'''
# 탐색
print(1 in A)
# True
print(2 in A)
#False