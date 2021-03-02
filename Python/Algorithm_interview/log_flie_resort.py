# 로그 파일 재정렬

# 로그의 가장 앞 부분은 식별자이다.
# 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
# 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일한 경우 식별자 순으로 한다.
# 숫자 로그는 입력 순서대로 한다.

logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]

# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

# 문자 로그와 숫자 로그를 판별
letters = []  
digits = []

for log in logs:
    if log.split()[1].isdigit():
        digits.append(log)
    else:
        letters.append(log)

# 판별된 문자 로그를 정렬

letters.sort(key= lambda x: x.split()[0]) # 식별자를 먼저 정렬
letters.sort(key= lambda x: x.split()[1:]) # 식별자를 제외하고 문자열에 대해 정렬한다.

# 아래와 같이 1줄로 줄일 수 있다!
# 식별자를 제외한 문자열 [1:]을 키로 하여 정렬하며, 동일한 경우 후순위로 식별자[0]을 지정해 정렬되도록 표현한 것이다!
# letters.sort(key= lambda x: (x.split()[1:], x.split()[0]))

print(letters + digits) # 리스트 연결 -> 숫자 로그는 입력 순서대로 한다.
# ['g1 act car', 'a8 act zoo', 'ab1 off key dog', 'a1 9 2 3 1', 'zo4 4 7']


# # # # # # # # # # # # # # # # # # # # # # # # # 

# 문자가 동일할 경우 식별자를 이용해 다시 정렬된다.
# 람다를 2번 사용할 경우, 실제로 식별자는 후 순위로 정렬이 되나, 식별자를 나중에 정렬할 경우 이전 정렬했던 리스트에 패치되므로 순서에 주의하자.

# 정렬 순서에 따른 값의 변화 알아보기 / key = 문자열 [1:]을 기준으로 먼저 정렬 / 오답
print(f'원본 : {letters}')
letters.sort(key= lambda x: x.split()[1:]) 

print(f'1번 정렬 : {letters}')

letters.sort(key= lambda x: x.split()[0])
print(f'2번 정렬 : {letters}')

# 원본    : ['g1 act car', 'ab1 off key dog', 'a8 act zoo']
# 1번 정렬 : ['g1 act car', 'a8 act zoo', 'ab1 off key dog']
# 2번 정렬 : ['a8 act zoo', 'ab1 off key dog', 'g1 act car']

# 정렬 순서에 따른 값의 변화 알아보기 / key = 문자열 [0]을 기준으로 먼저 정렬 / 정답

print(f'원본 : {letters}')
letters.sort(key= lambda x: x.split()[0]) 

print(f'1번 정렬 : {letters}')

letters.sort(key= lambda x: x.split()[1:])
print(f'2번 정렬 : {letters}')

# 원본    : ['a8 act zoo', 'ab1 off key dog', 'g1 act car']
# 1번 정렬 : ['a8 act zoo', 'ab1 off key dog', 'g1 act car']
# 2번 정렬 : ['g1 act car', 'a8 act zoo', 'ab1 off key dog']

# 람다 표현식 1줄로 표현하기


print(f'원본 : {letters}')

letters.sort(key= lambda x: (x.split()[0], x.split()[1:])) # 오답
print(f'1번 정렬 : {letters}')


letters.sort(key= lambda x: (x.split()[1:], x.split()[0])) # 정답
print(f'2번 정렬 : {letters}')

# 원본    : ['g1 act car', 'ab1 off key dog', 'a8 act zoo']
# 1번 정렬 : ['a8 act zoo', 'ab1 off key dog', 'g1 act car']
# 2번 정렬 : ['g1 act car', 'a8 act zoo', 'ab1 off key dog']