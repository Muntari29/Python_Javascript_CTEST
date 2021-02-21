# 입력된 하나의 문자가 대문자이면 YES / NO 출력하는 프로그램 만들기

str_data = input()

if str_data == str_data.upper():
    print('YES')
else:
    print('NO')

# isupper 사용한 답안

if str_data.isupper():
    print('YES')
else:
    print('NO')