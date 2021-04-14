# 세트

# 빈 세트 생성
A = set()

# 삽입
A.add("10000")
A.add(100)
print(A)
# {'10000', 100}

# 탐색
print(100 in A) # True
print(5 in A) # False

# 삭제
A.remove(100)

# 길이 확인
len(A)