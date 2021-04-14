# 큐

from collections import deque

A = deque()

# 맨 앞 삽입
A.appendleft(100)
# 맨 앞 삭제
A.popleft()
# 맨 뒤 삽입
A.append(300)
# 맨 뒤 삭제
A.pop()
# 길이 확인
len(A)