# 문자열 속 문자 찾기
# 해당 문자로 시작하는 index를 반환하는 프로그램 만들기

sentence = 'pineapple is very apple'
str_data_exists = 'apple'
str_data_does_not_exists = '123'

print(sentence.find(str_data_exists))
# 4

print(sentence.find(str_data_does_not_exists))
# -1

print(sentence.index(str_data_exists))
# 4

print(sentence.index(str_data_does_not_exists))
# ValueError: substring not found

# point find method 와 index method의 차이

# find => 특정 문자열을 찾고 첫 인덱스를 반환 없을 경우  -1 반환!
# index => 특정 문자열을 찾고 첫 인덱스를 반환 없을 경우 Error 발생!