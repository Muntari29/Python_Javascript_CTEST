# 프로그래머스 해쉬 1번 문제
# 완주하지 못한 선수

# A = 마라톤에 참가한 사람 ["A", "B", "C"]
# B = 마라톤에 완주한 사람 ["B", "C"]

def solution(participant, completion):
    answer = ''
    A = {}
    count = 0
    
    for part in participant:
        A[hash(part)] = part
        count += int(hash(part))
    
    for com in completion:
        count -= int(hash(com))
    
    answer = A[count]
    
    return answer

# 어떠한 키값(입력값)을 받아도 일정범위의 자연수로 변환하는 hash함수를 이용함
# 해시함수로 반환되는 값을 키값으로 이용해 추상자료형 딕셔너리를 구현
# 동일한 해시값을 반환하는 특성으로 더했던 값을 모두 빼서 남은 값(키)를 이용해 완주하지 못한 사람을 answer로 할당함
# collections 의 Count 객체를 이용해 2줄로 표현이 가능하다고함. 

