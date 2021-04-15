# 스택

from collections import deque

A = deque()

# 맨 뒤 데이터 추가
A.append(1)
A.append(22)
A.append(333)

# 맨 앞 삭제
A.popleft()

# 맨 뒤 삽입
A.append(300)

# 맨 뒤 삭제
A.pop()

# 길이 확인
len(A)